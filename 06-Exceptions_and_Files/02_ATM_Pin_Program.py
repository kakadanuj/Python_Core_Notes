# Practice: ATM PIN program with three attempts

correct_pin = 1234

for attempt in range(3):
    try:
        pin = int(input("Enter your ATM PIN: "))
    except ValueError:
        print("Please enter a valid PIN")
        continue

    if pin == correct_pin:
        print("Access granted")
        break
    print("Wrong PIN. Try again")
else:
    # for-else runs only when the loop finishes without break
    print("Your card is blocked")
