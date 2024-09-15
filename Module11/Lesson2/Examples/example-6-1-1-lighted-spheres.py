#!/usr/bin/python3
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
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Extras.MovementRig import MovementRig
from Geometry.Sphere import SphereGeometry
from Light.Ambient import AmbientLight
from Light.Directional import DirectionalLight
from Light.Point import PointLight
from Material.Flat import FlatMaterial
from Material.Lambert import LambertMaterial
from Material.Phong import PhongMaterial

class Example(Base):
    """
    Demonstrate:
    - the flat shading model;
    - the Lambert illumination model and Phong shading model;
    - the Phong illumination model and Phong shading model.
    The Lambert illumination model uses a combination of ambient and diffuse lighting.
    The Phong illumination model uses ambient, diffuse, and specular lighting.
    In the flat shading model, the light calculations are performed in the vertex shader.
    In the Phong shading model, the light calculations are performed in the fragment shader.

    Move a camera: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 0, 6])
        self.scene.add(self.rig)

        # four light sources
        ambient_light = AmbientLight(color=[0.1, 0.1, 0.1])
        self.scene.add(ambient_light)
        directional_light = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional_light)
        point_light1 = PointLight(color=[0.9, 0, 0], position=[4, 0, 0])
        self.scene.add(point_light1)
        point_light2 = PointLight(color=[0, 0.9, 0], position=[-4, 0, 0])
        self.scene.add(point_light2)

        # lighted materials with a color
        flat_material = FlatMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=4
        )
        lambert_material = LambertMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=4
        )
        phong_material = PhongMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=4
        )

        # lighted spheres with a color
        sphere_geometry = SphereGeometry()
        sphere_left_top = Mesh(sphere_geometry, flat_material)
        sphere_left_top.set_position([-2.5, 1.5, 0])
        self.scene.add(sphere_left_top)
        sphere_center_top = Mesh(sphere_geometry, lambert_material)
        sphere_center_top.set_position([0, 1.5, 0])
        self.scene.add(sphere_center_top)
        sphere_right_top = Mesh(sphere_geometry, phong_material)
        sphere_right_top.set_position([2.5, 1.5, 0])
        self.scene.add(sphere_right_top)

        # lighted materials with a texture
        textured_flat_material = FlatMaterial(
            texture=Texture("Data/images/grid.jpg"),
            number_of_light_sources=4
        )
        textured_lambert_material = LambertMaterial(
            texture=Texture("Data/images/grid.jpg"),
            number_of_light_sources=4
        )
        textured_phong_material = PhongMaterial(
            texture=Texture("Data/images/grid.jpg"),
            number_of_light_sources=4
        )

        # lighted spheres with a texture
        sphere_left_bottom = Mesh(sphere_geometry, textured_flat_material)
        sphere_left_bottom.set_position([-2.5, -1.5, 0])
        self.scene.add(sphere_left_bottom)
        sphere_center_bottom = Mesh(sphere_geometry, textured_lambert_material)
        sphere_center_bottom.set_position([0, -1.5, 0])
        self.scene.add(sphere_center_bottom)
        sphere_right_bottom = Mesh(sphere_geometry, textured_phong_material)
        sphere_right_bottom.set_position([2.5, -1.5, 0])
        self.scene.add(sphere_right_bottom)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
