class ExpenseAnalyzer:
    def __init__(self, paycheck_amount, df):
        self.total_amount = paycheck_amount
        self.needs = paycheck_amount * 0.5
        self.wants = paycheck_amount * 0.3
        self.savings = paycheck_amount * 0.2
        self.expenses = df

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

 
        
        
