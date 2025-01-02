principal = 1000
annual_rate = 0.07
number_of_years = int(input('Enter number of years: ')) 

amount_deposit = int(1000*(1 + 0.07)** number_of_years)
print('The amount deposited in ten years is :', amount_deposit) 