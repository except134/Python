class ConstantBuffer:
    def InitWithLayout(self):
        self.layout = []
        self.padding = 0

        self.SetLayout()
        self.ApplyPadding()
        self.Init()

    def Init(self):
        pass

    def Update(self, data):
        pass

    def Bind(self, binding):
        pass

    def Unbind(self):
        pass

    def Size(self):
        size = 0
        for e in self.layout:
            size += e["size"]
        return size + self.padding

    def SetLayout(self):
        self.layout.append({"size": T})

    def SetLayout(self):
        self.SetLayout()
        self.SetLayout()

    def ApplyPadding(self):
        self.padding = 0
        self.padding = self.Size()
        self.padding = 16 - (self.padding % 16)
