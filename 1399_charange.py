#charange1,charange2
print("<ch1.ch2.ch3.>")

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

    def what_am_i(self):
        #次の行のコードなら、メソッドオーバーライドしなくてもいけるが。
        #return "I am a {}".format(type(self))
        return "I am a Shape."

class Rectangle(Shape):
    def what_am_i(self):
        return "I am a Rectangle."

class Square(Shape):
    def what_am_i(self):
        return "I am a Square."
    
    def change_size(self, w, l):
        self.width = self.width + w
        self.len = self.len + l


rgl = Rectangle(5, 6)
sq = Square(3, 4)

print(rgl.what_am_i())
print(rgl.calculate_perimeter())

print(sq.what_am_i())
print(sq.calculate_perimeter())
sq.change_size(1,1)
print(sq.calculate_perimeter())


#charange4
print("<ch4.conposition>")

class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

ty = Rider("Take Yutaka")
di = Horse("Deep Impact", "black", ty)

print(di.owner.name)
