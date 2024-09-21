class InputLayout:
    # Define the ElementType Enum class
    class ElementType:
        INT = 1
        UINT = 2
        FLOAT = 3
        FLOAT2 = 4
        FLOAT3 = 5
        FLOAT4 = 6

    def AddElement(self, semantic_name:str, element_type:ElementType):
        pass

    def Bind(self):
        pass

    def Unbind(self):
        pass
