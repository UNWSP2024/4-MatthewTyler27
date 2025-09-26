#Matthew Tyler
#09/26/2025
#Budget analysis

def main():
    budget = 0.0
    difference = 0.0
    total = 0.0

    print("This program will help you keep track of your monthly budget")
    budget = float(input("what was your budget for the month?"))
    
    while True: 
        expenses = float(input('Enter each expense or "0" when finished'))
        if expenses == 0:
            break
        total += expenses

    
    print("You spent a total of: ", format(total, ".2f"))

    
    if total > budget:
        difference = total - budget
        print("You are over budget by $", format(difference, ".2f"))
    elif total < budget:
        difference = budget - total
        print("You made your budget by $", format(difference, ".2f"))
    else:
        print("You are exactly on budget, well done!")


if __name__ == '__main__':
    main()
