def addstr(str):
    l=len(str)
    if l>0:
        if str[-3:]=="ing":
            str=str+"ly"
        else:
            str=str+"ing"
    print(str)
str=(input("Enter the string"))
addstr(str)