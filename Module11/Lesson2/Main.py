import random
import numpy as np
import pathlib
import sys
import OpenGL.GL as GL

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
from CoreExt.RenderTarget import RenderTarget
from CoreExt.Scene import Scene
from CoreExt.Texture import Texture
from Geometry.Box import BoxGeometry
from Geometry.Pyramid import PyramidGeometry
from Geometry.Rectangle import RectangleGeometry
from Material.Texture import TextureMaterial

class particle:
    def __init__(self):
        self.ACTIVE = 1  # dead or live
        self.LIFE = 0.0  # len of life
        self.FADE = 0.0  # step of fade

        self.R = 0.0  # red
        self.G = 0.0  # green
        self.B = 0.0  # blue

        self.X = 0.0  # X position
        self.Y = 0.0  # Y position
        self.Z = 0.0  # Z position

        self.Xi = 0.0  # X direction
        self.Yi = 0.0  # Y direction
        self.Zi = 0.0  # Z direction

        self.Xj = 0.0  # X gravity
        self.Yj = 0.0  # Y gravity
        self.Zj = 0.0  # Z gravity

prts = []

# global particles settings
MAX_PARTICLES = 1000  # Number of particles create.
SPEED_PARTICLES = 2.0  # particles speed
XSPEED = 0.0  # speed OX
YSPEED = 0.0  # speed OY
ZOOM = -30.0  # zoom
LOOP = 0  # loop particles
DELAY = 0  # delay

for i in range(MAX_PARTICLES):
    particl = particle()
    prts.append(particl)

colors = [
    [(1.0, 0.5, 0.5), (1.0, 0.75, 0.5), (1.0, 1.0, 0.5), (0.75, 1.0, 0.5)],
    [(0.5, 1.0, 0.5), (0.5, 1.0, 0.75), (0.5, 1.0, 1.0), (0.5, 0.75, 1.0)],
    [(0.5, 0.5, 1.0), (0.75, 0.5, 1.0), (1.0, 0.5, 1.0), (1.0, 0.5, 0.75)],
]

class Example(Base):
    """ Render the sine function """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=self._screen.get_width()/self._screen.get_height())
        self.camera.set_position([0, 0, 2])

        GL.glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
        GL.glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
        GL.glDepthFunc(GL.GL_LESS)  # The Type Of Depth Test To Do
        GL.glDisable(GL.GL_DEPTH_TEST)  # Enables Depth Testing
        GL.glEnable(GL.GL_BLEND)
        GL.glShadeModel(GL.GL_SMOOTH)  # Enables Smooth Color Shading
        
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE)
        GL.glHint(GL.GL_PERSPECTIVE_CORRECTION_HINT, GL.GL_NICEST)
        GL.glHint(GL.GL_POINT_SMOOTH_HINT, GL.GL_NICEST)
        GL.glEnable(GL.GL_TEXTURE_2D)

        max_color = len(colors)

        for i in range(MAX_PARTICLES):
            prts[i]

            prts[i].LIFE = 1.0
            prts[i].FADE = float(random.randrange(0, 100)) / 1000.0 + 0.003

            prts[i].R = colors[i % max_color][0]
            prts[i].G = colors[i % max_color][1]
            prts[i].B = colors[i % max_color][2]

            prts[i].Xi = (float(random.randrange(0, 100) % 50) - 26.0) * 10.0
            prts[i].Yi = (float(random.randrange(0, 100) % 50) - 25.0) * 10.0
            prts[i].Zi = (float(random.randrange(0, 100) % 50) - 25.0) * 10.0

            prts[i].Xj = 0.0
            prts[i].Yj = -0.8
            prts[i].Zj = 0.0

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()  # Reset The Projection Matrix
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def update(self):
        for i in range(MAX_PARTICLES):
            if prts[i].ACTIVE == 1:
                x = float(prts[i].X)
                y = float(prts[i].Y)
                z = float(prts[i].Z + ZOOM)

                GL.glColor4f(prts[i].R == i, prts[i].G == i, prts[i].B == i, prts[i].LIFE)

                GL.glBegin(GL.GL_TRIANGLE_STRIP)
                GL.glTexCoord2d(1, 1)
                GL.glVertex3f(x + 0.5, y + 0.5, z)
                # upper right
                GL.glTexCoord2d(0, 1)
                GL.glVertex3f(x - 0.5, y + 0.5, z)
                # upper left
                GL.glTexCoord2d(1, 0)
                GL.glVertex3f(x + 0.5, y - 0.5, z)
                # bottom right
                GL.glTexCoord2d(0, 0)
                GL.glVertex3f(x - 0.5, y - 0.5, z)
                # bottom left
                GL.glEnd()

                prts[i].X += prts[i].Xi / (SPEED_PARTICLES * 1000)
                prts[i].Y += prts[i].Yi / (SPEED_PARTICLES * 1000)
                prts[i].Z += prts[i].Zi / (SPEED_PARTICLES * 1000)

                prts[i].Xi += prts[i].Xj
                prts[i].Yi += prts[i].Yj
                prts[i].Zi += prts[i].Zj

                prts[i].LIFE -= prts[i].FADE
                if prts[i].LIFE < 0.0:
                    prts[i].LIFE = 1.0
                    prts[i].FADE = float(random.randrange(0, 100) % 100) / 1000.0 + 0.003

                    prts[i].X = 0.0
                    prts[i].Y = 0.0
                    prts[i].Z = 0.0

                    prts[i].Xi = XSPEED + float((random.randrange(0, 100) % 60) - 32.0)
                    prts[i].Yi = XSPEED + float((random.randrange(0, 100) % 60) - 30.0)
                    prts[i].Zi = float((random.randrange(0, 100) % 60) - 32.0)

            else:
                prts[i].ACTIVE = 1
                prts[i].FADE = float(random.randrange(0, 100)) / 1000.0 + 0.003

                prts[i].X = 0.0
                prts[i].Y = 0.0
                prts[i].Z = 0.0


if __name__ == "__main__":
    Example().run()

