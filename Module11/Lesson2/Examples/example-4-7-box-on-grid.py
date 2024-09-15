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
from Extras.Axes import AxesHelper
from Extras.Grid import GridHelper
from Extras.MovementRig import MovementRig
from Geometry.Box import BoxGeometry
from Material.Surface import SurfaceMaterial

class Example(Base):
    """
    Render axes, a rotated xy-grid, and a box.
    Move the box: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 1, 5])
        geometry = BoxGeometry()
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        self.mesh = Mesh(geometry, material)
        self.rig = MovementRig()
        self.rig.add(self.mesh)
        self.rig.set_position([0, 0.5, 0])
        self.scene.add(self.rig)
        axes = AxesHelper(axis_length=2)
        self.scene.add(axes)
        grid = GridHelper(
            size=20,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
