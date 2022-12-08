from flask import Flask, request, Response
from flask_cors import CORS
import json
import mysql.connector
import functions



# main
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content type'


# game starts:
@app.route('/startgame')
def startgame():
    result = functions.fetch_dialog('startscreen', 'Melon_Dusk')
    return result


@app.route('/screen_name')
def get_name():
    args = request.args
    name = str(args.get('name'))
    check = functions.check_user_name(name)
    if check is True:
        result = functions.fetch_dialog('newgamepassword', 'Melon_Dusk')
    else:
        result = functions.fetch_dialog('same_screen_name', 'Melon_Dusk')
    return result


@app.route('/new_password')
def create_password():
    args = request.args
    password = str(args.get('password'))
    name = str(args.get('name'))
    result = functions.fetch_dialog('newgametutorial', 'Melon_Dusk')
    functions.create_new_user(name, password)
    return result


# gets a list of the items that need fetching
@app.route('/list_items')
def list_of_items():
    items = functions.get_and_rand_object()
    return json.dumps(items, default=lambda o: o.__dict__, indent=4)

@app.route('/list_locations')
def list_of_locations():
    items = functions.list_of_lat_long('latitude_deg', 'longitude_deg')
    return json.dumps(items, default=lambda o: o.__dict__, indent=4)


@app.route('/random_loc')
def rand_loc():
    locs = functions.random_location()
    return json.dumps(locs, default=lambda o: o.__dict__, ident=4)

if __name__ == '__main__':
   app.run(use_reloader=True, host='127.0.0.1', port=5000)
