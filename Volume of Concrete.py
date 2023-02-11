def volumeOfConcrete():
    totalVolume = sum(volumesForBuildings)
    typeOfBuilding = input("Is the Building Residential or Commercial (r "
                           "or c) or if you are finished type x: ").lower()
    while typeOfBuilding not in ("r", "c", "x"):
        typeOfBuilding = input("Is the Building Residential or Commercial (r "
                               "or c) or if you are finished type x: ").lower()
    if typeOfBuilding == "r":
        depth = 0.25
    elif typeOfBuilding == "c":
        depth = 0.5
    else:
        print(f"The total Volume of concrete needed for the buildings is "
              f"{totalVolume} Cubic Metres")
        quit("HAVE A NICE DAY! :  )")
    lengthOfConcrete = int(input("What is the length of concrete needed?: "))
    widthOfConcrete = int(input("What is the Width of concrete needed?: "))
    volume = lengthOfConcrete * widthOfConcrete * depth
    print(f"The volume of the concrete required for the slab with a length of "
          f"{lengthOfConcrete} and a width of {widthOfConcrete} and a depth "
          f"of {depth} is {volume} Cubic Metres")
    volumesForBuildings.append(volume)


volumesForBuildings = []
while True:
    volumeOfConcrete()
