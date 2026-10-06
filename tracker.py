# Laboratory 3 - Installment 3: The Tracker Does Math
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

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * tax_percent / 100

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print(f"Made by: {name}  |  Installment 3")