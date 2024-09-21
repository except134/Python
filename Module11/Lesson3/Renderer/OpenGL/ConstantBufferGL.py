from OpenGL.GL import *
from Renderer.ConstantBuffer import ConstantBuffer

class GLConstantBuffer(ConstantBuffer):
    def __del__(self):
        glDeleteBuffers(1, self.id)

    def Init(self):
        glGenBuffers(1, self.id)
        glBindBuffer(GL_UNIFORM_BUFFER, self.id)
        glBufferData(GL_UNIFORM_BUFFER, self.Size(), None, GL_STREAM_DRAW)
        glBindBuffer(GL_UNIFORM_BUFFER, 0)

    def Update(self, data):
        glBindBuffer(GL_UNIFORM_BUFFER, self.id)

        size = self.Size()
        dst = glMapBufferRange(GL_UNIFORM_BUFFER, 0, size, GL_MAP_WRITE_BIT)
        std.memcpy(dst, data, size)
        glUnmapBuffer(GL_UNIFORM_BUFFER)

        glBindBuffer(GL_UNIFORM_BUFFER, 0)

    def Bind(self, binding):
        glBindBuffer(GL_UNIFORM_BUFFER, self.id)
        glBindBufferBase(GL_UNIFORM_BUFFER, binding, self.id)

    def Unbind(self):
        glBindBuffer(GL_UNIFORM_BUFFER, self.id)
