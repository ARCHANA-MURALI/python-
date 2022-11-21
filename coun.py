def word_count(str):
    count=dict()
    words=str.split()
    for v in words:
        if  v in count:
            count+=1
        else:
          count[v]=1
          print(count)
d=input("Enter the string:")
word_count(d)
