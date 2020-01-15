# improved & converted to Python 3

import functions

print("We are going to start by organising the costs around your house.")
print("The amount asked for is per month.")

rent = functions.ask_amount("How much rent/mortgage do you pay? € ")
servicecosts = functions.ask_amount("How much servicecosts do you pay? € ")
total_rent = rent + servicecosts
print(f'The total amount you spend on rent/mortgage and servicecosts is € {total_rent}')

gas_and_electricity = functions.ask_amount("How much do you pay for gas and electricity? € ")
water = functions.ask_amount("How much do you pay for water? € ")
utilities = gas_and_electricity + water
print(f'The total amount you spend on rent and utilities is € {total_rent + utilities}')

tv_and_internet = functions.ask_amount("How much do you pay for tv and internet? € ")
print(f'For tv and internet you pay € {tv_and_internet}')

total = total_rent + utilities + tv_and_internet
print(f'The total amount you spend on your house is {total}')
