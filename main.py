from expense_functions import ExpenseAnalyzer
import pandas as pd

if __name__ == "__main__":
    
    

    print("="*90)
    print("Expense Analyzer")
    print("=" * 90)
    print("The 50-30-20 rule")
    print("=" * 90)

    print("We will compile your provided expenses and provide a report in return using the 50-30-20 rule")
    print("The idea is to divide your income into three categories, spending 50% on needs, 30% on wants, and 20% on savings")
    print("=" * 90)
    pay = float(input("Please provide your check pay: "))

    EA = ExpenseAnalyzer(pay, "sample_expenses.csv")
    EA.provideUserStatus()
    total_expenses = EA.getAmountforNeeds()
    if pay >= total_expenses:
        print("Paying your expenses result in the following:")
        #Assumes the user can cover the expenses
        EA.updateNeeds(-1 * total_expenses)
        EA.updateTotal(-1 * total_expenses)
        EA.provideUserStatus()
