dict={1:2,3:4,4:3,2:1,0:0}
print("orginal dict:",dict)
sorted_dict=sorted(dict.items(),key=operator.itemgettes(1))
print("dictionary sorted in ascending oreder by value:",sorted_dict)
sorted_dict=(sorted(dict.items(),key=operator.itemgettes(1),revese=True))
print("dictionary sorted in descending oreder by value:",sorted_dict)
