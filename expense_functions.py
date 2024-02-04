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
        #Update - we should remove the credit_card expenses - those will be seperate
        no_credit_boolean = self.expenses["Credit Card?"] == "N"
        costs = self.expenses[no_credit_boolean].get("Amount").tolist()
        return sum(costs)
    def provideUserStatusRule(self):
        title = "Applying the 50-30-20 rule"
        adornments = "*" * 100
        print(adornments.center(100))
        print(title.center(100))
        print("You currently have {}".format(self.total_amount))
        print("To cover must-have costs, you have {}".format(self.needs))
        print("The amount you can use for your savings is {}".format(self.savings))
        print("The amount you can use for your wants is {}".format(self.wants))

    def coveringExpensesBlurb(self, expected_expenses):
        title = "Covering Expenses"
        adornments = "*" * 100
        print(adornments.center(100))
        print(title.center(100))
        print("Your expected expenses total (without credit card debt): {}".format(expected_expenses))

def formatIntro():
    intro_string = "Expense Analyzer: Compiles provided expenses and provides a report using the 50-30-20 rule"
    print("=" * len(intro_string))
    print(intro_string)
    print("="* len(intro_string))

 
        
        
