#second half of the tutorial just put here 

spending = float(input("Enter total spending: "))

numberofppl = range(2,5)

for num in numberofppl:
    print(f"{num} people: ${spending/num} each")