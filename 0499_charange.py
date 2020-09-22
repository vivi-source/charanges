#charange1
print("<charange1>")

def exp():
    """
    Returns x ** x
    :no param
    :input:int
    :return exponents of x
    """
    x = input("type a number:")
    x = int(x)
    return x ** x

print(exp())


#charange2
print("<charange2>")

def str(s):
    """
    Prints(s)
    :param s:string
    :no return
    """
    print(s)

str("Hello, World!")


#charange3
print("<charange3>")

def num(v, w, x, y = 0, z = 0):
    """
    省略
    """
    v = int(v)
    w = int(w)
    x = int(x)
    y = int(y)
    z = int(z)
    return v * 10000 + w * 1000 + x * 100 + y * 10 + z

print(num(1,2,3))


#charange4
print("<charange4>")

def div(x):
    """
    Returns x // 2
    :param x: int
    :return 商 of x divided by 2
    """
    x = int( x )
    return x // 2

def mlt(x):
    """
    Returns x * 4
    :param x: int
    :return x murtiplicated 4
    """
    x = int( x )
    return x * 4

d = div(input("type a number:"))
m = mlt( d )
print( m )


#charange5
print("<charange5>")

def flt( x ):
    """
    Returns float(x)
    :param x: int
    :return floated x
    :if param x is no number,print "Invalid input"
    """
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

x =  flt(input("type a number:"))
print( x );
