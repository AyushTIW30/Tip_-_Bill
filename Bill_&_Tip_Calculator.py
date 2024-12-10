def calculate_tip():

    print("******************************************")
    print("        Welcome to the Tip Calculator!    ")
    print("******************************************\n")

    while True:
        try:
            total_bill = float(input("What was the total bill? $"))
            if total_bill <= 0:
                print("The bill amount must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            tip_percentage = int(input("What percentage tip would you like to give? (Choose 10, 12, or 15): "))
            if tip_percentage not in [10, 12, 15]:
                print("Please choose either 10, 12, or 15 for the tip percentage.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number (10, 12, or 15).")

    while True:
        try:
            num_people = int(input("How many people would you like to split the bill among? "))
            if num_people <= 0:
                print("The number of people must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of people.")

    tip_amount = (tip_percentage / 100) * total_bill


    total_with_tip = total_bill + tip_amount


    amount_per_person = total_with_tip / num_people

    print("\n******************************************")
    print("             Bill Breakdown                ")
    print("******************************************")
    print(f"Total bill (before tip):  ${total_bill:.2f}")
    print(f"Tip percentage:           {tip_percentage}%")
    print(f"Total tip amount:        ${tip_amount:.2f}")
    print(f"Total bill with tip:     ${total_with_tip:.2f}")
    print(f"Number of people:        {num_people}")
    print(f"Amount per person:       ${amount_per_person:.2f}")
    print("\n******************************************")

calculate_tip()
