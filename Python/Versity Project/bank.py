bank = {
    "rt_jeion":{
        "name":"Md. Rejuwan Tasfic",
        "pin":"20052025",
        "balance":5000,
        "history": [("Deposit", 1000), ("Withdraw", 500), ("Deposit", 4500)]
    },
    "zoro":{
        "name":"Roronoa Zoro, King of Hell",
        "pin":"12345678",
        "balance":1000000,
        "history": [("Deposit", 1000000), ("Withdraw", 500), ("Deposit", 500)]
    },
    "luffy":{
        "name":"Monkey D. luffy, Sun God Nika",
        "pin":"meatmeat",
        "balance":0,
        "history": [("Deposit", 100000000), ("Withdraw", 100000000)]
    },
    "sanji":{
        "name":"Sanji The Cook, Mr. Prince",
        "pin":"nami....chaaaan",
        "balance":1000001,
        "history": [("Deposit", 1000000), ("Withdraw", 500), ("Deposit", 501)]
    }
}

def create_account(user_name):
    if user_name in bank.keys():
        return "user_name already exists.."
    bank[user_name] = {}
    name = input("Enter You full name: ")
    bank[user_name]["name"] = name
    print("Enter your pin (minimum 8 digit): ")
    while True:
        pin = input()
        len_pin = len(pin)
        if len_pin >= 8:
            bank[user_name]["pin"] = pin
            print("Pin created successfully.")
            break
        else:
            print("Input Pin is less than 8 digit...")
            print("Enter your pin again (minimum 8 digit): ")

    bank[user_name]["balance"] = 0
    bank[user_name]["history"] = []
    #print(bank[user_name])
    return f"Account successfully Created.\nUser name:{user_name}\nName:{name}\nPin:{pin[:3]}{(len_pin-3)*"*"}\nBalance= $00000000\nHistory:N/A"


def access(user_name):
    if user_name in bank.keys():
        for i in range(2,-1,-1):
            pin = input("Enter your pin number: ")
            if bank[user_name]["pin"] == pin:
                return True
            else:
                print(f"Entered wrong password\nTry again.(You have {i}chances left.)")
        print("Access Denied")
        return False
    else:
        print("User name not found.....")
        return False

def check_balance(user_name):
        return float(bank[user_name]["balance"])
    
def check_history(user_name):
    
    history = bank[user_name]["history"]
    history_receipt = f"Name: {bank[user_name]["name"]}\nHistory Receipt:\n"

    for i in history:
        history_receipt += f"{i[0]}: ${i[1]}\n"

    balance = check_balance(user_name)
    history_receipt += f"Total Balance: ${balance}"
    return history_receipt

def withdraw(user_name,amount):
    if amount <= check_balance(user_name):
        bank[user_name]["balance"] -= amount
        bank[user_name]["history"].append(("Withdraw", amount))
        print(f'Money successfully withdrew.Amount: ${amount}\nNew Balance: ${bank[user_name]["balance"]}')
    else:
        print("Insufficient balance")




def deposit(user_name, amount):
    bank[user_name]["balance"] += amount
    bank[user_name]["history"].append(("Deposit", amount))
    print(F'Money successfully deposited.Amount: ${amount}\nNew Balance: ${bank[user_name]["balance"]}')


print("Welcome to  RT Bank......")
print("Here alongside creating a bank account..")
print("You can set password to access you account.....")
print("Also you can check balance and history,withdraw and deposit money from account...")

while True:
    print("\nType[new} to create a new account")
    print("Type[access] to access your account")
    print("Type[q] to quit")

    responese = input()

    if responese == "new":
        UserName = input("Enter your user name: ")
        print(create_account(UserName))
        #create_account(UserName)

    elif responese == "access":
        UserName = input("Enter your user name: ")
        if access(UserName):
            print(f"Welcome {bank[UserName]['name']}")
            while True:
                print("\nType[withdraw] to withdraw money from account")
                print("Type[deposit] to deposit money from account")
                print("Type[history] to check history money from account")
                print("Type[q] to quit")

                action = input()

                if action == "withdraw":
                    Amount = float(input("Enter amount to withdraw: "))
                    withdraw(UserName,Amount)
                elif action == "deposit":
                    Amount = float(input("Enter amount to deposit: "))
                    deposit(UserName,Amount)
                elif action == "history":
                    print(check_history(UserName))
                elif action == "q":
                   break
                else:
                    print("Invalid input. Try again....")
    elif responese == "q":
        break

    elif responese == "admin":
        admin = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if (admin == "wahia_ma'am" or admin == "rt_jeion") and (password == "ads@1234"):
            for account in bank.keys():
               print(bank[account])

    else:
        print("Invalid input. Try again....")
