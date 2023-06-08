'''
Task 16 'Holiday' application that prints destination cities and calculates total holiday cost
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
# Goal: Develop a holiday application that asks user to type destination city 
# and calculates total cost. Functions are used for calculating hotel, flight, 
# car rental, and total cost of holiday.
# Application also gives the user the choice to add a city, if it doesn't exist.

# Defining a 'cities' list containing city names
cities = ['berlin', 'paris', 'new york', 'tokyo', 'dubai', 'barcelona', 
         'rome', 'new delhi', 'mumbai', 'moscow', 'beijing']

# Defining 'hotel price' dictionary, which contains price per night of each city.
hotel_price_night = {cities[0]: 75, cities[1]: 80, cities[2]: 90, cities[3]: 100,
                    cities[4]: 80, cities[5]: 65, cities[6]: 70, cities[7]: 70,
                    cities[8]: 80, cities[9]: 90, cities[10]: 65}

# Defining 'flight cost' dictionary, which contains return flight cost for each city.
flight_cost = {cities[0]: 150, cities[1]: 100, cities[2]: 290, cities[3]: 580, 
              cities[4]: 250, cities[5]: 90, cities[6]: 85, cities[7]: 635, 
              cities[8]: 600, cities[9]: 550, cities[10]: 650}

# Defining 'car price' dictionary, which contains price per day for renting a car in each city.
car_rental_day = {cities[0]: 35, cities[1]: 30, cities[2]: 40, cities[3]: 45, cities[4]: 30,
                 cities[5]: 20, cities[6]: 28, cities[7]: 25, cities[8]: 28, cities[9]: 30,
                 cities[10]: 29}

# Defining a function to print list of cities
def city_list():
    print("\n City List")
    print("--------------")
    for city in range(len(cities)):
        print(cities[city])

# Defining function to calculate hotel cost
def hotel_cost(num_nights, city_flight):
    total_hotel_cost = num_nights * hotel_price_night[city_flight]
    return total_hotel_cost

# Defining function to calculate plane cost
def plane_cost(city_flight):
    total_plane_cost = flight_cost[city_flight]
    return total_plane_cost

# Defining function to calculate car rental
def car_rental(rental_days, city_flight):
    total_car_cost = rental_days * car_rental_day[city_flight]
    return total_car_cost

# Defining function to calculate total holiday cost
def holiday_cost(total_hotel_cost, total_car_cost, total_plane_cost):
    total_holiday_cost = total_hotel_cost + total_car_cost + total_plane_cost
    return total_holiday_cost

try:

    # Function call to print city list
    city_list()
    city_flight = input("\nType the city you want to fly: ")

    # Checks if user input is valid or if user typed 'City' exist in the current 'City' list, 
    # if it doesn't, gives the option to add.
    if city_flight == '':
        raise EOFError

    elif city_flight not in cities:
        user_choice = input("\nFlight to this destination 'City' is not available. " 
                      "Do you want to add this 'City'? Type yes/no: ")
        
        if user_choice.lower() == 'yes':
            print(f"\nYou choose to add a new destination {city_flight.capitalize()}")
            input_hotel_price = int(input("\nType hotel price per night in pounds: "))
            input_flight_fare = int(input("\nType flight fare to the destination in pounds: "))
            input_car_rental = int(input("\nType car price per day in pounds: "))
            cities.append(city_flight)
            hotel_price_night[city_flight] = input_hotel_price
            flight_cost[city_flight] = input_flight_fare
            car_rental_day[city_flight] = input_car_rental
            print(f"\nNew detination City '{city_flight}' has been added to the list.\n")

        else:
            city_list()
            city_flight = input(f"\nPlease choose to add a city from the above list: ")
            pass
        
    num_nights = int(input("\nType the number of nights of hotel stay: "))
    rental_days = int(input("\nType the number of rental days for car hire: "))

    # Calling the defined functions
    total_car_cost = car_rental(rental_days, city_flight)
    total_plane_cost = plane_cost(city_flight)
    total_hotel_cost = hotel_cost(num_nights, city_flight)
    total_holiday_cost = holiday_cost(total_hotel_cost, total_car_cost, total_plane_cost)

    # printing output in refined format
    print ("\n{:<10} {:<10}".format('Total Holiday Cost Summary (£):', city_flight.capitalize()))
    print("----------------------------------------")
    print("{:<15}  {:<10}".format('Hotel stay', total_hotel_cost))
    print("{:<15}   {:<10}".format('Car hire', total_car_cost))
    print("{:<15}  {:<10}".format('Flight cost', total_plane_cost))
    print("----------------------------------------")
    print("{:<15}  {:<10}".format('Total cost', total_holiday_cost), '\n')

except ValueError:
    print("\nValueError: Invalid! input. Please type valid integer value")

except EOFError:
    print("\nEOFError: No input is given. Please type valid string (city)")

finally:
    print("Thanks! for using the app. Happy Holiday!\n")