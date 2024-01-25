
def fifty_thirty_rule(take_home_pay):
    fifty_percent = 0.5 * take_home_pay
    thirty_percent = 0.3 * take_home_pay
    twenty_percent = 0.2 * take_home_pay

    return (fifty_percent, thirty_percent, twenty_percent)
 
def credit_utilization(list_of_credit_cards):
    #Should calculate the credit utilization of the cards you have
    '''
    @param list_of_credit_cards -> list of tuples of size 2
    '''
    total_limit = 0
    total_used = 0 
    for tuplet in list_of_credit_cards:
        total_limit += tuplet[2]
        total_used += tuplet[1]
        print("For card {}, this is credit utilization: {}".format(tuplet[0], total_used/total_limit))
    return total_used / total_limit