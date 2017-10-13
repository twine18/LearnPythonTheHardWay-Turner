#Euler Problem #6: Sum Square Difference

#Creates a list named 'digits'
digits = []

#Line 4 creates a for-loop for i in range of 1-100
#Line 5 appends or changes the list by squaring all of the numbers in the list
for i in range (1, 101):
    digits.append(i ** 2)

#Line 9 finds the sum of all the numbers in the list 'digits' and prints it
print sum(digits)

#Line 12 creates a new list named 'newdigits'
newdigits = []

#Line 15 creates a for-loop for i in range of 1-100
#Line 16 adds those numbers int the  list 'new digits'
for i in range (1, 101):
    newdigits.append(i)

#Line 20 takes the sum of all the numbers in the list 'newdigits'
# and then squares it
print (sum(newdigits) ** 2)

#Line 24 subtracts the total of the list 'newdigits' from the total of 'digits'
print((sum(newdigits) ** 2) - (sum(digits)))

#This program will Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
