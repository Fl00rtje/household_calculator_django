# improved & converted to Python 3
# I think it can be further improved

import functions

car = functions.yes_or_no("Do you own a car?")

def cost_parking_permit():
    amount = 0
    if functions.yes_or_no("Do you pay for a parking permit?"):
        amount = functions.ask_amount("How much do you pay for your parking permit? € ")
    return amount

def cost_road_assistance():
    amount = 0
    if functions.yes_or_no("Do you pay for road assistance?"):
        amount = functions.ask_amount("How much do you pay for road assistance? € ")
    return amount

if car:
    insurance = functions.ask_amount("How much do you pay for insurance? € ")
    roadtaxes = functions.ask_amount("How much do you pay for road taxes? € ")
    parking_permit = cost_parking_permit()
    road_assistance = cost_road_assistance()

    total_car = insurance + roadtaxes + parking_permit + road_assistance
    print(f'The total amount you are spending on your car is € {total_car}')
else:
    print("Thank you for saving the planet!")