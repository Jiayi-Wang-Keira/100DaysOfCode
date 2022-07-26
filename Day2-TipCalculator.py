bill = float(input("What was the total bill?"))
per = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

output = (bill*(1+per/100))/people
print(f"Each person should pay: {output:.2f}")
