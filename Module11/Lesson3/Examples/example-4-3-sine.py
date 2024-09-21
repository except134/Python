#!/usr/bin/python3
import numpy as np
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
from Geometry.Geometry import Geometry
from Material.Point import PointMaterial
from Material.Line import LineMaterial

class Example(Base):
    """ Render the sine function """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 0, 5])
        geometry = Geometry()
        vs_code = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
        }
        """
        fs_code = """
        uniform vec3 baseColor;
        uniform bool useVertexColors;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor, 1.0);
        }
        """
        position_data = []
        x_values = np.arange(-3.2, 3.2, 0.2)
        y_values = np.sin(x_values)
        for x, y in zip(x_values, y_values):
            position_data.append([x, y, 0])
        geometry.add_attribute("vec3", "vertexPosition", position_data)
        use_vertex_colors = False
        point_material = PointMaterial(vs_code, fs_code, {"baseColor": [1, 1, 0], "pointSize": 10}, use_vertex_colors)
        point_mesh = Mesh(geometry, point_material)
        line_material = LineMaterial(vs_code, fs_code, {"baseColor": [1, 0, 1], "lineWidth": 4}, use_vertex_colors)
        line_mesh = Mesh(geometry, line_material)
        self.scene.add(point_mesh)
        self.scene.add(line_mesh)

    def update(self):
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example().run()
