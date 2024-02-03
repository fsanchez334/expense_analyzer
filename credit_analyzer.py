from IPython.display import display
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import heapq as hq

class CreditAnalyzer:
    def __init__(self, credit_card_df):
        self.credit_used = 0
        self.credit_card_df = credit_card_df
    
    def credit_card_utilization(self):
    #Get Credit Card dataframes
        
        total_credit_allowed = sum(self.credit_card_df.get("Total").tolist())
        total_credit_used = sum(self.credit_card_df.get("Amount").tolist())
        self.credit_used = float(total_credit_used/ total_credit_allowed)

    
    def credit_card_breakdown(self):
        #Here, we return the breakdown of each credit card, including amount used, total and interest rate
        col = self.credit_card_df.apply(lambda row: float(row.Amount / row.Total), axis=1)
        interest_column = self.credit_card_df.apply(lambda row: ((row["Interest Rate"] / 12) / 100) * row['Amount'], axis=1)

        df_credit_card = self.credit_card_df.assign(percent_used=col.values)
        df_credit_card = self.credit_card_df.assign(approximateInterest=interest_column)
        columns = ["Expense", "Amount", "Total", "Interest Rate", "approximateInterest", "percent_used"]
        df_credit_card = df_credit_card[columns]
        return df_credit_card

    def credit_heap(self):
        #Here, we will take in the credit df and only get the CC, the amount, interest_rate, percent_used
        focused_columns = ["Expense", "approximateInterest", "percent_used"]
        df_starter = self.credit_card_df[focused_columns]
        #We will need to scale the interest and the percent used
        scaler = MinMaxScaler()
        df_starter[["approximateInterest", "percent_used"]] = scaler.fit_transform(df_starter[["approximateInterest", "percent_used"]])
        #Now that we have constructed this - we are ready construct our Priority Heap (we can use the average of the scaled percentages)
        credit_cards = df_starter["Expense"].tolist()
        summation = ((df_starter["approximateInterest"] +  df_starter["percent_used"]) / 2).tolist()
        heap = []
        for i in range(len(credit_cards)):
            heap.append((summation[i] * -1, credit_cards[i]))
        hq.heapify(heap)
        while len(heap) != 0:
            credit_tuplet = hq.heappop(heap)
            print(credit_tuplet[1])
            
