from flask import Flask
from flask_mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']="53306"
app.config['MYSQL_DB']="w3schools"
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"

cursor=mysql.connection.cursor()
query='SELECT '
cursor.execute(query)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
