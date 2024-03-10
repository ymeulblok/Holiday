def hotel_cost(num_nights, hotel_star):
    # Define hotel costs per night based on star rating
    if hotel_star == 3:
        return num_nights * 75  # Assuming £80 per night for 3-star hotel
    elif hotel_star == 4:
        return num_nights * 125  # Assuming £120 per night for 4-star hotel
    elif hotel_star == 5:
        return num_nights * 200  # Assuming £200 per night for 5-star hotel
    else:
        return 0  # If star rating not found

def plane_cost(city_flight, class_type):
    # Define flight costs for different cities and class types
    if class_type == "economy":
        if city_flight == "Amsterdam":
            return 100
        elif city_flight == "Paris":
            return 150
        elif city_flight == "Rome":
            return 350
        elif city_flight == "New York":
            return 750
    elif class_type == "business":
        if city_flight == "Amsterdam":
            return 200
        elif city_flight == "Paris":
            return 275
        elif city_flight == "Rome":
            return 600
        elif city_flight == "New York":
            return 1600
    return 0  # If city or class not found

def car_rental(rental_days):
    # Assuming daily car rental cost is £75
    return rental_days * 75

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Get user inputs
city_flight = input("Enter the city you will be flying to (options: Amsterdam, Paris, Rome, New York): ")
class_type = input("Enter class type (options: economy, business): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
hotel_star = int(input("Enter the star rating of the hotel (options: 3, 4, 5): "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate costs
hotel_total = hotel_cost(num_nights, hotel_star)
plane_total = plane_cost(city_flight, class_type)
car_total = car_rental(rental_days)
total_cost = holiday_cost(hotel_total, plane_total, car_total)

# Print details
print("\nHoliday Details:")
print(f"Destination: {city_flight}")
print(f"Class Type: {class_type.capitalize()}")
print(f"Hotel Rating: {hotel_star} stars")
print(f"Hotel Cost: ${hotel_total}")
print(f"Flight Cost: ${plane_total}")
print(f"Car Rental Cost: ${car_total}")
print(f"Total Holiday Cost: ${total_cost}")