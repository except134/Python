from OpenGL.GL import *
from Renderer.IndexBuffer import IndexBuffer

class GLIndexBuffer(IndexBuffer):
    def __init__(self, num_indices, data):
        super().__init__(num_indices)
        self.id = 0
        self.id = glGenBuffers(1, self.id) 
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(uint32_t) * num_indices, data, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def __del__(self):
        glDeleteBuffers(1, self.id)

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id)

    def unbind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def draw(self):
        glDrawElements(GL_TRIANGLES, self.num_indices, GL_UNSIGNED_INT, None)


