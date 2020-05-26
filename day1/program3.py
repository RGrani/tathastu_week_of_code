'''swap 2 variables without using third variable'''
a = int(input("Enter first no :"))
b = int(input("Enter second no :"))
a = a+b
b = a-b
a = a-b
print("\n AFTER SWAPPING :-\n")
print("                   first no  = ",a)
print("                   second no = ",b)
