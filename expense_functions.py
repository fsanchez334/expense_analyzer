import pandas as pd 

class ExpenseAnalyzer:
    def __init__(self, paycheck_amount, expenses_file):
        self.needs = paycheck_amount * 0.5
        self.wants = paycheck_amount * 0.2
        self.savings = paycheck_amount * 0.3
        self.expenses = pd.read_csv(expenses_file)

    def getSavings(self):
        return self.savings
    
    def getAmountforNeeds(self):
        return self.needs

    def getAmoutforWants(self):
        return self.wants
    
    def modifySavingsAmount(self, amount):
        self.savings += amount
    
    def modifyNeedsAmount(self, amount):
        self.needs += amount
    
    def modifyWantsAmount(self, amount):
        self.wants += amount

    def expense_collection(self):
        #Collect all the payments that must be made from the 50% amount
        costs = self.expenses.get("Amount").tolist()
        return sum(costs)
    
    def provideUserStatus(self):
        print("To cover must-have costs, you have {}".format(self.needs))
        print("The amount you can use for your savings is {}".format(self.savings))
        print("The amount you can use for your wants is {}".format(self.wants))