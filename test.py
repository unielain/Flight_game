from flask import Flask, request, Response
from flask_cors import CORS
import json
import functions

# main
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content type'



# gets a list of the items that need fetching
@app.route('/list_items')
def list_of_items():
    items = functions.get_and_rand_object()
    return json.dumps(items, default=lambda o: o.__dict__, indent=4)


# gets coordinates
@app.route('/list_locations')
def list_of_locations():
    items = functions.find_locations()
    return json.dumps(items, default=lambda o: o.__dict__, indent=4)

# users start location
@app.route('/random_loc')
def rand_loc():
    locs = functions.random_location()
    airport = functions.airport_name(locs)
    functions.change_loc('sakari', airport)
    return json.dumps(locs, default=lambda o: o.__dict__, indent=4)

# gets the hints for selected objects
@app.route('/get_a_hint')
def hints():
    args = request.args
    items = str(args.get('items'))
    hint = functions.hint_country(items)
    return json.dumps(hint, default=lambda o: o.__dict__, indent=4)


@app.route('/co2_stats')
def getco2():
    result = functions.getco2()
    return json.dumps(result, default=lambda o:o.__dict__, indent=4)


# updates co2 based on travel in map.html
@app.route('/travel')
def travel():
    args = request.args
    lat = float(args.get('lat'))
    lon = float(args.get('lon'))
    degs = [lat, lon]
    name = functions.airport_name(degs)
    airport = functions.find_loc('sakari')
    resp = functions.fly_to_a_country(lat, lon)
    co2consumed = functions.calculate_co2(lat, lon, airport)
    functions.update_co2('sakari', co2consumed)
    functions.change_loc(lat, lon)
    return json.dumps(resp, default=lambda o:o.__dict__, indent=4)

@app.route('/check_item')
def item_checker():
    item = functions.find_object()
    return json.dumps(item, default=lambda o:o.__dict__, indent=4)


# measures the location

if __name__ == '__main__':
   app.run(use_reloader=True, host='127.0.0.1', port=5000)
