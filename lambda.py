a=int(input("enter the side of the square :"))
area=lambda b:b*b
print("area of square",area(a))

a=int(input("enter the length of the rectangle "))
b=int(input("enter the breadth of the rectangle "))
area=lambda l,b:l*b
print("area of the rectangle is",area(a,b))

a=int(input("enter the height of the triangle "))
b=int(input("enter the breadth of the triangle "))
area=lambda h,b:h*b
print("area of triangle",area(a,b))
