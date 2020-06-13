# Write your code here
water = 400
milk = 540
coffee_beans = 120
number_of_cups = 9
money = 550
print('The coffee machine has:')
print(str(water) + ' of water')
print(str(milk) + ' of milk')
print(str(coffee_beans) + ' of coffee beans')
print(str(number_of_cups) + ' of disposable cups')
print(str(money) + ' of money')
print("Write action (buy, fill, take):")
action = input()
if action == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    option = int(input())
    if option == 1:
        water -= 250
        coffee_beans -= 16
        money += 4
        number_of_cups -= 1
    elif option == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        number_of_cups -= 1
    elif option == 3:
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
print('The coffee machine has:')
print(str(water) + ' of water')
print(str(milk) + ' of milk')
print(str(coffee_beans) + ' of coffee beans')
print(str(number_of_cups) + ' of disposable cups')
print(str(money) + ' of money')
