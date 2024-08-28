# Task 1: Formatting Flight Itineraries
def format_itineraries(itineraries):
    result = []
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        result.append(f"Itinerary {index}: {traveler_name} - From {origin} to {destination}")
    return "\n".join(result)

# Sample input for Task 1
flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

# Print formatted itineraries
print("Flight Itineraries:")
print(format_itineraries(flight_itineraries))
print()  # Blank line for readability

# Task 2: Library System Enhancement
def add_book(library, new_book):
    if new_book in library:
        print(f"The book {new_book} already exists in the library.")
    else:
        library.append(new_book)
        print(f"Book {new_book} added to the library.")

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding new books for Task 2
add_book(library, ("To Kill a Mockingbird", "Harper Lee"))
add_book(library, ("1984", "George Orwell"))  # Duplicate book

print("Updated Library:")
for book in library:
    print(book)
print()  # Blank line for readability

# Task 3: Customer Order Processing
def process_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Sample order data for Task 3
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # Add more orders if needed
]

# Process and print each order
print("Customer Orders:")
process_orders(orders)
