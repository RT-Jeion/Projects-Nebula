bank = {
    "rt_jeion":{
        "name":"",
        "pin":"",
        "balance":0000,
        "history":[]
    }
}

def create_account(user_name):
    if user_name in bank.keys():
        return "user_name already exists.."
    
    name = input("Enter You full name: ")
    bank[user_name]["name"] = name
    while True:
        pin = input("Enter your pin (minimum 8 digit): ")
        bank[user_name]["pin"] = pin

        len_pin = len(pin)
        if len_pin >= 8:
            print("Pin created successfully.")
            break
        else:
            print("Input Pin is less than 8 digit...")
        
        bank[user_name]["balance"] = 0
        bank[user_name]["history"] = []

    return f"Account successfully Created.\nUser name:{user_name}\nName:{name}\nPin:{pin[":3"]}{(len_pin-3)*"*"}\nBalance= $00000000\nHistory:N/A"


def access(user_name, pin):
    if user_name in bank.keys():
        for i in range(2,-1,-1):
            if bank[user_name]["pin"] == pin:
                return True
            else:
                print("Entered wrong password\nTry again.(You have {i}chances left.)")
        return False
    return False

def check_balance(user_name):
        return {bank[user_name]["balance"]}
    
def check_history(user_name):
    
    history = bank[user_name]["history"]
    history_recipt = "History Recipt:\n"

    for i in history:
        history_recipt += f"{i[0]: ${i[1]}}\n"

    balance = check_balance(user_name)
    history_recipt += f"Total Balance: ${balance}"
    return history_recipt

def withdraw(user_name,amount):
    if amount <= check_balance(user_name):



def deposit(user_name, amount):
    pass


print("Welcome to  RT Bank......")
print("Here alongside creating a bank acocunt..")      
print("You can set password to access you account.")
print("Also you can check balance, check withdraw and deposit history, and modify your account...")
