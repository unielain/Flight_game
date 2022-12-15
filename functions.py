import json
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
    sql = f"SELECT latitude_deg, longitude_deg, elevation_ft from airport where iso_country in("
    sql += "select iso_country from objects);"
    cursor_location = connection.cursor()
    cursor_location.execute(sql)
    result = cursor_location.fetchall()
    index2 = -1
    for object in result:
        index2 += 1
    random_index = random.randint(1, index2)
    location = result[random_index]
    return location


# finds the locations for map api
def find_locations():
    latitude = []
    lognitude = []
    airports = []
    iso = []
    thewholething = []
    connection = connect_to_database()
    sql = f"SELECT latitude_deg, longitude_deg, name, iso_country from airport where iso_country in("
    sql += "select iso_country from objects);"
    cursor_loc = connection.cursor()
    cursor_loc.execute(sql)
    result = cursor_loc.fetchall()
    if len(result) > 0:
        for row in result:
            if row[3] not in iso:
                latitude.append(row[0])
                lognitude.append(row[1])
                airports.append(row[2])
                iso.append(row[3])
        thewholething =[latitude, lognitude, airports, iso]
        return thewholething
    else:
        return False


def airport_name(degs):
    characters = ["(", ")", ",", "'"]
    connection = connect_to_database()
    sql = f"select name from airport where latitude_deg={degs[0]} and longitude_deg={degs[1]};"
    cursor_get_iso = connection.cursor()
    cursor_get_iso.execute(sql)
    result = cursor_get_iso.fetchall()
    result = result[0]
    result = str(result)
    for character in characters:
        result = result.replace(character,"")
    return result

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


# gives the hints of objects
def hint_country(items):
    connection = connect_to_database()
    sql = f"SELECT hint FROM objects WHERE name='{items}'"
    hints_fetch = connection.cursor()
    hints_fetch.execute(sql)
    hints_get = hints_fetch.fetchall()
    for row in hints_get:
        hint = beautify_object(row)
        with open(hint) as dusk1:
            hint = dusk1.readlines()
    return hint


def fly_to_a_country(lat, lon):
    connection = connect_to_database()
    sql = f"SELECT name FROM airport WHERE latitude_deg='{lat}' AND longitude_deg='{lon}';"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    result = cursor_country.fetchall()
    result = beautify_object(result)
    return result


# WORKING WITH THIS ONE RN, DO NOT TOUCH
def calculate_co2(lat, lon, location):
    connection = connect_to_database()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name='{location}';"
    cursor_country = connection.cursor()
    cursor_country.execute(sql)
    cord1 = cursor_country.fetchall()
    cord2 = [lat, lon]
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


def change_loc(username, airport):
    connection = connect_to_database()
    sql = f'UPDATE game SET location = "{airport}" where screen_name="{username}";'
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



