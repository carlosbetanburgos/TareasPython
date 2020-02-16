from flask import Flask, render_template, request, jsonify
from flask_api import status
import configparser
import psycopg2

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('based.ini')
cnx=psycopg2.connect(dbname=config['DB']['name'], user=config['DB']['user'], password=config['DB']['password'], host=config['DB']['host'], port=config['DB']['port'])
cur=cnx.cursor()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/v2/provincias',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia;")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/provincia/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia WHERE codigo=%s;",(codigo,))
        provincia=cur.fetchone()
        if provincia is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/cantones',methods=['POST', 'GET', 'DELETE', 'PUT'])
def cantones():
    if request.method == 'GET':
        cur.execute("SELECT provincia.nombre, canton.codigo, canton.nombre FROM canton, provincia WHERE canton.provincia = provincia.codigo;")
        dataJson = []
        for canton in cur.fetchall():
            dataDict = {
                'provincia':canton[0],
                'codigo': canton[1],
                'nombre': canton[2]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para cantones'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/canton/<string:provincia>/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def canton(provincia,codigo):
    if request.method == 'GET':
        cur.execute("SELECT provincia.nombre, canton.codigo, canton.nombre FROM provincia, canton WHERE (canton.provincia=%s and canton.codigo=%s) AND (canton.provincia = provincia.codigo);",(provincia,codigo,))
        canton=cur.fetchone()
        if canton is None :
            content = {'Error de código': 'El canton con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'provincia': canton[0],
                'codigo': canton[1],
                'nombre': canton[2]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para canton'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/distritos',methods=['POST', 'GET', 'DELETE', 'PUT'])
def distritos():
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito;")
        dataJson = []
        for distrito in cur.fetchall():
            dataDict = {
                'provincia':distrito[0],
                'canton': distrito[1],
                'codigo': distrito[2],
                'nombre': distrito[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para cantones'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/distrito/<string:provincia>/<string:canton>/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def distrito(provincia,canton,codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE (provincia=%s and canton=%s) AND codigo=%s;",(provincia,canton,codigo,))
        distrito=cur.fetchone()
        if distrito is None :
            content = {'Error de código': 'El distrito con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'provincia': distrito[0],
                'canton': distrito[1],
                'codigo': distrito[2],
                'nombre': distrito[3]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distrito'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/ciudadanos',methods=['POST', 'GET', 'DELETE', 'PUT'])
def ciudadano():
    if request.method == 'GET':
        cur.execute(("SELECT * FROM ciudadano;").format(limit = 50, offset = 0))
        dataJson = []
        for ciudadano in cur.fetchall():
            dataDict = {
                'cedula':ciudadano[0],
                'nombre': ciudadano[3],
                'apellido1': ciudadano[4],
                'apellido2': ciudadano[5]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para ciudadano'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v2/ciudadano/<string:cedula>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def ciudadano(cedula):
    if request.method == 'GET':
        cur.execute("SELECT * FROM ciudadano WHERE cedula=%s;",(cedula,))
        ciudadano=cur.fetchone()
        if ciudadano is None :
            content = {'Error de código': 'El ciudadano con la cédula {} no existe.'.format(cedula)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'cedula': ciudadano[0],
                'nombre': ciudadano[3],
                'apellido1': ciudadano[4],
                'apellido2': ciudadano[5]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para ciudadano'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

if __name__ == '__main__':
    app.debug = True
    app.run()
