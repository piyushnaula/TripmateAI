from tools.flight_tool import search_flights, parse_route

# Test the parse_route fix
test_queries = [
    "Plan a 7 days Thailand trip from India",
    "Plan a 7 days Nepal trip from India",
    "Japan trip from India",
    "from India to Thailand",
    "flights from DAC to BKK",
    "Tokyo vacation from Delhi",
    "Plan a trip to Japan",
]

print("Route Parsing Tests\n")
for q in test_queries:
    dep, arr = parse_route(q)
    print(f"Query: {q!r}")
    print(f"  Departure: {dep}, Arrival: {arr}")
    print()

# Test actual API call for Thailand trip
print("\nAPI Test: Thailand trip from India\n")
result = search_flights("Plan a 7 days Thailand trip from India", limit=5)
print(result)
