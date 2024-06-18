from flask import Flask,request,jsonify
from flask_cors import CORS
import pymysql
from class_declaration import Users,Products,Cars
import datetime
import uuid
app = Flask(__name__)
CORS(app,origins="http://localhost:5173")

#database
try:
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="usm-store",
        port=3334  # Puerto de la base de datos (opcional)
    )
    print('CONEXIÓN DE BASE DE DATOS')
except Exception as error:
    print("ERROR- COMUNICACIÓN DE BASE DE DATOS",error)

# Registrar rutas aquí
@app.route('/products',methods=['GET'])
def products():
    cursor = db.cursor()
    table_name = "products"
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    products = []
    products_json = []
    for row in results:
        product = Products(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        products.append(product)
        products_json.append(product.print_json())
        print('enajdjnajnsajsnj',product.uid)
    return jsonify(products_json)
# Registrar rutas aquí
@app.route('/users',methods=['GET'])
def users():
    cursor = db.cursor()
    table_name = "users"
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    users = []
    users_json = []
    for row in results:
        user = Users(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        users.append(user)
        users_json.append(user.print_json())
    return jsonify(users_json)
  
@app.route('/cars',methods=['GET'])
def cars():
    cursor = db.cursor()
    table_name = "cars"
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    cars = []
    cars_json = []
    for row in results:
        item = Cars(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        cars.append(item)
        cars_json.append(item.print_json())
        print('enajdjnajnsajsnj',item.uid)
    return jsonify(cars_json)


@app.route('/checkin', methods=['POST'])
def checkin():
  # Recibir datos del formulario JSON
    image= request.json['image']
    nationality = request.json['nationality']
    ci = request.json['ci']
    username = request.json['username']
    name = request.json['name']  
    lastname = request.json['lastname']  
    email = request.json['email']  
    password = request.json['password']  
    admin = 0
    car_id = ''
    uid = nationality + ci
    today = datetime.date.today()
    created_at = today.strftime("%Y-%m-%d")
    update_at = today.strftime("%Y-%m-%d")
    # Preparación de la consulta SQL
    consulta_sql = """
    INSERT INTO users (uid,name,lastname,username,email,admin,password,car_id,image,createdAt,updateAt)
    VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
    """

    # Preparación del cursor y ejecución de la consulta
    cursor = db.cursor()
    cursor.execute(consulta_sql,(uid,name,lastname,username,email,admin,password,car_id,image,created_at,update_at))
    db.commit()
    cursor.close()
  # Procesar datos del formulario (opcional)
  # ...
  # Enviar respuesta a React
    response = {'message': 'Formulario recibido exitosamente!'}
    return jsonify(response), 200
@app.route('/administrator_permissions', methods=['POST'])
def administrator_permissions():
  uid = request.json['uid']
  admin = request.json['admin']
  today = datetime.date.today()
  update_at = today.strftime("%Y-%m-%d")
  consultation = """
  UPDATE users
  SET admin = %s, updateAt = %s
  WHERE uid = %s
  """
  cursor = db.cursor()
  values = (admin, update_at, uid)
  cursor.execute(consultation, values)
  db.commit()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200
@app.route('/users_delete', methods=['POST'])
def users_delete():
  uid = request.json['uid']
  consultation = """
  DELETE FROM users
  WHERE uid = %s
  """
  cursor = db.cursor()
  values = (uid,)
  cursor.execute(consultation, values)
  db.commit()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200
@app.route('/new_administrator', methods=['POST'])
def new_administrator():
  image= request.json['image']
  nationality = request.json['nationality']
  ci = request.json['ci']
  username = request.json['username']
  name = request.json['name']  
  lastname = request.json['lastname']  
  email = request.json['email']  
  password = request.json['password']  
  admin = 1
  car_id = ''
  uid = nationality + ci
  today = datetime.date.today()
  created_at = today.strftime("%Y-%m-%d")
  update_at = today.strftime("%Y-%m-%d")
  consult_sql = """
  INSERT INTO users (uid,name,lastname,username,email,admin,password,car_id,image,createdAt,updateAt)
  VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
  """
  cursor = db.cursor()
  cursor.execute(consult_sql ,(uid,name,lastname,username,email,admin,password,car_id,image,created_at,update_at))
  db.commit()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200
@app.route('/product_new', methods=['POST'])
def product_new():
  uid = uuid.uuid4()
  title = request.json['title']
  description = request.json['description']
  price = request.json['price']
  amount = request.json['amount']
  image= request.json['image']
  today = datetime.date.today()
  created_at = today.strftime("%Y-%m-%d")
  update_at = today.strftime("%Y-%m-%d")
  consult_sql = """
  INSERT INTO products (uid,title,description,price,amount,image,createdAt,updateAt)
  VALUES (%s, %s, %s,%s, %s,%s, %s,%s)
  """
  cursor = db.cursor()
  cursor.execute(consult_sql,(uid,title,description,price,amount,image,created_at,update_at))
  db.commit()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200

@app.route('/product_delete', methods=['POST'])
def product_delete():
  uid = request.json['uid']
  consultation = """
  DELETE FROM products
  WHERE uid = %s
  """
  cursor = db.cursor()
  # Preparar la consulta con los valores a actualizar
  values = (uid,)
  cursor.execute(consultation, values)
  # Confirmar los cambios en la base de datos
  db.commit()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200

@app.route('/buy_car', methods=['POST'])
def buy_car():
  uid = uuid.uuid4()
  uid_product = request.json['uid_product']
  uid_user = request.json['uid_user']
  title = request.json['title']
  description = request.json['description']
  price = request.json['price']
  amount_buy = request.json['amount_buy']
  amount_product = request.json['amount_product']
  image= request.json['image']
  today = datetime.date.today()
  created_at = today.strftime("%Y-%m-%d")
  update_at = today.strftime("%Y-%m-%d")
  consult_sql = """
  INSERT INTO cars (uid,uid_product,uid_user,title,description,price,amount_product,image,createdAt,updateAt)
  VALUES (%s, %s, %s,%s, %s,%s, %s,%s,%s,%s)
  """
  cursor = db.cursor()
  cursor.execute(consult_sql,(uid,uid_product,uid_user,title,description,price,amount_buy,image,created_at,update_at))
  db.commit()
  consult_sql = """
  UPDATE products
  SET amount = %s, updateAt = %s
  WHERE uid = %s
  """
  cursor = db.cursor()
  values = (amount_product, update_at, uid_product)
  cursor.execute(consult_sql, values)
  db.commit()
  cursor.close()
  cursor.close()
  response = {'message': 'Formulario recibido exitosamente!'}
  return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True,port=5000)
