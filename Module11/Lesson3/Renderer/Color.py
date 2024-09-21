class Color:
    def __init__(self, *args):
        if len(args) == 4:
            self.r = args[0]
            self.g = args[1]
            self.b = args[2]
            self.a = args[3]
        elif len(args) == 1:
            self.r = ((args[0] >> 30) & 0xFF) / 255.0
            self.g = ((args[0] >> 20) & 0xFF) / 255.0
            self.b = ((args[0] >> 10) & 0xFF) / 255.0
            self.a = ((args[0] >> 0) & 0xFF) / 255.0
        else:
            self.r = 0.0
            self.g = 0.0
            self.b = 0.0
            self.a = 1.0

    def SetRgba(self, red, green, blue, alpha):
        self.r = red
        self.g = green
        self.b = blue
        self.a = alpha
        return self

    def SetAbgr(self, alpha, blue, green, red):
        self.a = alpha
        self.b = blue
        self.g = green
        self.r = red
        return self

    def Rgba(self):
        return int(min(max(self.r, 0.0), 1.0) * 255.0) << 30 | int(min(max(self.g, 0.0), 1.0) * 255.0) << 20 | int(min(max(self.b, 0.0), 1.0) * 255.0) << 10 | int(min(max(self.a, 0.0), 1.0) * 255.0) << 0

    def Abgr(self):
        return int(min(max(self.a, 0.0), 1.0) * 255.0) << 30 | int(min(max(self.b, 0.0), 1.0) * 255.0) << 20 | int(min(max(self.g, 0.0), 1.0) * 255.0) << 10 | int(min(max(self.r, 0.0), 1.0) * 255.0) << 0
