series = "N-02"

if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("Doesn't exist")

match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Doesn't exist")

customer = {"name":"Federico",
            "age":45,
            "profession":"instructor"}

movie = {"title":"Matrix",
         "description":{"star":"Keanu Reeves",
                        "director":"Lana and Lilly Wachowski"}}

elements = [customer, movie, "book"]

for e in elements:
    match e:
        case {"name":name,
              "age":age,
              "profession":profession}:
            print("This is a customer")
            print(f"{name} is {age} years old and is a {profession}")
            print()
        case {"title":title,
              "description":{"star":star,
                             "director":director}}:
            print("This is a movie")
            print(f"The star for {title} is {star} and the director is {director}")
            print()
        case _:
            print("I don't know what this is")