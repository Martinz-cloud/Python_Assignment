pizza_type = {'sapa size','small money','big boys', 'odogwu'}

number_of_slices = {4, 6, 8, 12}

price_per_box = {2500, 2900, 4000, 5200}

print('ENTER NUMBER OF SLICES')
slices = int(input())

print('''

'PIZZA PAYMENT :\n' +

 '0 = Sapa size\n' +
 '1 = Small money\n' +
 '2 = big boys\n'+
 '3 = odogwu\n' +

''')
pizzatypeindex = int(input())

if pizzatypeindex < 0 or pizzatypeindex >= len(pizza_type) :
	print('invalid selection')
	

	slicesperboxchosen = int(number_of_slices[pizzatypeindex])
	priceperboxchosen = int(price_per_box[pizzatypeindex])
	boxes_needed = int(slices / slicesperboxchosen)

if slices % slicesperboxchosen != 0 :
	boxes_needed += 1
 
totalSlices = boxes_needed * slicesperboxchosen
leftOverSlices = totalSlices - slices
totalPrice = boxes_needed * priceperboxchosen

print('Number of Boxes of pizza to buy = ' + boxesNeeded + 'boxes')
print('Number left over slices after serving = ' + leftOverSlices + 'slices')
print("price = " + totalPrice)