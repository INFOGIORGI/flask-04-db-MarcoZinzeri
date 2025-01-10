from flask import Flask
from flask_mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']="53306"
app.config['MYSQL_DB']="w3schools"
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"

mysql = MySQL(app)

@app.route("/")
def users():
    #il cursore è un interfaccia che collega ai database
    cur = mysql.connection.cursor()
    query="select * from products "
    cur.execute(query)
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
app.run(debug=True)
