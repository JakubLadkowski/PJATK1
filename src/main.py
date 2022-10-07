print("...:::Prosty Kalkulator:::...")

x = int(input("Pierwsza cyfra:"))
y = int(input("Druga cyfra:"))
z = input("Co chcesz zrobic?(+,-,*,/,**)")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("Error: )")
