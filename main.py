from expense_functions import ExpenseAnalyzer
import pandas as pd

if __name__ == "__main__":
    
    

    print("Hello there!")
    print("We will compile your provided expenses and provide a report in return")
    pay = float(input("We will apply the 50-30-20 rule - please provide your check pay: "))
    #TODO: Probably give context to what each percentage represents

    EA = ExpenseAnalyzer(pay, "sample_expenses.csv")
    EA.provideUserStatus()
    total_expenses = EA.expense_collection()
    print("The total amount of expenses you need to cover is {}".format(total_expenses))
    