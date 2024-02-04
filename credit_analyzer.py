from IPython.display import display
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import heapq as hq

class CreditAnalyzer:
    def __init__(self, credit_card_df):
        self.credit_used = 0
        self.credit_card_df = credit_card_df

    def getCreditUtilization(self):
        return self.credit_used
    
    def calculate_credit_card_utilization(self):
    #Get Credit Card dataframes
        total_credit_allowed = sum(self.credit_card_df.get("Total").tolist())
        total_credit_used = sum(self.credit_card_df.get("Amount").tolist())
        self.credit_used = float(total_credit_used/ total_credit_allowed)
        return total_credit_used
    
    def credit_card_breakdown(self):
        #Here, we return the breakdown of each credit card, including amount used, total and interest rate
        percent_column = self.credit_card_df.apply(lambda row: float(row.Amount / row.Total), axis=1)
        interest_column = self.credit_card_df.apply(lambda row: ((row["Interest Rate"] / 12) / 100) * row['Amount'], axis=1)

        df_credit_card = self.credit_card_df.assign(percent_used=percent_column)
        df_credit_card = df_credit_card.assign(approximateInterest=interest_column)
        columns = ["Expense", "Amount", "Total", "Interest Rate", "approximateInterest", "percent_used"]
        df_credit_card = df_credit_card[columns]
        return df_credit_card
    
    def constructCreditDict(self, df):
        container = df.copy()
        container["Expense"] = container["Expense"].apply(lambda x: x.strip())
        container.set_index("Expense", drop=True, inplace=True)
        credit_dict = container.to_dict(orient="index")
        return credit_dict

    def credit_heap(self, df, credit_dict):
        #Here, we will take in the credit df and only get the CC, the amount, interest_rate, percent_used
        focused_columns = ["Expense", "approximateInterest", "percent_used"]
        df_starter = df[focused_columns].copy()
        #We will need to scale the interest and the percent used
        scaler = MinMaxScaler()
        df_starter.loc[:, ["approximateInterest", "percent_used"]] = scaler.fit_transform(df_starter[["approximateInterest", "percent_used"]])
        #Now that we have constructed this - we are ready construct our Priority Heap (we can use the average of the scaled percentages)
        credit_cards = df_starter["Expense"].tolist()
        summation = ((df_starter["approximateInterest"] +  df_starter["percent_used"]) / 2).tolist()
        heap = []
        for i in range(len(credit_cards)):
            heap.append((summation[i] * -1, credit_cards[i]))
        hq.heapify(heap)
        while len(heap) != 0:
            credit_tuplet = hq.heappop(heap)
            credit_card_name = credit_tuplet[1]
            print(credit_card_name)
                
            
    def calculateOptimalPayment(self, credit_dict, card_name, goal_utilization):
        #We need the amount, total
        goal_amount = credit_dict[card_name]['Total'] * goal_utilization
        need_to_pay = credit_dict[card_name]['Amount'] - goal_amount
        message_= "In order for the card {} to be {}% utilized, you'd need to pay {}".format(card_name, goal_utilization, need_to_pay)
        return message_, need_to_pay