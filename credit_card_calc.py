#Credit card calculator
#First, get the total credit card

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

def calculate_accrued_interest(total_used, interest):
    #Assume 30 day cycle
    #Divide APR by number of days in year
    daily_rate = interest / 365
    #Multiply daily rate by average daily balance(end of the bill cycle)
    return total_used * interest
def interest_rate(list_of_cards, interest_rates):
    '''
    Using the interest rates, return a sorted list. The sorted list should be orderd
    in Descending order (maxumim amount of interest to pay to min interest rate to pay)
    '''
    credit_card_info = []
    for cc_tuplet in list_of_cards:
        #Search the interest accrued for the billing period
        credit_card = cc_tuplet[0]
        total_used = cc_tuplet[1]
        #Get the interest rate for credit card
        interest_rate = interest_rates[credit_card]
        accrued_interest = calculate_accrued_interest(total_used, interest_rate)
        credit_card_info.append((credit_card, accrued_interest))
    #Sort the list
    credit_card_info.sort(key= lambda a: a[1], reverse=True)
    return credit_card_info