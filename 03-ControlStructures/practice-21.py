amount = int(input("Enter the amount in PLN: "))

coin_5 = amount // 5
coin_2 = (amount - coin_5 * 5 ) // 2
coin_1 = amount - coin_2 * 2 - coin_5 * 5

print("5 PLN coins:", coin_5)
print("2 PLN coins:", coin_2)
print("1 PLN coins:", coin_1)