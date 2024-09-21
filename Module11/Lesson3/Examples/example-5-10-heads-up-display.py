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
from Core.Matrix import Matrix
from CoreExt.Camera import Camera
from CoreExt.Mesh import Mesh
from CoreExt.Renderer import Renderer
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Geometry.Box import BoxGeometry
from Geometry.Rectangle import RectangleGeometry
from Material.Texture import TextureMaterial
from Extras.MovementRig import MovementRig
from Extras.TextTexture import TextTexture
from Extras.Grid import GridHelper

class Example(Base):
    """
    Demonstrate a heads-up display (HUD): a transparent layer containing some images
    (for example, with a text), rendered after the main scene, and appearing on the top layer.
    Move the camera: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 1.5, 5])
        self.scene.add(self.rig)

        crate_geometry = BoxGeometry()
        crate_material = TextureMaterial(Texture("Data/images/crate.jpg"))
        crate = Mesh(crate_geometry, crate_material)
        crate.translate(0, 0.5, 0)
        self.scene.add(crate)

        grid = GridHelper(grid_color=[1, 1, 1], center_color=[1, 1, 0])
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)

        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, self._screen.get_width(), 0, self._screen.get_height(), 1, -1)

        label_geometry1 = RectangleGeometry(
            width=self._screen.get_width() / 2, height=self._screen.get_width() / 5,
            position=[0, self._screen.get_height()],
            alignment=[0, 1]
        )
        label_material1 = TextureMaterial(Texture("Data/images/crate-simulator.png"))
        label1 = Mesh(label_geometry1, label_material1)
        self.hud_scene.add(label1)

        label_geometry2 = RectangleGeometry(
            width=self._screen.get_width() / 5, height=self._screen.get_width() / 5,
            position=[self._screen.get_width(), 0],
            alignment=[1, 0]
        )
        message = TextTexture(
            text="Version 1.0",
            system_font_name="Ink Free",
            font_size=32,
            font_color=[127, 255, 127],
            image_width=200,
            image_height=200,
            transparent=True
        )
        label_material2 = TextureMaterial(message)
        label2 = Mesh(label_geometry2, label_material2)
        self.hud_scene.add(label2)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(
            scene=self.hud_scene,
            camera=self.hud_camera,
            clear_color=False
        )


# Instantiate this class and run the program
Example().run()
