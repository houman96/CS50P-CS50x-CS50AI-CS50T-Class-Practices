import cs50

while True:
    dollars = cs50.get_float('Change: ')
    if dollars > 0:
        coins = 0

        quarters = int(dollars / 0.25)
        dime = int((dollars % 0.25) / 0.10)
        nickels = int(((dollars % 0.25) % 0.10) / 0.05)
        pennies = int(((dollars % 0.25) % 0.10) % 0.05)

        coins = coins + quarters
        if dime > 0:
            coins = coins + dime
        if nickels > 0:
            coins = coins + nickels
        if pennies > 0:
            coins = coins + pennies

        print(coins)
        break
