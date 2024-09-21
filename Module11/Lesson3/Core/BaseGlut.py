from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from Core.Input import Input
from Core.Utils import Utils

# Number of the glut window.
window = 0

class Base:
    def __init__(self, screen_size=(1920, 1080)):
        # Initialize GLUT
        global window
        glutInit(sys.argv)
        # Select type of Display mode:
        #  Double buffer
        #  RGBA color
        # Alpha components supported
        # Depth buffer
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

        # get a 640 x 480 window
        glutInitWindowSize(screen_size[0], screen_size[1])

        # the window starts at the center of the screen
        glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH)-Width)//2,
                           (glutGet(GLUT_SCREEN_HEIGHT)-Height)//2);
        # Okay, like the C version we retain the window id to use when closing, but for those of you new
        # to Python (like myself), remember this assignment would make the variable local and not global
        # if it weren't for the global declaration at the start of main.
        window = glutCreateWindow("Except engine")
        # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
        # set the function pointer and invoke a function to actually register the callback, otherwise it
        # would be very much like the C version of the code.
        glutDisplayFunc(Update)
        # When we are doing nothing, redraw the scene.
        glutIdleFunc(Update)
        # Register the function called when our window is resized.
        glutReshapeFunc(Resize)
        # Register the function called when the keyboard is pressed.
        glutKeyboardFunc(KeyPressed)
        # Initialize our window.
        InitGL(screen_size[0], screen_size[1])
        # Determine ifsmailoop is active
        self._running = True
        # Manage time-related data and operations
        self._clock = pygame.time.Clock()
        # Manage user input
        self._input = Input()
        # number of seconds application has been running
        self._time = 0
        # Print the system information
        Utils.print_system_info()

    @property
    def delta_time(self):
        return self._delta_time

    @property
    def input(self):
        return self._input

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    def initialize(self):
        """ Implement by extending class """
        pass

    def update(self):
        """ Implement by extending class """
        pass

    def run(self):
        # Startup #
        self.initialize()
        # main loop #
        while self._running:
            # process input #
            self._input.update()
            if self._input.quit:
                self._running = False
            # seconds since iteration of run loop
            self._delta_time = self._clock.get_time() / 1000
            # Increment time application has been running
            self._time += self._delta_time
            # Update #
            self.update()
            # Render #
            # Display image on screen
            pygame.display.flip()
            # Pause if necessary to achieve 60 FPS
            self._clock.tick(60)
        # Shutdown #
        pygame.quit()
        sys.exit()
