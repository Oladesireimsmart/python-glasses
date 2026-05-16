unit=int(input("Enter the number of units consumed:     "))

if unit<50:
    amount= unit*2.60+25

elif unit>=50& unit<=100:
    amount= unit*3.25+35

elif unit>100 & unit<=200:
    amount= unit*5.26+45

else:
    amount= unit*8.45+75

print("Electricity bill is:     ",amount)