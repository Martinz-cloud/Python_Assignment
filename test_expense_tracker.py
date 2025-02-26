import unittest
import expense_tracker

class TestExpenseTracker(unittest.TestCase):
	def test_that_match_case_funtion_exists(self):
		option = "1","2","3","4"
		expense_tracker.main_pass()
	
	def test_that_match_case_funtion_exist(self):
		option = "1","2","3","4"
		result = expense_tracker.main_pass()
		expected = "1","2","3","4"
		self.assertEqual(result, expected)

	def test_that_appending_function_exist(self):
		expenses = []
		date = "2020-10-20"
		description = "groceries"
		amount = 500.00
		expenses = ([date], [description], [amount])
		expense_tracker.add_expense(expenses, date, description, amount)
		
	
	
	def test_that_appending_function_exists(self):
		expenses = []
		amount = 500.00
		date = "2020-10-20"
		description = "groceries"
		expenses.append([date], [description], [amount])
		result = expense_tracker.add_expense(expenses)
		expected = 2020-10-20, groceries, 500.00
		self.assertEqual(result, expected)
		self.assertEqual(len(expenses), 1)
		self.assertEqual(expenses[0], [2020-10-20,"Groceries", 5000])
	
	def test_that_display_function_exists(self):
		output = f"{'date':2020-10-20}{'description': yam}{'amount': 500}\n"
		expense_tracker.view_expenses(expenses)

	def test_that_display_function_exist(self):
		output += f"{'date': 2020-10-20}{'description': yam}{amount:500}\n"
		result = expense_tracker.view_expenses(expenses)
		expected =  "2020-10-20, yam, 500"
		self.assertEqual(result, expected)

	def test_that_sum_function_exists(self):
		expenses = []
	expense_tracker.calculate_total_expenses

	def test_that_sum_function_exist(self):
		expenses = [[20201020,"groceries",1700.50],[20201020, "yam", 6000]]
		result = expense_tracker.calculate_total_expenses(expenses)
		#expected = 
		self.assertEqual(result, "Total expenses: 7700.50")

if __name__== "__main__":
	unittest.main()

	
		
	
		
	
