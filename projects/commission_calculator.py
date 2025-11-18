# Calculate comission to be paid to employees based on their sales
# Comission is 13% of the total $$$ sold
# Code should ask for the name of the employee and how much $$$ have they sold
# Code should output a phrase stating the employee name and how much $$$ they'll get paid

name = input("What is your name? ")
sales = float(input("How much money did you sold? "))
percentage = 0.13
commission = round(sales * percentage,2)
print(f"\nHi {name}!"
      f"\nYou sold ${sales}."
      f"\nExcellent!"
      f"\nYou'll get a {int(percentage * 100)}% in comissions over the total amount sold."
      f"\nThat would be ${commission}!")