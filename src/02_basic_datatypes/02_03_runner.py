'''

If a runner runs 10 miles in 30 minites and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''



def convert_miles_to_km(miles):
    return miles*1.6

def convert_minutes_to_hours(minutes):
    return minutes/60

def average_speed(distance,time):
    return distance/time

miles = 10
minutes = 30.5

km=convert_miles_to_km(miles)
hours= convert_minutes_to_hours(minutes)
speed=average_speed(km,hours)

print('Her average speed is ', speed, 'km/h.')