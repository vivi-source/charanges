#charange1
print("<ch1.クラス変数追加>")

class Square:
    square_list = []
    
    def __init__(self,l):
        self.len = l
        self.square_list.append(self)
    
    #回答では、普通にフォーマット使っていた。そんなもんか。
    def __repr__(self): #__repr__をオーバーライド
        s = str(self.len)
        by4 = [s, s, s, s]
        return " by ".join(by4)

    def is_equal(self, other):
        return self is other     #なるほど。is式そのものを戻り値でいいよな
#        if self is other:
#            return True
#        else:
#            return False

s1 = Square(4)
s2 = Square(5)
s3 = Square(4)
s4 =s1

print(s1)
print(s2)
print(s3)
print(Square.square_list)       #__repr__メソッドをオーバーライドすると、
                                #全体表示もオーバーライドされちゃうんだ。
print(Square.is_equal(s1, s4))  #同じオブジェクト指してるのでT
print(Square.is_equal(s1, s2))  #別オブジェクトなのでFalse
print(Square.is_equal(s1, s3))  #値が同じでも別オブジェクトはFalse
