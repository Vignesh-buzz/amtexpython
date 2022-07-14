#passing arguments in functions
"""def ninu(a,b):
    c=a+b
    print(c)
ninu(10,20)"""

"""#using return function
def trans():
    return "hello world"
print(trans().upper())"""

#args and kwargs
#same like dctionary concepts
# to get a multiple dictionary we are going to dictionary
def students_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses=["maths","art"]
info={"name":"vicky","age":22}
students_info(*courses,**info)

