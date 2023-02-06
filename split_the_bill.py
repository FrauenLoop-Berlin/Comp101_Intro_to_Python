# *Create a Tip calculator 

guest = 2
bill = 80
tip = 10

def tip_calculator(guest,bill,tip):
    total_tip = (bill*(tip/100))
    bill_per_guest = bill/guest
    tip_per_geust = int(total_tip/guest)
    amount_per_guest = int(bill_per_guest + tip_per_geust)

    return f"Each guest needs to pay: {amount_per_guest} euro.The amount of tip for each guest is: {tip_per_geust} euro"

