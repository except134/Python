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
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Geometry.Rectangle import RectangleGeometry
from Extras.PointLight import PointLightHelper
from Light.Ambient import AmbientLight
from Light.Point import PointLight
from Material.Lambert import LambertMaterial

class Example(Base):
    """ Bump mapping: combining color textures with normal map textures """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 0, 1.5])

        ambient_light = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient_light)
        self.point_light = PointLight(color=[1, 1, 1], position=[1.2, 1.2, 0.3])
        self.scene.add(self.point_light)
        # texture of a brick wall
        color_texture = Texture("Data/images/brick-color.png")
        # texture of normals of the brick wall
        bump_texture = Texture("Data/images/brick-bump.png")

        rectangle_geometry = RectangleGeometry(width=2, height=2)

        color_material = LambertMaterial(
            texture=color_texture,
            number_of_light_sources=2
        )

        bump_material = LambertMaterial(
            texture=color_texture,
            bump_texture=bump_texture,
            property_dict={"bumpStrength": 20},
            number_of_light_sources=2
        )

        # Replace color_material and bump_material
        # in Mesh to see a difference
        mesh = Mesh(rectangle_geometry, bump_material)
        mesh.rotate_y(45)
        self.scene.add(mesh)

        point_light_helper = PointLightHelper(self.point_light)
        self.point_light.add(point_light_helper)

    def update(self):
        self.point_light.set_position([math.cos(0.5 * self.time) / 2, math.sin(0.5 * self.time) / 2, 0.3])
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
