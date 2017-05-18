import random
tup1 = ('math', 'computer', 'games', 'class');#tuples use () and the elements canot be chainged
print "tup1:", tup1[2]
list2 = [a, 2, 3, 4, 5 ];#lists use [] and the elements can be chainged
print "list2:", list2[3]
list2 += tup1
print list2
print "list2 sliced:", list2[3:8]
list3 = list2[3:8]
print "list3:", list3[3:8]
print "random: ",random.choice(list2)