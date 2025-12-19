# Dictionary with fake data (string fake data)
Data = {
    "location": ["Hyderabad", "Vijayawada", "Wanaparthy"],
    "person": ["Asha", "Deepika", "Sravani"],
    "organization": ["Google", "Microsoft", "Amazon"]
}

# Print the whole dictionary
print("Complete Data Dictionary:")
print(Data)
print("\n")

# Print each category nicely
for key, values in Data.items():
    print(f"{key.title()}:")
    for value in values:
        print(f" - {value}")
    print()

# Example: Search for a value
search_value = "Google"
found = False
for key, values in Data.items():
    if search_value in values:
        print(f"'{search_value}' found in '{key}' category.")
        found = True
        break

if not found:
    print(f"'{search_value}' not found in the dictionary.")
