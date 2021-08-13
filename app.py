weight = 4.8
cost = 0
premium = 125.00
print("Ground Shipping premium cost: ", premium)
#ground shipping
if weight <= 2:
  cost = (weight*1.5) + 20
  print("Ground Shipping cost: ",cost)
elif weight >2 and weight <= 6:
  cost = (weight*3) + 20
  print("Ground Shipping cost: ",cost)
elif weight >6 and weight <= 10:
  cost = (weight*4) + 20
  print("Ground Shipping cost: ",cost)
else:
  cost = (weight*4.75) + 20
  print("Ground Shipping cost: ",cost)

#drone shiping
if weight <= 2:
  cost = (weight*4.5) 
  print("Drone Shipping cost: ",cost)
elif weight >2 and weight <= 6:
  cost = (weight*9) 
  print("Drone Shipping cost: ",cost)
elif weight >6 and weight <= 10:
  cost = (weight*12)
  print("Drone Shipping cost: ",cost)
else:
  cost = (weight*14.25) 
  print("Drone Shipping cost: ",cost)