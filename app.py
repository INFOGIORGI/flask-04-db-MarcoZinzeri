from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']="53306"
app.config['MYSQL_DB']="w3schools"
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"

mysql = MySQL(app)
# Simulazione dei dati del database
mock_products = [
    (1, "Product A", 1, 1, "10 boxes", 20.5),
    (2, "Product B", 2, 2, "5 boxes", 15.0),
    (3, "Product C", 3, 1, "20 boxes", 7.8),
]

mock_categories = [
    (1, "Category A", "Description A"),
    (2, "Category B", "Description B"),
]
@app.route("/")
def homepage():
    return render_template("home.html", titolo="Home")

@app.route("/products")
def products():
    #Creazione cursore e interrogazione al Database
    #cursor = mysql.connection.cursor()
    #query = "SELECT * FROM products"
    #Il cursore esegue la query
    #cursor.execute(query)

    #Il risultato della query viene memorizzato in una tupla di tuple chiamata dati
    #dati = cursor.fetchall()
    #cursor.close()
    dati = mock_products
    return render_template("products.html", titolo="Products", dati=dati)


@app.route("/categories/<int:categoryID>")  #devo castare ad int il categoryID della route
def categories(categoryID):
    #Creazione cursore e interrogazione al Database
   # cursor = mysql.connection.cursor()
   # query = "SELECT * FROM categories WHERE CategoryID = %s"
    
    #Il cursore esegue la query
    #cursor.execute(query)

    #Il risultato della query viene memorizzato in una tupla di tuple chiamata dati
    #dati = cursor.fetchall()
    
    #l=[]
    #for i in dati:
     #   if int(i[0]) == categoryID:
    #        l.append(i)
    # Filtra i dati mock
    l = [c for c in mock_categories if c[0] == categoryID]

    #cursor.close()
    return render_template("category.html", titolo="Categories", categoryID=categoryID, l=l)

if __name__ == '__main__': 
    app.run(debug=True)