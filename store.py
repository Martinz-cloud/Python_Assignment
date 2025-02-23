 

def display_menu():
	print ("Welcome To Semicolon Expense Tracker App")
	print ("-----------------------------------------")
	print ("""
	1. Add an expense
	2. View all expenses
	3. Calculate total expenses
	4. Exit
		""") 


def main_pass():
	expenses = []
	while True:
	  display_menu() 
	  option = input("choose an option (1-4): ")
	  if option == "1":
	     date = input("Enter date (YYYY-MM-DD): ")
	     description = input("Enter description: ")
	     amount = input("Enter amount: ")
	     print(add_expense(expenses, date, description, amount))
	  elif option == "2":
	     print(view_expenses(expenses))
	  elif option == "3":
	     print(calculate_total_expenses(expenses))
	  elif option == "4":
	     print("***Exiting the Expense Tracker...... Bye***")
	     break
	  else:
	     print("<<<Invalid Input.>>>")	
def add_expense(expenses, date, description, amount):
	try:
		amount = float(amount)
		date = str(date)
		expenses.append([date, description, amount])
		return "Expense added"
	except ValueError:
		return "<<<invalid amount and date entered .>>> please enter a number."


def view_expenses(expenses):
	if not expenses:
	     return "no expenses input"
	output = "\nExpenses:\n"
	output += f"{'date':<12}{'description':<20}{'amount':<10}\n"
	output += "-" * 50 + "\n"
	for expense in expenses:
		output += f"{expense[0]:<12}{expense[1]:<20}{expense[2]:<10.3f}\n"
	return output
def calculate_total_expenses(expenses):
	if not expenses:
		return "Your total expenses is 0.000 "
	total = sum(expense[2] for expense in expenses)
	return f"Total expenses: {total:.3f}"
		
if __name__ == "__main__":
	main_pass()




