import credit_card_calc as cc
if __name__ == "__main__":
    print("Hello there - provide inputs to gather your_reports")
    chase_unlimited = ('Chase Freedom Unlimited' , 500, 3600)
    chase_sapphire = ('Chase Sapphire', 470, 16000)
    amex = ('Amex', 290, 5500)
    best_buy = ('Best Buy', 0, 3000)

    interest_rates = {
        'Chase Freedom Unlimited': 0.2024,
        'Chase Sapphire': 0.2349,
        'Amex': 0.00,
        'Best Buy': 0.2
    }
    cards = [chase_unlimited, chase_sapphire, amex, best_buy]
    print(cc.credit_utilization(cards))
    #Sorted list of credit cads to pay
    print(cc.interest_rate(cards, interest_rates))