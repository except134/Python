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
from Geometry.Box import BoxGeometry
from Geometry.Geometry import Geometry
from Material.Surface import SurfaceMaterial
from Material.Texture import TextureMaterial
from Geometry.Sphere import SphereGeometry
from Light.Ambient import AmbientLight
from Light.Directional import DirectionalLight
from Light.Point import PointLight
from Material.Flat import FlatMaterial
from Material.Lambert import LambertMaterial
from Material.Phong import PhongMaterial

class Example(Base):
    """ Example template """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 0, 2])
        geometry = BoxGeometry()
        material = SurfaceMaterial(
            property_dict={
                "useVertexColors": True,
                "wireframe": True,
                "lineWidth": 8
            }
        )
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.mesh.rotate_y(0.0514)
        self.mesh.rotate_x(0.0337)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
