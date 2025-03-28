square = lambda x : x*x
cube = lambda x : x*x*x

print(square(5),"\t",cube(5))

def func(fnx, value) :
    return 100 + fnx(value)

print(func(cube,3))