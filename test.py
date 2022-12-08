from flask import Flask, request, Response
from flask_cors import CORS
import json
import mysql.connector
import functions




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
    result = functions.start_screen()
    return result


# continues with what was your name?
@app.route('/screen_name')
def get_name():
    args = request.args
    name = str(args.get('name'))
    check = functions.check_user_name(name)
    if check is True:
        result = 'Make a new account'
    else:
        result = 'Name not available'
    return result

@app.route('/password')
def get_password(uname, pword):
    username = uname
    password = pword
    functions.create_new_user(username, password)
    result = functions.fetch_dialog('newgametutorial' ,'Melon_Dusk')
    return result

if __name__ == '__main__':
   app.run(use_reloader=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
   app.run(use_reloader=True, host='127.0.0.1', port=5000)
