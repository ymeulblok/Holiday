def hotel_cost(num_nights, hotel_star):
    """
    Calculate the total cost of hotel accommodation based on the number of nights and hotel star rating.

    Parameters:
    - num_nights (int): The number of nights of stay.
    - hotel_star (int): The star rating of the hotel (3, 4, or 5).

    Returns:
    - float: The total cost of hotel accommodation.
    """
    if not isinstance(num_nights, int) or not isinstance(hotel_star, int):
        raise ValueError("Number of nights and hotel star rating must be integers.")
    if num_nights <= 0 or hotel_star not in [3, 4, 5]:
        raise ValueError("Number of nights must be a positive integer and hotel star rating must be 3, 4, or 5.")
    
    # Define hotel costs per night based on star rating
    if hotel_star == 3:
        return num_nights * 80  # Assuming £80 per night for 3-star hotel
    elif hotel_star == 4:
        return num_nights * 120  # Assuming £120 per night for 4-star hotel
    elif hotel_star == 5:
        return num_nights * 200  # Assuming £200 per night for 5-star hotel
    else:
        return 0  # If star rating not found

def plane_cost(city_flight, class_type):
    """
    Calculate the cost of the flight based on the destination city and class type.

    Parameters:
    - city_flight (str): The destination city (Amsterdam, Paris, Rome, or New York).
    - class_type (str): The class type of the flight (economy or business).

    Returns:
    - float: The cost of the flight.
    """
    if city_flight not in ["Amsterdam", "Paris", "Rome", "New York"] or class_type not in ["economy", "business"]:
        raise ValueError("Invalid destination city or class type.")
    
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
    """
    Calculate the total cost of car rental based on the number of rental days.

    Parameters:
    - rental_days (int): The number of days for which the car is rented.

    Returns:
    - float: The total cost of car rental.
    """
    if not isinstance(rental_days, int) or rental_days <= 0:
        raise ValueError("Number of rental days must be a positive integer.")
    
    # Assuming daily car rental cost is £75
    return rental_days * 75

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """
    Calculate the total cost of the holiday based on hotel, flight, and car rental costs.

    Parameters:
    - hotel_cost (float): The total cost of hotel accommodation.
    - plane_cost (float): The cost of the flight.
    - car_rental (float): The total cost of car rental.

    Returns:
    - float: The overall cost of the holiday.
    """
    return hotel_cost + plane_cost + car_rental

try:
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
    print(f"Hotel Cost: £{hotel_total}")  # Assuming £ for hotel costs
    print(f"Flight Cost: £{plane_total}")  # Assuming £ for flight costs
    print(f"Car Rental Cost: £{car_total}")  # Assuming £ for car rental costs
    print(f"Total Holiday Cost: £{total_cost}")  # Assuming £ for total holiday cost
except ValueError as e:
    print(f"Error: {e}")