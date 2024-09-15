#!/usr/bin/python3
import math
import pathlib
import sys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[2])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from Core.BasePygame import Base
from CoreExt.Camera import Camera
from CoreExt.Mesh import Mesh
from CoreExt.Renderer import Renderer
from CoreExt.RenderTarget import RenderTarget
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Geometry.Rectangle import RectangleGeometry
from Geometry.Sphere import SphereGeometry
from Material.Texture import TextureMaterial
from Material.Surface import SurfaceMaterial
from Extras.MovementRig import MovementRig
from Extras.Postprocessor import Postprocessor
from Effects.HorizontalBlur import HorizontalBlurEffect
from Effects.VerticalBlur import VerticalBlurEffect
from Effects.AdditiveBlend import AdditiveBlendEffect

class Example(Base):
    """
    Demonstrate a glow effect using two scenes.
    The first one renders the glow effect (blur of a red-material sphere).
    The second (main) one renders blending the first one and the original scene.
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer(clear_color=[0, 0, 0])
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 1, 4])
        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="Data/images/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)

        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="Data/images/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
        self.scene.add(grass)

        sphere_geometry = SphereGeometry()
        sphere_material = TextureMaterial(Texture("Data/images/grid.jpg"))
        self.sphere = Mesh(sphere_geometry, sphere_material)
        self.sphere.set_position([0, 1, 0])
        self.scene.add(self.sphere)

        self.postprocessor = Postprocessor(self.renderer, self.scene, self.camera)

        # glow scene
        self.glow_scene = Scene()
        red_material = SurfaceMaterial(property_dict={"baseColor": [1, 0, 0]})
        glow_sphere = Mesh(sphere_geometry, red_material)
        glow_sphere.local_matrix = self.sphere.local_matrix
        self.glow_scene.add(glow_sphere)

        # glow postprocessing
        glow_target = RenderTarget(resolution=[self._screen.get_width(), self._screen.get_height()])
        self.glow_pass = Postprocessor(self.renderer, self.glow_scene, self.camera, glow_target)
        self.glow_pass.add_effect(HorizontalBlurEffect(texture_size=[self._screen.get_width(), self._screen.get_height()], blur_radius=50))
        self.glow_pass.add_effect(VerticalBlurEffect(texture_size=[self._screen.get_width(), self._screen.get_height()], blur_radius=50))

        # combining results of glow effect with main scene
        self.combo_pass = Postprocessor(self.renderer, self.scene, self.camera)
        self.combo_pass.add_effect(
            AdditiveBlendEffect(
                blend_texture=glow_target.texture,
                original_strength=1,
                blend_strength=3
            )
        )

    def update(self):
        self.sphere.rotate_y(0.01337)
        self.rig.update(self.input, self.delta_time)
        self.glow_pass.render()
        self.combo_pass.render()


# Instantiate this class and run the program
Example().run()
