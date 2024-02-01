from IPython.display import display
import pandas as pd
class ExpenseAnalyzer:
    def __init__(self, paycheck_amount, expenses_file):
        self.total_amount = paycheck_amount
        self.needs = paycheck_amount * 0.5
        self.wants = paycheck_amount * 0.3
        self.savings = paycheck_amount * 0.2
        self.expenses = pd.read_csv(expenses_file)

    def getSavings(self):
        return self.savings
    
    def getAmountforNeeds(self):
        return self.needs

    def getAmoutforWants(self):
        return self.wants
    
    def updateTotal(self, amount):
        self.total_amount += amount
    
    def updateSavings(self, amount):
        self.savings += amount
    
    def updateNeeds(self, amount):
        self.needs += amount
    
    def updateWants(self, amount):
        self.wants += amount

    def expense_collection(self):
        #Collect all the payments that must be made from the 50% amount
        costs = self.expenses.get("Amount").tolist()
        return sum(costs)
    def provideUserStatus(self):
        print("*" * 90)
        print("You currently have {}. This assumes you want to pay off all of your credit card debt".format(self.total_amount))
        print("To cover must-have costs, you have {}".format(self.needs))
        print("The amount you can use for your savings is {}".format(self.savings))
        print("The amount you can use for your wants is {}".format(self.wants))
        print("*" * 90)

    def credit_card_utilization(self):
        #Get Credit Card dataframes
        credit_boolean = self.expenses["Credit Card?"] == "Y"
        df_credit_card = self.expenses[credit_boolean]
        total_credit_allowed = sum(df_credit_card.get("Total").tolist())
        total_credit_used = sum(df_credit_card.get("Amount").tolist())
        return float(total_credit_used/ total_credit_allowed)
    
    
    def credit_card_breakdown(self):
        #Here, we return the breakdown of each credit card, including amount used, total and interest rate
        credit_boolean = self.expenses["Credit Card?"] == "Y"
        df_credit_card = self.expenses[credit_boolean]
        col = df_credit_card.apply(lambda row: float(row.Amount / row.Total), axis=1)
        interest_column = df_credit_card.apply(lambda row: ((row["Interest Rate"] / 12) / 100) * row['Amount'], axis=1)

        df_credit_card = df_credit_card.assign(percent_used=col.values)
        df_credit_card = df_credit_card.assign(approximateInterest=interest_column)
        columns = ["Expense", "Amount", "Total", "Interest Rate", "approximateInterest", "percent_used"]
        df_credit_card = df_credit_card[columns]
        return df_credit_card

    # def credit_heap(self, df):
    #     #Here, we will take in the credit df and only get the CC, the amount, interest_rate, percent_used
    #     focused_columns = ["Expense", "Amount", "Interest Rate", "percent_used"]
        
        
