x = 10
y = 5
print("---ARITHMETIC OPERATORS---")
print(f"addition: {x+y}")
print("subtraction:", x-y)
print("multiplication:", x*y)
print("division:",x/y)
print("floor division:",x//y)
print("modulus:", x%y)
print("exponential:",x**y)
print("")
print("")

print("---ASSIGNMENT OPERATORS---")
x+=5
print("x+=5:",x)
x-=y
print("x-=y:",x)
y*=x
print("y*=x:",y)
x/=2
print("x/=2:",x)
y//=3
print("y//=3:",y)
x%=3
print("x%=2:",x)
y**=1
print("y**=1:",y)
print("")
print("")

print("---COMPARISON OPERATORS---")
print("x==y:",x==y)
print("y<x:",y<x)
print("y>x:",y>x)
print("x>=y:",x>=y)
print("x<=y:",x<=y)
print("x!=y:",x!=y)
print("")
print("")

print("---LOGICAL OPERATORS---")
print(x<y and y>x)
print(x>2 or y<9)
print(not(x>6 and y>10))
print("")
print("")

print("---IDENTITY OPERATORS---")
print(x is y)
print(x is not y)
print("")
print("")


data=[2,4,6,8,10]
print("---MEMBERSHIP OPERATORS---")
print(x in data)
print (y in data)
print(x not in data)
print(y not in data)
