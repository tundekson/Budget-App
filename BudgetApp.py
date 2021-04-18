class Budget:
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance
        print(f"\nWelcome to {category}, Your balance is N{balance}\n")

    def deposit(self):
        deposit_amount = float(input("\nEnter amount to deposit >> :"))
        self.balance += deposit_amount
        print(f"\nYour deposit of N{deposit_amount} was suucessful")

    def check_balace(self):
        print(f"Your balance = N{self.balance}")

    def withdraw(self):
        withdraw_amount = float(input("\nEnter amount to withdraw >> :"))
        self.balance -= withdraw_amount
        print(f"Your withdrawal of N{withdraw_amount} was suucessful")

    def transfer(self, categ):
        transBalance = float(
            input("\nEnter amount to Transfer to selected category >> :"))
        self.balance -= transBalance
        print(f"Your Transfer of N{transBalance} to {categ} was suucessful")


def action():
    print("\nAvailable Function to perfom")
    print("*" * 16)
    print("1: CHECK BALANCE")
    print("2: WITHDRAWAL")
    print("3: DEPOSIT")
    print("4: TRANSFER")

    per_action = int(input("\nChoose action to perform >>: "))

    if per_action == 1:
        print("Check Balance selected")

    elif per_action == 2:
        print("Withdrawal selected")

    elif per_action == 3:
        print("Deposit selected")

    elif per_action == 4:
        print("Transfer selected")

    else:
        print("\nInvalid selection")
    return per_action


def select_Transfer():
    print("*" * 16)
    print("1: FOOD")
    print("2: CLOTHING")
    print("3: ENTERTAINMENT")

    trans = int(input("\nSelect category to make Transfer to >>: "))

    if trans == 1:
        return "Food Category"

    elif trans == 2:
        return "Clothing Category"

    elif trans == 3:
        return "Entertainment Category"

    else:
        print("\nInvalid selection")


food_budget_balance = 15000
clothing_budget_balance = 40000
entertainment_budget_balance = 10000

print("\nAvailable categories")
print("*" * 16)
print("1: FOOD CATEGORY")
print("2: CLOTHING CATEGORY")
print("3: ENTERTAINMENT CATEGORY")
catergory = int(input("\nSelect a category number from the list above >> : "))


if catergory == 1:
    food_category = Budget("Food Category", food_budget_balance)
    option_select = action()
    if option_select == 1:
        food_category.check_balace()
    elif option_select == 2:
        food_category.withdraw()
    elif option_select == 3:
        food_category.deposit()
    elif option_select == 4:
        food_category.transfer(select_Transfer())
    else:
        print("Wrong selection")

elif catergory == 2:
    clothing_category = Budget("Clothing Category", clothing_budget_balance)
    option_select = action()
    if option_select == 1:
        clothing_category.check_balace()
    elif option_select == 2:
        clothing_category.withdraw()
    elif option_select == 3:
        clothing_category.deposit()
    elif option_select == 4:
        clothing_category.transfer()
    else:
        print("Wrong selection")

elif catergory == 3:
    entertainment_category = Budget(
        "Entertainment Category", entertainment_budget_balance)
    option_select = action()
    if option_select == 1:
        entertainment_category.check_balace()
    elif option_select == 2:
        entertainment_category.withdraw()
    elif option_select == 3:
        entertainment_category.deposit()
    elif option_select == 4:
        entertainment_category.transfer()
    else:
        print("Wrong selection")

else:
    print("\nInvalid Category selected")


#option_select = action()
