# Expense Tracker

A command-line application for managing personal expenses with features to add, categorize, search, and export financial data.

## Features

✨ **Core Functionality:**
- ➕ Add expenses with category and date
- 📊 Display all expenses or filter by category
- 🗑️ Delete specific expense records
- 💰 Find the highest expense
- 📤 Export data to CSV, TXT, or DAT formats
- 💾 Persistent storage using CSV files

## Getting Started

### Prerequisites
- Python 3.x
- No external dependencies required (uses only built-in libraries)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

2. Run the application:
```bash
python expense_tracker.py
```

## Usage

### Main Menu
When you start the application, you'll see:
```
==============================
             Menu
==============================
0 - to exit program
1 - to add expense
2 - to display all expenses
3 - to display all expenses in a category
4 - to delete a record
5 - to find highest expense
6 - to export data
==============================
```

### Example Workflow

**Adding an Expense:**
1. Select option `1`
2. Enter amount (e.g., `45.50`)
3. Enter category (e.g., `Groceries`)
4. Enter date in YYYY-MM-DD format (e.g., `2024-01-15`)

**Viewing Expenses:**
- Option `2`: Shows all expenses sorted by date with total
- Option `3`: Filter expenses by specific category
- Option `5`: Displays your highest expense

**Exporting Data:**
- Select option `6`
- Choose file format: `.csv`, `.txt`, or `.dat`
- Enter filename (e.g., `expenses_backup.csv`)

## File Structure

```
expense-tracker/
├── expense_tracker.py       # Main application file
├── expenses.csv             # Data storage (auto-created)
└── README.md               # This file
```

## Technical Details

### Data Storage
- Expenses are stored in a CSV file with columns: Category, Amount, Date
- Automatic file creation if not present
- Data persists between sessions

### Input Validation
- Amount: Must be positive numbers
- Category: Letters and spaces only
- Date: Must be in YYYY-MM-DD format with valid day/month
- Handles leap years correctly

### Functions

| Function | Purpose |
|----------|---------|
| `load_expenses()` | Load data from CSV file |
| `save_expenses()` | Save data to CSV file |
| `add_expense()` | Add new expense to list |
| `display_expenses()` | Show all expenses sorted by date |
| `display_by_category()` | Filter and show expenses by category |
| `highest_expense()` | Find expense with highest amount |
| `delete()` | Remove expense record |
| `export_as()` | Export data to different formats |

## Known Limitations
- No duplicate expense detection
- Date validation follows basic rules (doesn't check for all impossible dates)
- Single CSV file storage (no database)

## Future Enhancements
- 📈 Monthly/yearly expense reports
- 🏷️ Expense tags and notes
- 📱 Budget tracking and alerts
- 📊 Data visualization with charts
- 🔍 Advanced filtering options

## Author
[Your Name]

## License
This project is open source and available under the MIT License.

## Contact
For questions or suggestions, feel free to reach out!
