import csv
import pickle
def load_expenses(filename):
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            expenses = []
            try:
                header = next(reader)
            except:
                print("File might be corrupted. Starting over with an empty list.\n")
                expenses = []
            for line in reader:
                try:
                    if len(line) == 3:    
                        expense = {}
                        expense[header[0]] = line[0]
                        expense[header[1]] = float(line[1])
                        expense[header[2]] = line[2]
                        expenses.append(expense)
                except (IndexError, ValueError):
                    continue
    except FileNotFoundError:
        print("File wasn't found.. Returning empty list.")
        expenses = []
    return expenses
def save_expenses(expenses, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'Amount', 'Date'])
        for expense in expenses:
            writer.writerow([expense['Category'], f"{expense['Amount']:.2f}", expense['Date']])
def add_expense(expenses, amount, category, date):
    expense = {
        'Category': category,
        'Amount': amount,
        'Date': date
    }
    print(f"Expense added: ${amount:.2f} to {category.lower()} on {date}")
    expenses.append(expense)
def highest_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return None
    highest = expenses[0]
    for expense in expenses:
        if float(expense['Amount']) > float(highest['Amount']):
            highest = expense
    print(f"Highest expense: Amount: ${highest['Amount']:.2f}, Category: {highest['Category']}, Date: {highest['Date']}")
    return highest
def delete(expenses):
    if len(expenses) == 0:
        print("No records to delete.")
        return expenses
    new_expenses = []
    for i in range(1, len(expenses) + 1):
        print(f"{i}. Date: {expenses[i-1]['Date']}, Category: {expenses[i-1]['Category']}, Amount: {expenses[i-1]['Amount']:.2f}")
    try:
        record = int(input("Which record do you want to delete? (number): "))
        if record > 0 and record <= len(expenses):
            for i in range(len(expenses)):
                if i != (record - 1):
                    new_expenses.append(expenses[i])
            values = expenses[record - 1]
            print(f"Successfully deleted: Category - {values['Category']}, Amount - ${values['Amount']:.2f}, Date - {values['Date']}")
            return new_expenses
        else:
            print("Number out of range. No record deleted.")
            return expenses
    except ValueError:
        print("Input must be a number value. Please enter a valid number value.")
        return expenses

def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("==============================")
        print("         Expenses")
        print("==============================")
        unsorted_pairs = []
        for i in range(len(expenses)):
            unsorted_pairs.append((expenses[i]['Date'], expenses[i]['Category'], float(expenses[i]['Amount']), i))
        sorted_pairs = sorted(unsorted_pairs)

        total = 0
        for date, category, amount, i in sorted_pairs:
            expense = expenses[i]
            total += amount
            print(f"Date: {date}, Category: {category.capitalize()}, Amount: ${amount:.2f}")
        print("==============================")
        print(f"Total: ${total:.2f}")
        print("==============================")
def display_by_category(expenses):
    if not expenses:
        print("No expenses to display.")
    else:
        unsorted_pairs = []
        for i in range(len(expenses)):
            unsorted_pairs.append((expenses[i]['Date'], expenses[i]['Category'], float(expenses[i]['Amount']), i))
        unsorted_pairs.sort()
        sorted_pairs = unsorted_pairs

        categories = []
        for date, category, amount, i in sorted_pairs:
            if category not in categories:
                categories.append(category)
        categories.sort()
        print("Availible categories: ")
        for category in categories:
            print(f" - {category}")

        cat_input = category_input("Enter the category to display: ")
        print("==============================")
        print(f"         {cat_input}")
        print("==============================")

        cat_found = False
        for category in categories:
            if cat_input.lower() == category.lower():
                cat_found = True
                break
        if cat_found:
            total = 0
            for date, category, amount, i in sorted_pairs:
                if category.lower() == cat_input.lower():
                    expense = expenses[i]
                    total += amount
                    print(f"Date: {date}, Category: {category.capitalize()}, Amount: ${amount:.2f}")
            print("==============================")
            print(f"Total: ${total:.2f}")
            print("==============================")

def export_as(expenses, filename):
    if not expenses:
        print("No expenses to export.")
        return
    file_type = filename.lower().split(".")[1]
    if file_type == "txt":
        try:
            with open(filename, "w") as f:
                f.write("Category, Amount, Date\n")
                for expense in expenses:
                    f.write(f"{expense['Category']}, {expense['Amount']:.2f}, {expense['Date']}\n")
                print(f"Successfully exported data to {filename}.")
        except FileNotFoundError:
            print("FileNotFound Error occurred.")
    elif file_type == "dat":
        try:
            with open(filename, "wb") as f:
                pickle.dump(["Category", "Amount", "Date"], f)
                for expense in expenses:
                    formatted_expense = {
                        'Category': expense['Category'],
                        'Amount': f"{expense['Amount']:.2f}",
                        'Date': expense['Date']
                    }
                    pickle.dump(formatted_expense, f)
                print(f"Successfully exported data to {filename}.")
        except FileNotFoundError:
            print("FileNotFound Error occurred.")

    elif file_type == "csv":
        try:
            with open(filename, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Category', 'Amount', 'Date'])
                for expense in expenses:
                    writer.writerow([expense['Category'], f"{expense['Amount']:.2f}", expense['Date']])
            print(f"Successfully exported data to {filename}.")
        except FileNotFoundError:
            print("FileNotFound Error occurred.")

    else:
        print("Only .txt, .dat and .csv files are accepted.")
def integer_input(text):
    while True:
        value = input(text).lower().strip()
        if value in ["0","1","2","3","4","5","6","zero","one","two","three","four","five","six"]:
            return value
        print("Invalid choice. Please try again.")
def amount_input():
    while True:
        try:
            value = float(input("Enter the expense amount: "))
            if value <= 0:
                print("Amount should be more than 0. Please enter a valid Amount.")
                continue
            return value
        except ValueError:
            print("Invalid input. The amount should be a number value.")
def category_input(text="Enter the expense category: "):
    while True:
        value = input(text).strip()
        
        if not value:
            print("Category cannot be left empty. Please enter a valid Category.")
            continue
        
        valid = True
        for char in value:
            if not (char.isalpha() or char.isspace()):
                valid = False
                break
        
        if valid:
            return value.capitalize()
        else:
            print("Category should only contain letters and spaces. No numbers or special characters.")

def date_input():
    while True:
        date_str = input("Enter the expense date: ").strip()
        parts = date_str.split('-')
        if (len(parts) == 3 and
            parts[0].isdigit() and
            parts[1].isdigit() and
            parts[2].isdigit() and
            len(parts[0]) == 4):
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                if month == 2 and day > 29:
                    print("February has only 28 or 29 days.")
                    continue
                else:
                    if month == 2: 
                        is_leap = (year%4 == 0 and (year%100 != 0 or year%400 == 0))
                        if is_leap:
                            max_feb_day = 29
                        else:
                            max_feb_day = 28
                        if day > max_feb_day:
                            if is_leap:
                                print(f"{year} is a leap year so February only has 29 days. Please enter a valid date.")
                            else:
                                print(f"{year} is not a leap year so February only has 28 days. Please enter a valid date.")
                            continue
                if month in [4, 6, 9, 11] and day > 30:
                    print(f"{month} month has only 30 days.")
                    continue
                return f"{year:04d}-{month:02d}-{day:02d}"
        
        print("Invalid format. Please use YYYY-MM-DD.")
def filename_check():
            while True:
                    filename = input("Enter the file name to export to: ")
                    if "." not in filename:
                        print("Not a valid file name. try using .txt, .dat or .csv")
                        continue
                    if filename.lower().split(".")[1] in ["dat", "txt", "csv"]:
                        return filename
                    else:
                        print("Only .txt, .dat and .csv file types are accepted. Please try again.")
expenses = load_expenses('expenses.csv')
while True:
    print("==============================")
    print("             Menu")
    print("==============================")
    print("0 - to exit program")
    print("1 - to add expense")
    print("2 - to display all expenses")
    print("3 - to display all expenses in a category")
    print("4 - to delete a record")
    print("5 - to find highest expense")
    print("6 - to export data")
    print("==============================")
    ch = integer_input("Enter your choice: ").strip().lower()
    if ch == '0' or ch == "zero":
        print("Exiting the expense tracker application.")
        break
    elif ch == '1' or ch == "one":
        amount = amount_input()
        category = category_input()
        date = date_input()
        add_expense(expenses, amount, category, date)
    elif ch == '2' or ch == "two":
        display_expenses(expenses)
    elif ch == '3' or ch == "three":
        display_by_category(expenses)
    elif ch == '4' or ch == "four":
        expenses = delete(expenses)
    elif ch == '5' or ch == "five":
        highest_expense(expenses)
    elif ch == '6' or ch == "six":
        filename = filename_check()
        
        export_as(expenses, filename)
    try:
        save_expenses(expenses, 'expenses.csv')
    except:
        print(f"An error occurred while saving expenses. Please try again.")
        break