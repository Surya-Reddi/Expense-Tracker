from expense import Expense

def main():
    print('Running Expense Tracker\n')
    
    #Get the input for expense.
    print(get_expense())
    
    #Store it in a file.
    save_expense()
    
    #Summarize the expense
    summarize_expense()
    
    pass

def get_expense():
    print("Getting user expense\n")
    expense_name = input("Enter expense name: ")
    exppense_amount = float(input("Enter expense amount: "))
    print(f"you've entered {expense_name}, {exppense_amount}")
    
    expense_categories = [
        "Food", "Education", "Clothes", "Fun", "Other"
    ]
    
    while True:
        print("Select a category")
        for i, category in enumerate(expense_categories):
            print(f"{i+1}) {category}")
            
        value_range = f"1 - {len(expense_categories)}"
        selected_index = int(input(f"Enter a category number: {value_range} "))-1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=exppense_amount)
            return new_expense
        else:
            print("Invalid category, select again!")
            
    

def save_expense():
    print("Saving expenses\n")
    pass

def summarize_expense():
    print("Summarizing expenses\n")
    pass

if __name__ == "__main__":
    main()