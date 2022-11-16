childs_meal = float(input("what is the price of a child's meal? "))
adults_meal = float(input("what is the price of an adult's meal? "))
num_child = int(input("how many children are there? "))
num_adult = int(input("how many adults are there? "))
sales_tax = float(input("what is the sales tax rate? "))

print()
child = childs_meal * num_child
adult = adults_meal * num_adult
subtotal = child + adult
print (f"subtotal: ${subtotal:.2f}")
sales_tax2 = (sales_tax/100) * subtotal
print (f"sales tax: ${sales_tax2:.2f}")
total = subtotal + sales_tax2
print (f"total: ${total:.2f}")
print()

#extension work
import math
payment = math.ceil(total/10) * 10 
print (f"amount owed to the nearest $10: ${payment}")
change = payment - total
print(f"change: ${change:.2f}")