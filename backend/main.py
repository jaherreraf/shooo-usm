from flask import Flask

app = Flask(__name__)

# Registrar rutas aquí
@app.route('/users',methods=['GET'])
def users():
    return 'users'

if __name__ == "__main__":
    app.run(debug=True)
