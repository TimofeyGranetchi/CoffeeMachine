# Write your code here
water = 400
milk = 540
coffee_beans = 120
number_of_cups = 9
money = 550

while True:
    print("Write action (buy, fill, take):")
    action = input()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        input_ = input()
        if input_ == 'back':
            continue
        option = int(input_)
        if option == 1:
            if water < 250:
                print("Sorry, not enough water!")
            elif coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif number_of_cups == 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 250
                coffee_beans -= 16
                money += 4
                number_of_cups -= 1
        elif option == 2:
            if water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif number_of_cups == 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -= 75
                coffee_beans -= 20
                money += 7
                number_of_cups -= 1
        elif option == 3:
            if water < 200:
                print("Sorry, not enough water!")
            elif milk < 100:
                print("Sorry, not enough milk!")
            elif coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif number_of_cups == 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                coffee_beans -= 12
                money += 6
                number_of_cups -= 1
    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        water += int(input())
        print("Write how many ml of milk do you want to add:")
        milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        number_of_cups += int(input())
    elif action == "take":
        print("I gave you $" + str(money))
        money = 0
    elif action == 'remaining':
        print('The coffee machine has:')
        print(str(water) + ' of water')
        print(str(milk) + ' of milk')
        print(str(coffee_beans) + ' of coffee beans')
        print(str(number_of_cups) + ' of disposable cups')
        print(str(money) + ' of money')
    elif action == 'exit':
        break
