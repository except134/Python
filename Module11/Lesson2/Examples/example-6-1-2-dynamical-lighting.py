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
from Extras.DirectionalLight import DirectionalLightHelper
from Extras.MovementRig import MovementRig
from Extras.PointLight import PointLightHelper
from Geometry.Sphere import SphereGeometry
from Light.Ambient import AmbientLight
from Light.Directional import DirectionalLight
from Light.Point import PointLight
from Material.Flat import FlatMaterial
from Material.Lambert import LambertMaterial
from Material.Phong import PhongMaterial

class Example(Base):
    """
    Demonstrate dynamical lighting with:
    - the flat shading model;
    - the Lambert illumination model and Phong shading model;
    - the Phong illumination model and Phong shading model;
    and render light helpers that show a light position and
    a light direction for a point light and a directional light,
    respectively.

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

        # three light sources
        ambient_light = AmbientLight(color=[0.1, 0.1, 0.1])
        self.scene.add(ambient_light)
        self.directional_light = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, 0])
        self.scene.add(self.directional_light)
        self.point_light = PointLight(color=[0.9, 0, 0], position=[1, 1, 0.8])
        self.scene.add(self.point_light)

        # lighted materials with a color
        flat_material = FlatMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=3
        )
        lambert_material = LambertMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=3
        )
        phong_material = PhongMaterial(
            property_dict={"baseColor": [0.2, 0.5, 0.5]},
            number_of_light_sources=3
        )

        # lighted spheres with a color
        sphere_geometry = SphereGeometry()
        sphere_left = Mesh(sphere_geometry, flat_material)
        sphere_left.set_position([-2.5, 0, 0])
        self.scene.add(sphere_left)
        sphere_center = Mesh(sphere_geometry, lambert_material)
        sphere_center.set_position([0, 0, 0])
        self.scene.add(sphere_center)
        sphere_right = Mesh(sphere_geometry, phong_material)
        sphere_right.set_position([2.5, 0, 0])
        self.scene.add(sphere_right)

        # helpers
        directional_light_helper = DirectionalLightHelper(self.directional_light)
        # The directional light can take any position because it covers all the space.
        # The directional light helper is a child of the directional light.
        # So changing the global matrix of the parent leads to changing
        # the global matrix of its child.
        self.directional_light.set_position([0, 2, 0])
        self.directional_light.add(directional_light_helper)
        point_light_helper = PointLightHelper(self.point_light)
        self.point_light.add(point_light_helper)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.directional_light.set_direction([-1, math.sin(0.5 * self.time), 0])
        self.point_light.set_position([1, math.sin(self.time), 1])
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
