#!/usr/bin/env python3

# This program determines the distance to a lightning strike.
# based on the time elapsed between the flash and the sound of thunder
# Speed of sound is approximately 1100ft/sec and 1 mile is 5280 ft.
# Or speed -eq 0.20833333333333334 miles per second.
# Distance = Speed * Time

print()
speed = 1100    #ft/sec
time = float(input("Enter time elapsed between flash and thunder: "))
speed_units = input("Enter units of speed(ft/sec, miles/sec): ")
time_units = input("Input units of time(sec, min): ")

distance = speed * time
if time_units == "sec":
    if speed_units == 'ft/sec':
        print(f"The lightning striked {distance} feet "
                "from the ear.")
        print("Lightning is ", distance/5280, "miles away")
    elif speed_units == 'miles/sec':
        distance = (speed/5280) * time
        print(f"The lightning distance is {distance} miles away")
        print("The lightning distance is ", distance*5280, "feet far")
    else:
        print("please input speed in miles/sec or ft/sec.")
        print()
elif time_units == "min":
    if speed_units == 'ft/sec':
        distance = speed * (time*60)
        print(f"The lightning striked {distance} feet "
                "from the ear.")
        print("Lightning is ", distance/5280, "miles away")
    elif speed_units == 'miles/sec':
        distance = (speed/5280) * (time*60)
        print(f"The lightning distance is {distance} miles away")
        print("The lightning distance is ", distance*5280, "feet far")
    else:
        print("please input speed in miles/sec or ft/sec.")
        print()
else:
    print("Please input time in sec or min")
    print()
