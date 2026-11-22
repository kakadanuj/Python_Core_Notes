# Practice: a simple movie ticket booking program using conditions

print("========= PVR =========")

age = int(input("Enter your age: "))

if age <= 18:
    print("Not eligible to watch this movie")
else:
    print("Eligible to watch the movie")

    print("""
Select your seating plan:
    1. Row 1       : 1000
    2. Row 2       : 500
    3. Last Row    : 250
""")

    seat_plan = {1: ("Row 1", 1000), 2: ("Row 2", 500), 3: ("Last Row", 250)}
    choice = int(input("Enter your choice: "))

    if choice in seat_plan:
        row, cost = seat_plan[choice]
        print(f"Your {row} seat is booked. Amount: {cost}")
        print("Your ticket is successfully booked.")
        print("Thank you for booking at PVR")
    else:
        print("Invalid choice")
