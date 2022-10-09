import functions


# main program

# title:
print("Welcome to the Flight game!")
print("-----------------------------")

# returns a random starting location
starting_point = functions.random_location()

# creates a new user
username_main = str(input("Please enter your username: "))
functions.create_new_user(username_main, starting_point)
print("------------------------------")
print(f"Hello, {username_main}! You'll start your journey at {starting_point}")

# the game chooses 4 random objects player must fetch
find_items = []
find_items = functions.get_and_rand_object()
print(f"List of items you need to find: {find_items}")
inventory = []

# loop through until required objects are collected
while len(inventory) < 4:
    print("***************************")
    print(f"Your inventory: {inventory}")
    print(f"Your co2 is: {functions.fetch_co2(username_main)}")
    print(f"Items you need to find:{find_items}")
    quit = input("You can quit game by pressing Z, continue with enter")
    if quit == "Z":
        break

    print("***************************")

    #  player chooses a continent to travel
    cont_num = functions.where_to_travel()

    # fetches the countries for player and asks for input
    countries = functions.which_country(cont_num)
    while True:
        print()
        print(countries)
        number = int(input("Where do you want to travel? "))
        if number in range(len(countries) + 1):
            break
        else:
            print(f"Incorrect country number. Try again!")

    # converts input number to a country's iso_code
    iso = functions.fly_to_a_country(number, countries)

    # updates location, calculates co2 consumption and updates co2 consumption to the database
    location = functions.find_loc(username_main)
    co2 = functions.calculate_co2(location, iso)
    functions.change_loc(username_main, iso)
    functions.update_co2(username_main, co2)

    # fetches the item from object and if it is in the list. If so, item is added to the inventory
    obj = functions.find_object(iso)
    obj = functions.beautify_object(obj)
    print(f"Congratulations, you found {obj}!")
    if functions.check_list(obj, find_items) == True and obj not in inventory:
        inventory.append(obj)
        print(f"Your inventory has now {len(inventory)} items\n"
              f"{inventory}")
    else:
        print(f"couldn't add {obj} to the list")


# When the player finds all items
if quit != "Z":
    print("Congratulations! You found all of the objects!")
    co2_final = functions.fetch_co2(username_main)
    print(f"Your co2 consumption was: {co2_final}")
    print("************")
    print("LEADERBOARD")
    print("************")
    print("username - co2_consumed")
    leaderboard = functions.leaderboard()
    i = 1
    for item in leaderboard:
        print(f"{i}. {item}")
        i += 1

# If player decides to quit
else:
    print("*************")
    print("* GAME OVER *")
    print("*************")
