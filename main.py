import credit_card_calc as cc
if __name__ == "__main__":
    
    

    print("Hello there!")
    print("We will compile your provided expenses and provide a report in return")
    pay = float(input("We will apply the 50-30-20 rule - please provide your pay per pay period: "))
    print(cc.fifty_thirty_rule(pay))
    # credit_cards = []
    # interest_rates = {}
    # while True:
    #     container = [x for x in input("Please provide name of bank, the balance you have on that card, the limit, and the APR: ").split(" ")]
    #     if container[0] == '':
    #         break
    #     else:
    #         for i in range(1, len(container)):
    #             container[i] = float(container[i])
    #         credit_card_tuple = tuple(container)
    #         print(credit_card_tuple)
    #         credit_cards.append(credit_card_tuple)
    #         interest_rates[credit_card_tuple[0]] = credit_card_tuple[3]
    
    # print(interest_rates)
    # print(cc.credit_utiliza
    # tion(credit_cards))
    # print(cc.calculate_accrued_interest())