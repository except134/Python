import math
from typing import overload

class Vector2:
    def __init__(self, *args): 
        if len(args) == 2:
            self.m_x = args[0]
            self.m_y = args[1]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.m_x = args[0][0]
            self.m_y = args[0][1]
        elif len(args) == 1 and isinstance(args[0], Vector2):
            self.m_x = args[0].m_x
            self.m_y = args[0].m_y

    @property
    def x(self):
        return self.m_x    
    @x.setter
    def x(self, v):
        self.m_x = v
    
    @property
    def y(self):
        return self.m_y    
    @y.setter
    def y(self, v):
        self.m_y = v
    
    def setX(self, x):
        self.m_x = x    
        
    def setY(self, y):
        self.m_y = y

    def inverse(self):
        self.m_x = 1.0 / self.m_x
        self.m_y = 1.0 / self.m_y

    def normalize(self):
        len = (self.m_x * self.m_x + self.m_y * self.m_y) ** 0.5
        if len > 0.0:
            inverse = 1.0 / len
            self.m_x *= inverse
            self.m_y *= inverse

    def inversed(self):
        v = Vector2(self)
        v.inverse()
        return v

    def normalized(self):
        v = Vector2(self)
        v.normalize()
        return v

    def angleBetween(self, vec2):
        len_product = self.length() * vec2.length()
        if len_product < 1e-6:
            len_product = 1e-6
        f = self.dotProduct(vec2) / len_product
        return abs(f)

    def length(self):
        return (self.m_x * self.m_x + self.m_y * self.m_y) ** 0.5

    def lengthSquared(self):
        return self.m_x * self.m_x + self.m_y * self.m_y

    def distance(self, vec2):
        return (self - vec2).length()

    def distancesquared(self, vec2):
        return (self - vec2).lengthSquared()

    @staticmethod
    def cross(v1, v2):
        return v1.m_x * v2.m_y - v1.m_y * v2.m_x

    def crossProduct(self, vec2):
        return Vector2.cross(self, vec2)

    @staticmethod
    def dot(v1, v2):
        return v1.m_x * v2.m_x + v1.m_y * v2.m_y

    def dotProduct(self, vec2):
        return Vector2.dot(self, vec2)

    def midPoint(self, vec2):
        return Vector2((self.m_x + vec2.m_x) * 0.5, (self.m_y + vec2.m_y) * 0.5)

    def perpendicular(self):
        return Vector2(-self.m_y, self.m_x)

    @staticmethod
    def add(left, right):
        result = Vector2()
        result.m_x = left.m_x + right.m_x
        result.m_y = left.m_y + right.m_y
        return result

    @staticmethod
    def subtract(left, right):
        result = Vector2()
        result.m_x = left.m_x - right.m_x
        result.m_y = left.m_y - right.m_y
        return result

    @staticmethod
    def multiply(left, right):
        result = Vector2()
        result.m_x = left * right.m_x
        result.m_y = left * right.m_y
        return result

    def __getitem__(self, i):
        return [self.m_x, self.m_y][i]

    def __eq__(self, vec2):
        return self.m_x == vec2.m_x and self.m_y == vec2.m_y

    def __ne__(self, vec2):
        return self.m_x != vec2.m_x or self.m_y != vec2.m_y

    def __add__(self, vec2):
        return Vector2.add(self, vec2)

    def __sub__(self, vec2):
        return Vector2.subtract(self, vec2)

    def __mul__(self, factor: float):
        return Vector2.multiply(factor, self)

    def __truediv__(self, divisor: float):
        return Vector2(self.m_x / divisor, self.m_y / divisor)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def toVector3(self):
        return Vector3(self.m_x, self.m_y, 1.0)

    def toVector4(self):
        return Vector4(self.m_x, self.m_y, 1.0, 1.0)


class Vector3:
    def __init__(self, *args): 
        if len(args) == 3:
            self.m_x = args[0]
            self.m_y = args[1]
            self.m_z = args[2]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.m_x = args[0][0]
            self.m_y = args[0][1]
            self.m_z = args[0][2]
        elif len(args) == 1 and isinstance(args[0], Vector3):
            self.m_x = args[0].m_x
            self.m_y = args[0].m_y
            self.m_z = args[0].m_z

    @property
    def x(self):
        return self.m_x
    @x.setter
    def x(self, v):
        self.m_x = v

    @property
    def y(self):
        return self.m_y
    @y.setter
    def y(self, v):
        self.m_y = v

    @property
    def z(self):
        return self.m_z
    @z.setter
    def z(self, v):
        self.m_z = v

    def setX(self, x):
        self.m_x = x

    def setY(self, y):
        self.m_y = y

    def setZ(self, z):
        self.m_z = z

    def inverse(self):
        self.m_x = 1.0 / self.m_x
        self.m_y = 1.0 / self.m_y
        self.m_z = 1.0 / self.m_z

    def normalize(self):
        len = self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z
        len = len ** 0.5
        if len > 0.0:
            inverse = 1.0 / len
            self.m_x *= inverse
            self.m_y *= inverse
            self.m_z *= inverse

    def inversed(self):
        v = Vector3(self)
        v.inverse()
        return v

    def normalized(self):
        v = Vector3(self)
        v.normalize()
        return v

    def angleBetween(self, vec3):
        len_product = self.length() * vec3.length()
        if len_product < 1e-6:
            len_product = 1e-6
        f = self.dotProduct(vec3) / len_product
        return Math.acos(f)

    def length(self):
        return (self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z) ** 0.5

    def lengthSquared(self):
        return self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z

    def distance(self, vec3):
        return (self - vec3).length()

    def distanceSquared(self, vec3):
        return (self - vec3).lengthSquared()

    @staticmethod
    def cross(v1, v2):
        return Vector3((v1.m_y * v2.m_z) - (v1.m_z * v2.m_y),
                       (v1.m_x * v2.m_z) - (v1.m_z * v2.m_x),
                       (v1.m_x * v2.m_y) - (v1.m_y * v2.m_x))

    def crossProduct(self, vec3):
        return Vector3.cross(self, vec3)

    @staticmethod
    def dot(v1, v2):
        return v1.m_x * v2.m_x + v1.m_y * v2.m_y + v1.m_z * v2.m_z

    def dotProduct(self, vec3):
        return Vector3.dot(self, vec3)

    def midPoint(self, vec3):
        return Vector3((self.m_x + vec3.m_x) * 0.5,
                       (self.m_y + vec3.m_y) * 0.5,
                       (self.m_z + vec3.m_z) * 0.5)

    def perpendicular(self):
        square_zero = 1e-06 * 1e-6
        perp = self.crossProduct(Vector3(1.0, 0.0, 0.0))
        if perp.lengthSquared() < square_zero:
            perp = self.crossProduct(Vector3(0.0, 1.0, 0.0))
        perp.normalize()
        return perp

    @staticmethod
    def add(left, right):
        result = Vector3()
        result.m_x = left.m_x + right.m_x
        result.m_y = left.m_y + right.m_y
        result.m_z = left.m_z + right.m_z
        return result

    @staticmethod
    def subtract(left, right):
        result = Vector3()
        result.m_x = left.m_x - right.m_x
        result.m_y = left.m_y - right.m_y
        result.m_z = left.m_z - right.m_z
        return result

    @staticmethod
    def multiply(left, right):
        result = Vector3()
        result.m_x = left * right.m_x
        result.m_y = left * right.m_y
        result.m_z = left * right.m_z
        return result

    def __getitem__(self, i):
        return [self.m_x, self.m_y, self.m_z][i]

    def __eq__(self, vec3):
        return self.m_x == vec3.m_x and self.m_y == vec3.m_y and self.m_z == vec3.m_z

    def __ne__(self, vec3):
        return self.m_x != vec3.m_x or self.m_y != vec3.m_y or self.m_z != vec3.m_z

    def __add__(self, vec3):
        return Vector3.add(self, vec3)

    def __sub__(self, vec3):
        return Vector3.subtract(self, vec3)

    def __mul__(self, factor):
        return Vector3.multiply(factor, self)

    def __truediv__(self, divisor):
        return Vector3(self.x / divisor, self.y / divisor, self.z / divisor)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y}, {self.z})"

    def toVector2(self):
        return Vector2(self.m_x, self.m_y)

    def toVector4(self):
        return Vector4(self.m_x, self.m_y, self.m_z, 1.0)

class Vector4:
    def __init__(self, *args): 
        if len(args) == 4:
            self.m_x = args[0]
            self.m_y = args[1]
            self.m_z = args[2]
            self.m_w = args[3]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.m_x = args[0][0]
            self.m_y = args[0][1]
            self.m_z = args[0][2]
            self.m_w = args[0][3]
        elif len(args) == 1 and isinstance(args[0], Vector3):
            self.m_x = args[0].m_x
            self.m_y = args[0].m_y
            self.m_z = args[0].m_z
            self.m_w = args[0].m_w

    @property
    def x(self):
        return self.m_x
    @x.setter
    def x(self, v):
        self.m_x = v

    @property
    def y(self):
        return self.m_y
    @y.setter
    def y(self, v):
        self.m_y = v

    @property
    def z(self):
        return self.m_z
    @z.setter
    def z(self, v):
        self.m_z = v

    @property
    def w(self):
        return self.m_w
    @w.setter
    def w(self, v):
        self.m_w = v

    def setX(self, x):
        self.m_x = x

    def setY(self, y):
        self.m_y = y

    def setZ(self, z):
        self.m_z = z

    def setW(self, w):
        self.m_w = w

    def inverse(self):
        self.m_x = 1.0 / self.m_x
        self.m_y = 1.0 / self.m_y
        self.m_z = 1.0 / self.m_z
        self.m_w = 1.0 / self.m_w

    def normalize(self):
        len = self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z + self.m_w * self.m_w
        len = len ** 0.5
        if len > 0.0:
            inverse = 1.0 / len
            self.m_x *= inverse
            self.m_y *= inverse
            self.m_z *= inverse
            self.m_w *= inverse

    def inversed(self):
        v = Vector4(self)
        v.inverse()
        return v

    def normalized(self):
        v = Vector4(self)
        v.normalize()
        return v

    def length(self):
        return (self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z + self.m_w * self.m_w) ** 0.5

    def lengthSquared(self):
        return self.m_x * self.m_x + self.m_y * self.m_y + self.m_z * self.m_z + self.m_w * self.m_w

    @staticmethod
    def dot(v1, v2):
        return v1.m_x * v2.m_x + v1.m_y * v2.m_y + v1.m_z * v2.m_z + v1.m_w * v2.m_w

    @staticmethod
    def add(left, right):
        result = Vector4()
        result.m_x = left.m_x + right.m_x
        result.m_y = left.m_y + right.m_y
        result.m_z = left.m_z + right.m_z
        result.m_w = left.m_w + right.m_w
        return result

    @staticmethod
    def subtract(left, right):
        result = Vector4()
        result.m_x = left.m_x - right.m_x
        result.m_y = left.m_y - right.m_y
        result.m_z = left.m_z - right.m_z
        result.m_w = left.m_w - right.m_w
        return result

    @staticmethod
    def multiply(left, right):
        result = Vector4()
        result.m_x = left * right.m_x
        result.m_y = left * right.m_y
        result.m_z = left * right.m_z
        result.m_w = left * right.m_w
        return result

    def __getitem__(self, i):
        return [self.m_x, self.m_y, self.m_z, self.m_w][i]

    def __eq__(self, vec4):
        return self.m_x == vec4.m_x and self.m_y == vec4.m_y and self.m_z == vec4.m_z and self.m_w == vec4.m_w

    def __ne__(self, vec4):
        return self.m_x != vec4.m_x or self.m_y != vec4.m_y or self.m_z != vec4.m_z or self.m_w != vec4.m_w

    def __add__(self, vec4):
        return Vector4.add(self, vec4)

    def __sub__(self, vec4):
        return Vector4.subtract(self, vec4)

    def __mul__(self, factor):
        return Vector4.multiply(factor, self)

    def __truediv__(self, divisor):
        return Vector4(self.x / divisor, self.y / divisor, self.z / divisor, self.w / divisor)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y}, {self.z}, {self.w})"

    def toVector2(self):
        return Vector2(self.m_x, self.m_y)

    def toVector3(self):
        return Vector3(self.m_x, self.m_y, self.m_z)

class Vector2D:
    def __init__(self, *args): 
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.x = args[0][0]
            self.y = args[0][1]
        elif len(args) == 1 and isinstance(args[0], Vector2D):
            self.x = args[0].x
            self.y = args[0].y
        else:
            self.x = 0.0
            self.y = 0.0
    
    def Normalize(self):
        magnitude = self.Magnitude()
        return self / magnitude
    
    def Normalized(self):
        res = Vector2D(self.x, self.y)
        return res.Normalize()
    
    def Dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def Magnitude(self):
        return (self.Dot(self)) ** 0.5
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not (self == other)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self
    
    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self
    
    def __getitem__(self, i):
        if i > 1:
            raise IndexError("Index to vec2 is out of range")
        return [self.x, self.y][i]
    
    def __setitem__(self, i, value):
        if i > 1:
            raise IndexError("Index to vec2 is out of range")
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value

class Vector3D:
    def __init__(self, *args): 
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        elif len(args) == 1 and isinstance(args[0], Vector3D):
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        else:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0

    def Normalize(self):
        mag = self.Magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def Normalized(self):
        res = Vector3D(self.x, self.y, self.z)
        return res.Normalize()

    def Cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def Dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def Magnitude(self):
        return (self.Dot(self))**0.5

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self

    def __getitem__(self, i):
        if i > 2:
            raise ValueError("Index to vec3 is out of range")
        return [self.x, self.y, self.z][i]

    def __setitem__(self, i, value):
        if i > 2:
            raise ValueError("Index to vec3 is out of range")
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        elif i == 2:
            self.z = value

class Vector4D:
    def __init__(self, *args): 
        if len(args) == 4:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.w = args[3]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
            self.w = args[0][3]
        elif len(args) == 1 and isinstance(args[0], Vector4D):
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
            self.w = args[0].w
        else:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.w = 0.0

    def Normalize(self):
        magnitude = self.Magnitude()
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        self.w /= magnitude
        return self

    def Normalized(self):
        res = Vector4D(self.x, self.y, self.z, self.w)
        return res.Normalize()

    def Dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)

    def Magnitude(self):
        return (self.Dot(self)) ** 0.5

    def __add__(self, other):
        return Vector4D(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Vector4D(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, scalar):
        return Vector4D(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __truediv__(self, scalar):
        return Vector4D(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w)

    def __ne__(self, other):
        return not (self == other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.w -= other.w
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.w *= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        self.w /= scalar
        return self

    def __getitem__(self, i):
        if i > 3:
            raise IndexError("Index to vec4 is out of range")
        return [self.x, self.y, self.z, self.w][i]

    def __setitem__(self, i, value):
        if i > 3:
            raise ValueError("Index to vec4 is out of range")
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        elif i == 2:
            self.z = value
        elif i == 3:
            self.w = value

class Matrix4x4:
    def __init__(self):
        self.right = Vector4D()
        self.up = Vector4D()
        self.forward = Vector4D()
        self.position = Vector4D()

    def Translate(self, translation):
        self.position = self.right * translation.x + self.up * translation.y + self.forward * translation.z + self.position
        return self

    def Rotate(self, axis, angle):
        angle_cos = math.cos(angle)
        angle_sin = math.sin(angle)
        axis_magnified = axis * (1.0 - angle_cos)

        self.right = self.right * (axis_magnified.x * axis.x + angle_cos) + self.up * (axis_magnified.x * axis.y + angle_sin * axis.z) + self.forward * (axis_magnified.x * axis.z - angle_sin * axis.y)
        self.up = self.right * (axis_magnified.y * axis.x - angle_sin * axis.z) + self.up * (axis_magnified.y * axis.y + angle_cos) + self.forward * (axis_magnified.y * axis.z + angle_sin * axis.x)
        self.forward = self.right * (axis_magnified.z * axis.x + angle_sin * axis.y) + self.up * (axis_magnified.z * axis.y - angle_sin * axis.x) + self.forward * (axis_magnified.z * axis.z + angle_cos)

        return self

    def Scale(self, scale):
        self.right *= scale.x
        self.up *= scale.y
        self.forward *= scale.z

        return self

    def SetIdentity(self):
        self.__init__() # Set all vectors to zero
        for i in range(0, 16, 5):
            self[i] = 1.0

        return self

    def SetPerspective(self, fov, aspect, nearclip, farclip):
        fov_half = math.tan(fov * 0.5)
        self.__init__() # Set all vectors to zero
        self.right.x = 1.0 / (aspect * fov_half)
        self.up.y = 1.0 / fov_half
        self.forward.z = farclip / (farclip - nearclip)
        self.forward.w = 1.0
        self.position.z = -(farclip * nearclip) / (farclip - nearclip)

        return self

    def SetOrthographic(self, l, r, b, t):
        self.__init__() # Set all vectors to zero
        self.right.x = 2.0 / (r - l)
        self.up.y = 2.0 / (t - b)
        self.forward.z = -1.0
        self.position.x = -(r + l) / (r - l)
        self.position.y = -(t + b) / (t - b)

        return self

    def SetLookAt(self, eye, target, world_up):
        eye_to_target = (target - eye).Normalized()
        outward = world_up.Cross(eye_to_target).Normalized()
        upward = eye_to_target.Cross(outward)

        self.right = Vector4D(outward.x, outward.y, outward.z, -outward.Dot(eye))
        self.up = Vector4D(upward.x, upward.y, upward.z, -upward.Dot(eye))
        self.forward = Vector4D(eye_to_target.x, eye_to_target.y, eye_to_target.z, -eye_to_target.Dot(eye))
        self.position = Vector4D(eye.x, eye.y, eye.z, 1.0)

        return self

    def Transpose(self):
        for row in range(4):
            for col in range(4):
                self[row + col * 4] = self[col + row * 4]

        return self

    def Invert(self):
        self.right.x    =  self[5] * self[10] * self[15] - self[5] * self[11] * self[14] - self[9] * self[6] * self[15] + self[9] * self[7] * self[14] + self[13] * self[6] * self[11] - self[13] * self[7] * self[10]
        self.right.y    = -self[1] * self[10] * self[15] + self[1] * self[11] * self[14] + self[9] * self[2] * self[15] - self[9] * self[3] * self[14] - self[13] * self[2] * self[11] + self[13] * self[3] * self[10]
        self.right.z    =  self[1] * self[6]  * self[15] - self[1] * self[7]  * self[14] - self[5] * self[2] * self[15] + self[5] * self[3] * self[14] + self[13] * self[2] * self[7]  - self[13] * self[3] * self[6]
        self.right.w    = -self[1] * self[6]  * self[11] + self[1] * self[7]  * self[10] + self[5] * self[2] * self[11] - self[5] * self[3] * self[10] - self[9]  * self[2] * self[7]  + self[9]  * self[3] * self[6]
        self.up.x       = -self[4] * self[10] * self[15] + self[4] * self[11] * self[14] + self[8] * self[6] * self[15] - self[8] * self[7] * self[14] - self[12] * self[6] * self[11] + self[12] * self[7] * self[10]
        self.up.y       =  self[0] * self[10] * self[15] - self[0] * self[11] * self[14] - self[8] * self[2] * self[15] + self[8] * self[3] * self[14] + self[12] * self[2] * self[11] - self[12] * self[3] * self[10]
        self.up.z       = -self[0] * self[6]  * self[15] + self[0] * self[7]  * self[14] + self[4] * self[2] * self[15] - self[4] * self[3] * self[14] - self[12] * self[2] * self[7]  + self[12] * self[3] * self[6]
        self.up.w       =  self[0] * self[6]  * self[11] - self[0] * self[7]  * self[10] - self[4] * self[2] * self[11] + self[4] * self[3] * self[10] + self[8]  * self[2] * self[7]  - self[8]  * self[3] * self[6]
        self.forward.x  =  self[4] * self[9]  * self[15] - self[4] * self[11] * self[13] - self[8] * self[5] * self[15] + self[8] * self[7] * self[13] + self[12] * self[5] * self[11] - self[12] * self[7] * self[9]
        self.forward.y  = -self[0] * self[9]  * self[15] + self[0] * self[11] * self[13] + self[8] * self[1] * self[15] - self[8] * self[3] * self[13] - self[12] * self[1] * self[11] + self[12] * self[3] * self[9]
        self.forward.z  =  self[0] * self[5]  * self[15] - self[0] * self[7]  * self[13] - self[4] * self[1] * self[15] + self[4] * self[3] * self[13] + self[12] * self[1] * self[7]  - self[12] * self[3] * self[5]
        self.forward.w  = -self[0] * self[5]  * self[11] + self[0] * self[7]  * self[9]  + self[4] * self[1] * self[11] - self[4] * self[3] * self[9]  - self[8]  * self[1] * self[7]  + self[8]  * self[3] * self[5]
        self.position.x = -self[4] * self[9]  * self[14] + self[4] * self[10] * self[13] + self[8] * self[5] * self[14] - self[8] * self[6] * self[13] - self[12] * self[5] * self[10] + self[12] * self[6] * self[9]
        self.position.y =  self[0] * self[9]  * self[14] - self[0] * self[10] * self[13] - self[8] * self[1] * self[14] + self[8] * self[2] * self[13] + self[12] * self[1] * self[10] - self[12] * self[2] * self[9]
        self.position.z = -self[0] * self[5]  * self[14] + self[0] * self[6]  * self[13] + self[4] * self[1] * self[14] - self[4] * self[2] * self[13] - self[12] * self[1] * self[6]  + self[12] * self[2] * self[5]
        self.position.w =  self[0] * self[5]  * self[10] - self[0] * self[6]  * self[9]  - self[4] * self[1] * self[10] + self[4] * self[2] * self[9]  + self[8]  * self[1] * self[6]  - self[8]  * self[2] * self[5]
        
        determinant = self[0] * self.right[0] + self[1] * self.up[0] + self[2] * self.forward[0] + self[3] * self.position[0]
        determinant = 1.0 / determinant
        self.right    *= determinant
        self.up       *= determinant
        self.forward  *= determinant
        self.position *= determinant

        return self

    def Transposed(self):
        res = Matrix4x4()
        return res.Transpose()

    def Inverted(self):
        res = Matrix4x4()
        return res.Invert()

    def __mul__(self, other):
        res = Matrix4x4()
        return res.__imul__(other)

    def __imul__(self, other):
        self.right = self.right * other.right.x + self.up * other.right.y + self.forward * other.right.z + self.position * other.right.w
        self.up = self.right * other.up.x + self.up * other.up.y + self.forward * other.up.z + self.position * other.up.w
        self.forward = self.right * other.forward.x + self.up * other.forward.y + self.forward * other.forward.z + self.position * other.forward.w
        self.position = self.right * other.position.x + self.up * other.position.y + self.forward * other.position.z + self.position * other.position.w

        return self

    def __getitem__(self, i):
        return [self.right.x, self.right.y, self.right.z, self.right.w,
                self.up.x, self.up.y, self.up.z, self.up.w,
                self.forward.x, self.forward.y, self.forward.z, self.forward.w,
                self.position.x, self.position.y, self.position.z, self.position.w][i]

class AABB2D:
    def __init__(self, *args):
        if len(args) == 2:
            self.min = Vector2D(args[0])
            self.max = Vector2D(args[1])
        else:
            self.min = Vector2D()
            self.max = Vector2D()

    def SetMin(self, _min: Vector2D):
        self.min = _min

        return self

    def SetMax(self, _max: Vector2D):
        self.max = _max

        return self

    def SetMinMax(self, _min: Vector2D, _max: Vector2D):
        self.min = _min
        self.max = _max

        return self

    def Contains(self, point):
        if isinstance(point, Vector2D):
            return not (point.x < self.min.x or point.y < self.min.y or
                        point.x > self.max.x or point.y > self.max.y)
        elif isinstance(point, AABB2D):
            return (self.Contains(point.min) and self.Contains(point.max))
        else:
            raise("Unknown type (AABB2D.Contains)")

class AABB3D:
    def __init__(self, *args):
        if len(args) == 2:
            self.min = Vector3D(args[0])
            self.max = Vector3D(args[1])
        else:
            self.min = Vector3D()
            self.max = Vector3D()

    def SetMin(self, _min: Vector3D):
        self.min = _min

        return self

    def SetMax(self, _max: Vector3D):
        self.max = _max

        return self

    def SetMinMax(self, _min: Vector3D, _max: Vector3D):
        self.min = _min
        self.max = _max

        return self

    def Contains(self, point):
        if isinstance(point, Vector3D):
            return not (point.x < self.min.x or point.y < self.min.y or point.z < self.min.z or
                        point.x > self.max.x or point.y > self.max.y or point.z > self.max.z)
        elif isinstance(point, AABB3D):
            return (self.Contains(point.min) and self.Contains(point.max))
        else:
            raise("Unknown type (AABB3D.Contains)")

class Quaternion:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=10):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def SetIdentity(self):
        self.x = self.y = self.z = 0.0
        self.w = 1.0
        return self
    
    def SetEuler(self, euler):
        rad = math.radians(euler.x * 0.5)
        rollx = math.cos(rad)
        rolly = math.sin(rad)
        
        rad = math.radians(euler.y * 0.5)
        pitchx = math.cos(rad)
        pitchy = math.sin(rad)
        
        rad = math.radians(euler.z * 0.5)
        yawx = math.cos(rad)
        yawy = math.sin(rad)
        
        self.x = rolly * (pitchx * yawx) - rollx * (pitchy * yawy)
        self.y = rollx * (pitchy * yawx) + rolly * (pitchx * yawy)
        self.z = rollx * (pitchx * yawy) - rolly * (pitchy * yawx)
        self.w = rollx * (pitchx * yawx) + rolly * (pitchy * yawy)
        
        return self
    
    def SetMatrix4x4(self, mat):
        trace = mat[0] + mat[5] + mat[10]
        
        if trace > 0.0:
            scale = math.sqrt(1.0 + trace)
            self.w = scale * 0.5
            
            scale = 0.5 / scale
            self.x = (mat[6] - mat[9]) * scale
            self.y = (mat[8] - mat[2]) * scale
            self.z = (mat[1] - mat[4]) * scale
        else:
            if mat[0] > mat[5] and mat[0] > mat[10]:
                scale = math.sqrt(1.0 + mat[0] - mat[5] - mat[10])
                self.x = scale * 0.5
                
                scale = 0.5 / scale
                self.y = (mat[4] + mat[1]) * scale
                self.z = (mat[8] + mat[2]) * scale
                self.w = (mat[6] - mat[9]) * scale
            elif mat[5] > mat[10]:
                scale = math.sqrt(1.0 + mat[5] - mat[0] - mat[10])
                self.y = scale * 0.5
                
                scale = 0.5 / scale
                self.x = (mat[4] + mat[1]) * scale
                self.z = (mat[9] + mat[6]) * scale
                self.w = (mat[8] - mat[2]) * scale
            else:
                scale = math.sqrt(1.0 + mat[10] - mat[0] - mat[5])
                self.z = scale * 0.5
                
                scale = 0.5 / scale
                self.x = (mat[8] + mat[2]) * scale
                self.y = (mat[9] + mat[6]) * scale
                self.w = (mat[1] - mat[4]) * scale
        
        return self
    
    def normalize(self):
        m = self.__abs__()
        if m == 0:
            return self
        return Quaternion(self[0] / m, self[1] / m, self[2] / m, self[3] / m)
    
    def Invert(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self
    
    def Dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def ToMatrix4x4(self):
        res = [0.0] * 16
        res[0] = 1.0 - 2.0 * self.y * self.y - 2.0 * self.z * self.z
        res[1] = 2.0 * self.x * self.y + 2.0 * self.z * self.w
        res[2] = 2.0 * self.x * self.z - 2.0 * self.y * self.w
        res[4] = 2.0 * self.x * self.y - 2.0 * self.z * self.w
        res[5] = 1.0 - 2.0 * self.x * self.x - 2.0 * self.z * self.z
        res[6] = 2.0 * self.z * self.y + 2.0 * self.x * self.w
        res[8] = 2.0 * self.x * self.z + 2.0 * self.y * self.w
        res[9] = 2.0 * self.z * self.y - 2.0 * self.x * self.w
        res[10] = 1.0 - 2.0 * self.x * self.x - 2.0 * self.y * self.y
        res[15] = 1.0
        
        return res

    def ToEuler(self):
        res = Vector3D()
        
        res.x = math.atan2(2.0 * (self.w * self.x + self.y * self.z),
                           1.0 - 2.0 * (self.y * self.y + self.x * self.x))
        res.z = math.atan2(2.0 * (self.w * self.z + self.y * self.x),
                           1.0 - 2.0 * (self.y * self.y + self.z * self.z))
        pitchy = 2.0 * (self.w * self.y - self.z * self.x)
        if abs(pitchy) >= 1.0:
            res.y = math.copysign(math.pi * 0.5, pitchy)
        else:
            res.y = math.asin(pitchy)
        
        return res

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        return self
    
    def __imul__(self, other):
        if isinstance(other, Quaternion):
            self.x = self.x * other.w + self.w * other.x + self.z * other.y - self.y * other.z
            self.y = self.y * other.w + self.w * other.y + self.x * other.z - self.z * other.x
            self.z = self.z * other.w + self.w * other.z + self.y * other.x - self.x * other.y
            self.w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        else:
            self.x *= other
            self.y *= other
            self.z *= other
            self.w *= other
        return self
    
    def __mul__(self, other):
        if isinstance(other, Quaternion):
            res = Quaternion(self.x, self.y, self.z, self.w)
            return res.__imul__(other)
        else:
            return Quaternion(self.x * other, self.y * other, self.z * other, self.w * other)

    def __rmul__(self, other):
        if isinstance(other, Quaternion):
            res = Quaternion(self.x, self.y, self.z, self.w)
            return res.__imul__(other)
        else:
            return Quaternion(self.x * other, self.y * other, self.z * other, self.w * other)

    def __abs__(self) -> float:
        return math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)
