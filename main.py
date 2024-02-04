from expense_functions import *
from credit_analyzer import CreditAnalyzer
from IPython.display import display
import pandas as pd

if __name__ == "__main__":
    
    
    formatIntro()
    main_df = pd.read_csv("sample_expenses.csv")

    credit_boolean = main_df["Credit Card?"] == "Y"
    credit_df = main_df[credit_boolean]
    pay = float(input("Please provide your check pay: "))
    EA = ExpenseAnalyzer(pay, main_df)
    CA = CreditAnalyzer(credit_df)
    EA.provideUserStatusRule()

    amount_available_for_expenses = EA.getAmountforNeeds()
    expected_expenses = EA.expense_collection()
    #How much of the total is attributed to credit card debt
    EA.coveringExpensesBlurb(expected_expenses)
    


    credit_used_amount = CA.calculate_credit_card_utilization()
    credit_used_percent = CA.getCreditUtilization()
    print("Your credit card debt is {} ".format(credit_used_amount))
    print("Your credit utilization is {}".format(credit_used_percent))
    credit_df = CA.credit_card_breakdown()
    credit_dict = CA.constructCreditDict(credit_df)

    display(credit_df)
    print("Based on your input, these are the credit cards, in order of priority that you should pay")
    CA.credit_heap(credit_df, credit_dict)
    print("You have the option to choose a card and provide the desired percent utilization for that card - we can then calculate how much you need to pay to reach that desired goal")
    manage_credit_response = input("Would you like to try it? Yes/No: ")
    manage_boolean = False
    running_credit_sum = 0
    if manage_credit_response == "Yes":
        manage_boolean = True
    while manage_boolean:
        credit_card_name = input("What credit card would you like to analyze? ")
        desired_utilization = float(input("What's your desired utilization? Please input in decimal form (ex. 0.13 for 15%): "))
        message, calculated_pay= CA.calculateOptimalPayment(credit_dict, credit_card_name, desired_utilization)
        print(message)
        add_to_credit_sum = input("Would you like to set this amount to pay off credit debt? Yes/No: ")
        if add_to_credit_sum == "Yes":
            running_credit_sum += calculated_pay
        more_ = input("Would you like to analyze another card or the same card with a different desired utilization? Yes/No: ")
        if more_ != "Yes":
            manage_boolean = False
    print("You will use {} to go towards paying down credit card debt".format(running_credit_sum))
