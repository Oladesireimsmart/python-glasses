def total_calc(bill_aunt,_tip_perc):
    total = bill_aunt*(1+_tip_perc/100)
    total = round(total,2)
    total = round(total,2)
    print(f"The total bill including tip is: ${total}")


total_calc(100,15)