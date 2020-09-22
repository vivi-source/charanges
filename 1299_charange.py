#charange1
print("<ch1.class Apple>")

class Apple:
    """
    color：色
    weight：重さ
    spiece：品種
    locate：産地
    """
    def __init__(self, c, w, s, l):
        self.color = c
        self.weight = w
        self.spiece = s
        self.locate = l

ap1 = Apple("red", 100, "ふじ", "青森")
ap2 = Apple("pink", 200, "ゴールデン", "余市")

print(ap1.color)
print(ap1.weight)
print(ap1.spiece)
print(ap1.locate)
print(ap2.color)
print(ap2.weight)
print(ap2.spiece)
print(ap2.locate)


#charange2
import math
print("\n<ch2.class Circle>")

class Circle:
    def __init__(self, r):
        self.range = int(r)
        self.outline = int(r) * math.pi
    
    def area(self):
        self.area = self.range * self.outline
        return self.area

cl1 = Circle(3)
cl2 = Circle(5)

print(cl1.outline)
print(cl1.area())
print(cl2.outline)
print(cl2.area())


#charange3
print("\n<ch3.class Triangle>")

class Triangle:
    def __init__(self, l, h):
        self.len = l
        self.hight = h

    def area(self):
        self.area = self.len * self.hight / 2
        return self.area

tr1 = Triangle(3,5)
tr2 = Triangle(4,10)

print(tr1.len)
print(tr1.hight)
print(tr1.area())
print(tr2.len)
print(tr2.hight)
print(tr2.area())


#charange4
#　さすがに心配で答え見たら、意外とまんまだった（笑）
print("\n<ch4.class Hexagon>")

class Hexagon:
    def __init__(self, a,b,c,d,e,f):
        self.len1 = a
        self.len2 = b
        self.len3 = c
        self.len4 = d
        self.len5 = e
        self.len6 = f
    
    def calculate_perimeter(self):
        self.perimeter = self.len1 + self.len2 + self.len3 +self.len4 + self.len5 + self.len6
        return self.perimeter

hx = Hexagon(1,2,3,4,5,6)
print(hx.calculate_perimeter())
