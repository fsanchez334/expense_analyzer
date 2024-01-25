import credit_card_calc as cc

if __name__ == "__main__":
    
    

    print("Hello there!")
    print("We will compile your provided expenses and provide a report in return")
    pay = float(input("We will apply the 50-30-20 rule - please provide your check pay: "))
    tuplet_split = cc.fifty_thirty_rule(pay)
    print("50% is {}, 30 % is {}, and 20% is {}".format(tuplet_split[0], tuplet_split[1], tuplet_split[2]))