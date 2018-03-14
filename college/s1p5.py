# WAP to convert distance from centimeter to meter, km, feet, inches.

cen = float(input("Centimeter: "))

meter = cen / 100
km = cen / 100000
feet = meter * 3.28084
inches = cen * 0.3937

print("Meter:", str(meter) + "\n" +
      "KM:", str(km) + "\n" +
      "Feet:", str(feet) + "\n" +
      "Inches:", str(inches) + "\n")
