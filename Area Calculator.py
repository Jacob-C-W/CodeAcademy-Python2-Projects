# Calculator
# Calculate area of shapes
# Print area of shapes to user

print "Calculator is Running"

print "what shape do you need the area for?"
name = raw_input("Type C for Circle or T for Triangle")
if name == "C":
  radius = float(raw_input("Enter the radius"))
  area = 3.14159 * radius ** 2
  print ("Your area is %s" % (area))
elif name == "T":
  base = float(raw_input("Enter the base"))
  hieght = float(raw_input("Enter the hieght"))
  area = (0.5 * base * hieght)
  print ("Your area is %s" % (area))
else: 
  print "invaild"

print "Exiting..."
