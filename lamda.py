area_s=lambda a:a*a
area_rect=lambda l,b,h:l*b*h
area_traingle=lambda s,c:0.5*s*c

a=int(input('Enter the side of square'))
print('Area of square',area_s(a))
l=int(input('Enter the length of rectangle'))
b=int(input('Enter the bredth of rectangle'))
h=int(input('Enter the height of rectangle'))
print('Area of Rectangle',area_rect(l,b,h))
s=int(input('Enter the base of triangle'))
c=int(input('Enter the height of triangle'))
print('Area of triangle',area_traingle(s,c))



