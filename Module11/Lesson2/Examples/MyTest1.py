import numpy as np
import pathlib
import sys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from Core.BasePygame import Base
from Core.Math import *
from CoreExt.Camera import Camera
from CoreExt.Mesh import Mesh
from CoreExt.Renderer import Renderer
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Geometry.Box import BoxGeometry
from Geometry.Pyramid import PyramidGeometry
from Geometry.Teapot import TeapotGeometry
from Material.Texture import TextureMaterial

class Example(Base):
    """ Render the sine function """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 0, 2])

        grid_texture = Texture(file_name="Data/Images/grid.jpg")
        material = TextureMaterial(texture=grid_texture,
                                   property_dict={"doubleSide": False})

        boxgeometry = BoxGeometry()
        self.boxmesh = Mesh(boxgeometry, material)
        self.boxmesh.set_position([-1.5, 0.0, -1.0])
        self.scene.add(self.boxmesh)

        pyrgeometry = PyramidGeometry()
        self.pyrmesh = Mesh(pyrgeometry, material)
        self.pyrmesh.set_position([1.5, 0.0, -1.0])
        self.scene.add(self.pyrmesh)

        teageometry = TeapotGeometry()
        self.teamesh = Mesh(teageometry, material)
        self.teamesh.set_position([0.0, 0.0, -1.0])
        self.scene.add(self.teamesh)

    def update(self):
        self.boxmesh.rotate_y(0.02514)
        self.teamesh.rotate_x(0.02514)
        self.teamesh.rotate_y(0.02514)
        self.pyrmesh.rotate_y(-0.02514)
        self.renderer.render(self.scene, self.camera)

if __name__ == "__main__":
    Example().run()

