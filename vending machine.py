MAX_LINES=5   
MAX_BET=100
MIN_BET=1

def deposit():
    while True:
        amount=input("How much you like to deposit ? ")
        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print("Enter more than Zero !")
        else:
            print("Enter a number...")
    return amount

def no_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on(1-"+str(MAX_LINES)+")?" )
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print("Enter valid lines !")
        else:
            print("Enter a number...")
    return lines

def get_bet():
    while True:
        amount=input("How much you like to bet ? ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<MAX_BET:
                break
            else:
                print(f"Enter more than between ${MIN_BET}-${MAX_BET} !")
        else:
            print("Enter a number...")
    return amount



def main():
    balance=deposit()
    lines=no_of_lines()
    bet=get_bet()
    total_bet=bet*lines
    print(f"You are betting ${bet} on ${lines}lines. Your Total bet is equal to: ${total_bet}")
    print(balance,lines)



main()