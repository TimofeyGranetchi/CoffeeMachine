# Write your code here
class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, number_of_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.number_of_cups = number_of_cups
        self.money = money

    def make_espresso(self):
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.coffee_beans < 16:
            print("Sorry, not enough coffee beans!")
        elif self.number_of_cups == 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.number_of_cups -= 1

    def make_latte(self):
        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < 20:
            print("Sorry, not enough coffee beans!")
        elif self.number_of_cups == 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
            self.number_of_cups -= 1

    def make_cappucino(self):
        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < 12:
            print("Sorry, not enough coffee beans!")
        elif self.number_of_cups == 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.number_of_cups -= 1

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.number_of_cups += int(input())

    def take_money(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def __str__(self):
        return f'''The coffee machine has:
               {self.water} of water
               {self.milk} of milk
               {self.coffee_beans} of coffee beans
               {self.number_of_cups} of disposable cups
               {self.money} of money'''

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        input_ = input()
        if input_ == 'back':
            return
        option = int(input_)
        if option == 1:
            self.make_espresso()
        elif option == 2:
            self.make_latte()
        elif option == 3:
            self.make_cappucino()

    def run(self):
        while True:
            print("Write action (buy, fill, take):")
            action = input()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take_money()
            elif action == 'remaining':
                print(self)
            elif action == 'exit':
                break


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.run()
