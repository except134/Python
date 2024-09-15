from OpenGL.GL import *
from Renderer.InputLayout import InputLayout

class GLInputLayout(InputLayout):
    class Element:
        def __init__(self):
            self.num_components = None
            self.type = None
            self.size = None

    def __init__(self, stride):
        self.elements_ = []
        self.stride_ = stride

    def AddElement(self, semantic_name, element_type):
        element = self.Element()
        if element_type == self.ElementType.INT:
            element.num_components = 1
            element.type = GL_INT
            element.size = sizeof(int)
        elif element_type == self.ElementType.UINT:
            element.num_components = 1
            element.type = GL_UNSIGNED_INT
            element.size = sizeof(c_uint32)
        elif element_type == self.ElementType.FLOAT:
            element.num_components = 1
            element.type = GL_FLOAT
            element.size = sizeof(c_float)
        elif element_type == self.ElementType.FLOAT2:
            element.num_components = 2
            element.type = GL_FLOAT
            element.size = sizeof(c_float) * 2
        elif element_type == self.ElementType.FLOAT3:
            element.num_components = 3
            element.type = GL_FLOAT
            element.size = sizeof(c_float) * 3
        elif element_type == self.ElementType.FLOAT4:
            element.num_components = 4
            element.type = GL_FLOAT
            element.size = sizeof(c_float) * 4
        else:
            raise RuntimeError("Invalid layout element type")

        self.elements_.append(element)

    def Bind(self):
        offset_ptr = None
        for i in range(len(self.elements_)):
            element = self.elements_[i]
            glEnableVertexAttribArray(i)
            glVertexAttribPointer(i, element.num_components, element.type, 0, self.stride_, offset_ptr)
            offset_ptr += element.size

    def Unbind(self):
        for i in range(len(self.elements_)):
            glDisableVertexAttribArray(i)
