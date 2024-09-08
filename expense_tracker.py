from expense import Expense

def main():
    print('Running Expense Tracker\n')
    expense_file_path = "expense.csv"
    budget = 1000
    #Get the input for expense.
    expense = get_expense()
    
    #Store it in a file.
    save_expense(expense, expense_file_path)
    
    #Summarize the expense
    summarize_expense(expense_file_path, budget)
    

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
            
    

def save_expense(expense, expense_file_path):
    print("Saving expenses\n")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing expenses\n")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name,expense_category,expense_amount = line.strip().split(',')
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key]+= expense.amount
        else:
            amount_by_category[key] = expense.amount
    print(amount_by_category)
    total_spent = sum([a.amount for a in expenses])
    print(f"You have spent {total_spent} this month")
    print(f"Remaining money : {budget-total_spent}")

if __name__ == "__main__":
    main()