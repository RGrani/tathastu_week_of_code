# occurrances of an element in tuple
 
no = int(input("Enter tuple size:"))
tupl=[]
print("\nEnter elements in your tuple:")
for i in range(no):
    elem = input()
    tupl.append(elem)

tupl=tuple(tupl)
print("The given tuple is:",tupl)

var = input("Enter element to be counted:")

count = len([i for i in tupl if i==var])
print("\nThe element occurs {} times in the tuple".format(count))
