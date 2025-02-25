def display_menu():
	print ("SAMPLE RUN")
	print ("TO-DO LIST MANAGER")
	print ("""
	1. Add a task
	2. View task
	3. Mark task as complete
	4. Delete a task
	5. Exit
		""") 



def main_pass():
	to_do = {}
	while True:
	  display_menu() 
	  option = input("choose an option (1-4): ")
	  if option == "1":
	     task = input("Add a task: ")
	     print(add_task(to_do, 'serialnumber': task)
	  elif option == "2":
	     print(view_task(to_do))
	  elif option == "3":
	     print( mark_complete_tasks(to_do))
	  elif option == "4":
	     print(delete_a_task(to_do))
	  elif option == "5":
	     print("***Exiting the To-Do List Manager...... Bye***")   
	     print(display_task_with_status(to_do))	
		break
	  else:
	     print("<<<Invalid Input.>>>")

def add_task(to_do):
	try:
		task = str(task)
		to_do.append([serial_number])
		return "Task added!!!"
	except ValueError:
		return "<<<invalid serial number and task entered .>>> please follow instructions."


def view_task(to_do):
	if not to_do:
	     return "no To-Do List input"
	output = "\nto_do:\n"
	output += f"{'serial_number':<12}{'task':<12}\n"
	#output += "-" * 50 + "\n"
	for list in to_do:
		output += f"{to_do[0]:<12}\n"
	return output

def Serial_Number(to_do):
	figure = [serial_number]
	for figure in [serial_number]:
		counter += figure
	[serial_number] = counter

def mark_complete_tasks(to_do):
	if number_entered == figure:
	print("(to_do)[x]")
	else
	print("(to_do)[]")
	



def delete_a_task(to_do):
	if not to_do:
		return "Empty List "
	number_entered = int(input(Enter serial number of task you need to delete)) 
	total = to_do.pop("serial_number[number_entered]")
	return total
		

def display_task_with_status(to_do):
	



if __name__== "__main__":
	main_pass()