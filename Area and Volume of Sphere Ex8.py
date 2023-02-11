import math
radiusOfSphere = float(input("What is the radius of the Sphere? "))
print(f"A Sphere with a radius of {radiusOfSphere} units has a volume of "
      f"{4/3 * math.pi * radiusOfSphere**3:.3f} Cubic Units\nAlso a surface "
      f"area of {4 * math.pi * radiusOfSphere**2:.3f} Square Units")
