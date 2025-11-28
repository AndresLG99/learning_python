names = ["Ana","Hugo","Valeria"]
ages = [65,29,42]
cities = ["Lima","Madrid","Mexico"]

combined = list(zip(names, ages, cities))
print(combined)

for name, age, city in combined:
    print(f"{name} is {age} years old and lives in {city}")