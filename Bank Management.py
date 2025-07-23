Accounts = {101:1000,102:2000,103:3000}

def get_time():
    from datetime import datetime
    import pytz
    time_zone = pytz.timezone('Asia/Calcutta')
    b = datetime.now(time_zone)
    return datetime.time(b)


def deposit(num):
    amt = int(input("Enter the amount to be deposited: "))
    Accounts[num] += amt
    print(f"Rs.{amt} credited to your account at {get_time()}. Available Balance:{Accounts[num]}")

def withdraw(num):
    amt = int(input("Enter the amount to be withdrawn: "))
    if amt > Accounts[num]:
        print("Insufficient balance")
    else:
        Accounts[num] -= amt
        print(f"Rs.{amt} debited from your account at {get_time()}. Available balance:{Accounts[num]}")

def transfer(num):
    amt = int(input("Enter the amount to be transferred: "))
    if amt > Accounts[num]:
        print("Insufficient balance")
    else:
        to_acc = int(input("Enter the recipient account number: "))
        if to_acc not in Accounts:
            print("Recipient account not found")
        else:
            Accounts[num] -= amt
            Accounts[to_acc] += amt
            print(f"Rs.{amt} sent to {to_acc} from {num} at {get_time()}")

def menu(num):
    while True:
        print(f"\n---Menu for {num}---")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Amount Transfer\n5. Logout")
        c = int(input("Enter the required service: "))
        match c:
            case 1:
                print(f"Your account balance is: {Accounts[num]}")
            case 2:
                deposit(num)
            case 3:
                withdraw(num)
            case 4:
                transfer(num)
            case 5:
                break
            case _:
                print("Invalid choice")            

while True:
    print("---Welcome---")
    num = int(input("Enter your account number(or 0 to exit): "))
    if num == 0:
        exit(0)
    elif num not in Accounts:
        print("Invalid account number")
    else:
        menu(num)