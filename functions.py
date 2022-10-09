import random
import mysql.connector
from geopy import distance


# connects to the db
def connect_to_database():
    # Connection to database
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game2',
        user='root',
        password='m4*Rv1n42',
        autocommit=True
    )
    return connection


# gets a starting location
def random_location():

    connection = connect_to_database()
    sql = "SELECT name FROM country;"
    cursor_location = connection.cursor()
    cursor_location.execute(sql)
    result = cursor_location.fetchall()
    index2 = -1
    for object in result:
        index2 += 1
    random_index = random.randint(1, index2)
    location = result[random_index]
    location = beautify_object(location)
    for char in location[3:]:
        if char.isupper():
            index2 = location.find(char)
            location1 = location[0:index2]
            location2 = location[index2:]
            location = f"{location1} {location2}"
    return location


# check if user in db already
def check_user_name(username):
    connection = connect_to_database()
    sql = f"SELECT screen_name FROM game WHERE screen_name='{username}';"
    cursor_check = connection.cursor()
    cursor_check.execute(sql)
    result = cursor_check.fetchall()
    if len(result) > 0:
        sql = f"DELETE FROM game where screen_name='{username}';"
        cursor_del = connection.cursor()
        cursor_del.execute(sql)
    return True


# creates user
def create_new_user(username, location):
    connection = connect_to_database()
    check_user_name(username)
    sql = f"INSERT INTO game(Co2_consumed, co2_budget, location, screen_name) "
    sql += f"VALUES (0, 0, '{location}', '{username}');"
    cursor_create_new_user = connection.cursor()
    cursor_create_new_user.execute(sql)
    return True


# gets object for player to search
def get_and_rand_object():
    connection = connect_to_database()
    indexes = []
    i = 0
    sql = f"SELECT name FROM objects;"
    cursor_is_obj = connection.cursor()
    cursor_is_obj.execute(sql)
    result = cursor_is_obj.fetchall()
    index_for_random = len(result) - 1

    while i < 8:
        index = random.randint(0, index_for_random)
        if index not in indexes:
            indexes.append(index)
            i += 1

    sql = f"SELECT name FROM objects;"
    cursor_is_obj = connection.cursor()
    cursor_is_obj.execute(sql)
    result = cursor_is_obj.fetchall()
    objects_list = []

    for num in indexes:
        stuff_to_find = result[num]
        stuff_to_find = beautify_object(stuff_to_find)
        if stuff_to_find not in objects_list:
            objects_list.append(stuff_to_find)
        if len(objects_list) == 4:
            break
    return objects_list


# gives the user a choice for country
def where_to_travel():
    while True:
        print("Where do you want to travel?")
        print("Choose a continent:")
        print("1: Europe, 2: Africa 3: North-America, 4: South-America, 5: Oceania, 6: Asia, 7: Antarctica")
        continent = int(input("Give a number of the continent: "))
        if continent in range(1, 8):
            return continent
            break
        else:
            print(f"Incorrect continent number! Try again.")


def which_country(cont):
    continents = ["EU","AF", "NA", "SA", "OC", "AS", "AN"]
    index = cont - 1
    for item in continents:
        if continents[index] == item:
                continent = item
    connection = connect_to_database()
    sql = f"SELECT country.name FROM country, objects WHERE country.continent='{continent}' and country.iso_country = objects.iso_country;"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    result = cursor_country.fetchall()
    countries = []
    i = 1
    for country in result:
        option = beautify_object(country)
        str_country = f"{i}. {option}"
        countries.append(str_country)
        i += 1
    return countries


def fly_to_a_country(country_num, countries):
    index = country_num - 1
    for item in countries:
        if item == countries[index]:
            country = item[3:]
            for char in country[3:]:
                if char.isupper():
                    index = country.find(char)
                    country1 = country[0:index]
                    country2 = country[index:]
                    country = f"{country1} {country2}"
            if country[0] == " ":
                country = country[1:]
    connection = connect_to_database()
    sql = f"SELECT iso_country FROM country WHERE name='{country}';"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    result = cursor_country.fetchall()
    result = beautify_object(result)
    return result


def calculate_co2(location, country):
    connection = connect_to_database()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE iso_country='{location}';"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    cord1 = cursor_country.fetchall()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE iso_country='{country}';"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    cord2 = cursor_country.fetchall()
    distance_km = distance.distance(cord1[0:1], cord2[0:1]).km
    result = 3.16 * distance_km
    return result


def update_co2(username, co2):
    co2 = float(co2)
    connection = connect_to_database()
    sql = f"SELECT co2_consumed FROM game WHERE screen_name='{username}';"
    cursor_find = connection.cursor()
    cursor_find.execute(sql)
    prev_co2 = cursor_find.fetchall()
    prev_co2 = beautify_object(prev_co2)
    new_co2 = float(prev_co2) + co2
    sql = f"UPDATE game SET co2_consumed = {new_co2} WHERE screen_name='{username}';"
    cursor_co2 = connection.cursor()
    cursor_co2.execute(sql)
    return True


def find_loc(username):
    connection = connect_to_database()
    sql = f"SELECT location FROM game WHERE screen_name='{username}';"
    cursor_userdata = connection.cursor()
    cursor_userdata.execute(sql)
    result = cursor_userdata.fetchall()
    result = beautify_object(result)
    return result


def change_loc(username, country):
    connection = connect_to_database()
    sql = f"UPDATE game SET location = '{country}' where screen_name='{username}';"
    cursor_loc = connection.cursor()
    cursor_loc.execute(sql)
    return True


# searches the country and object from database
def find_object(iso_country):
    connection = connect_to_database()
    sql = f"SELECT name FROM objects where iso_country='{iso_country}';"
    cursor_location = connection.cursor()
    cursor_location.execute(sql)
    result = cursor_location.fetchall()
    return result


# make an object to a string
def beautify_object(object_func):
    object_func = str(object_func)
    object_func = object_func.replace(",", "")
    object_func = object_func.replace(" ", "")
    object_func = object_func.replace("'", "")
    object_func = object_func.replace("(", "")
    object_func = object_func.replace(")", "")
    object_func = object_func.replace("[", "")
    object_func = object_func.replace("]", "")
    return object_func


# check if item in the list
def check_list(item_found, objects_to_find):
    inventory_func = []
    if item_found in objects_to_find:
        return True
    else:
        return False


# to limit spaghetti, a function that checks the object found
def search_object_from(obj_func, iso_code_func, find_items_func, inventory_func):
    obj_func = find_object(iso_code_func)
    obj_func = beautify_object(obj_func)
    print(f"Congratulations, you found {obj_func}!")

    if check_list(obj_func, find_items_func) == True and obj_func not in inventory_func:
        inventory_func.append(obj_func)
        print(f"Your inventory has now {len(inventory_func)} items\n"
              f"{inventory_func}")
        print(f"objects you must find:{find_items_func}")
    else:
        print(f"couldn't add {obj_func} to the list")
        print(f"objects you must find:{find_items_func}")


def fetch_co2(username):
    connection = connect_to_database()
    sql = f"SELECT co2_consumed FROM game WHERE screen_name='{username}';"
    cursor_co2 = connection.cursor()
    cursor_co2.execute(sql)
    result = cursor_co2.fetchall()
    return result


def leaderboard():
    connection = connect_to_database()
    sql = f"SELECT screen_name, co2_consumed FROM game ORDER BY co2_consumed;"
    cursor_lead = connection.cursor()
    cursor_lead.execute(sql)
    result = cursor_lead.fetchall()
    board = []
    for stuff in result:
        board.append(stuff)
    return board