import credit_card_calc as cc
if __name__ == "__main__":
    print("Hello there!")
    print("We will compile your provided expenses and provide a report in return")
    print("You will need to provide the name of your credit card, your current balance, your limit, and your APR")
    
    credit_cards = []
    while True:
        container = [x for x in input("Please provide name of bank, the balance you have on that card, the limit, and the APR: ").split(" ")]
        if container[0] == '':
            break
        else:
            for i in range(1, len(container)):
                container[i] = float(container[i])
            credit_card_tuple = tuple(container)
            print(credit_card_tuple)
            credit_cards.append(credit_card_tuple)
    
    
    print(cc.credit_utilization(credit_cards))