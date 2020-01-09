from flask import Flask, request
from flask_cors import CORS
# from flaskext.mysql import MySQL
import pyodbc
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# define MySQL configurations
# app.config['MYSQL_DATABASE_HOST'] = 'db'
# app.config['MYSQL_DATABASE_DB'] = 'replacement_handsets_test'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'ccssrelvl11'

# # initialise MySQL
# mysql = MySQL()
# mysql.init_app(app)
# conn = mysql.connect()  # create mysql connection
# cursor = conn.cursor()  # need a cursor to query stored procedure


# define SQL server config
sqlserver = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost; DATABASE=replacement_handsets_test; UID=root; PWD=CCSSRElvl11')

# initialise cursor for SQL server
cursor = sqlserver.cursor()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/api/requesthandsetreplacement", methods=['POST'])
# define method to be performed
def new_order_request():
    response_object = {'status': 'success'}
    json_obj = request.get_json()

    if request.method == 'POST':
        if request.is_json:

            # values from received request
            _siteID = json_obj['siteID']
            _handsetModel = json_obj['handsetModel']
            _partNumber = json_obj['partNumber']
            _faultDesc = json_obj['faultDescription']
            _quantity = json_obj['quantity']
            _contactName = json_obj['contactName']
            _contactNumber = json_obj['contactNumber']
            _contactEmail = json_obj['contactEmail']
            _deliveryAddress = json_obj['deliveryAddress']
            cursor.execute("{CALL new_order(?,?,?,?,?,?,?,?,?)}", (_siteID, _handsetModel, _partNumber, _faultDesc, _quantity, _contactName, _contactNumber, _contactEmail, _deliveryAddress))

            data = cursor.fetchall()

            if len(data) == 0:
                cursor.commit() 
                return 'Order successfully created!'
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return 'Error: No JSON data received.'

    return response_object


if __name__ == '__main__':
    app.run()
