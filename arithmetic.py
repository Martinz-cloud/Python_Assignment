number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))
minimum = number1
maximum = number1
sum = number1 + number2 + number3 
print('The sum of numbers is : ',sum)

average = sum / 3
print('The average of numbers is : ', average)

product = number1 * number2 * number3
print('The product of numbers is : ', product)


if number2 < minimum:
	print(number2,'is the smallest')
if number3 < minimum:
	print(number3,'is the smallest')

if number2 > maximum:
	print(number2,'is the largest')
if number3 > maximum:
	print(number3,'is the largest')