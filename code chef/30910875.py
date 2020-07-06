# cook your dish her
def calculate_cash(balance):
    if(balance[0]%5==0):
        if((balance[0]+0.5)<=balance[1]):
            mybalance = balance[1] - balance[0] - 0.5
            return mybalance
        else:
            return balance[1]
    else:
        return balance[1]
balance = list(map(float,input().split()))
rem_balance = calculate_cash(balance)
print("{:.2f}".format(rem_balance))
print()