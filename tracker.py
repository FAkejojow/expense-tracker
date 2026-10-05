# Laboratory 2 - Installment 2: Talking to the User
# Author: JUSTINE JOREL JAYAG CARMEN

print("=" * 40)
print(f"{'EXPENSE TRACKER':>27}")
print(f"{'Know where your money goes.':>35}")
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"{f'  - {item1}:':<16}${amount1}")
print(f"{f'  - {item2}:':<16}${amount2}")
print(f"{'Total spent:':<16}${total}")
print(f"{'Average:':<16}${average}")
print("-" * 40)

print(f"Made by: {name}  |  Installment 2")