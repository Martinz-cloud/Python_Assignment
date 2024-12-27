print('Enter the percentage of successful delivery')
percentage = int(input())

collection_rate1 = 160
collection_rate2 = 200
collection_rate3 = 250
collection_rate4 = 500
base_salary = 5000
total_payment = 0


if percentage < 50 :
	total_payment = percentage * collection_rate1 + base_salary 
elif percentage >= 50 and percentage <= 59 :
 	total_payment = percentage * collection_rate2 + base_salary
elif percentage >= 60 and percentage <= 69 :
	total_payment = percentage * collection_rate3 + base_salary
elif percentage >= 70 :
	total_payment = percentage * collection_rate4 + base_salary

print('RIDERS PAYMENT', total_payment)