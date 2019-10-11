from flask import Flask,render_template
import json, sys
import sqlite3
app = Flask(__name__)
def get_db():
    db =sqlite3.connect(sys.argv[1])
    return db
def get_table():
    cur = get_db().execute("select name from sqlite_master where type='table';")
    datos=cur.fetchall()
    cur.close()
    return datos
@app.route("/tablas/")
def mostrar():
    return json.dumps(get_table())

@app.route("/html/tablas/")
def mostrar_html():
    return render_template('configuracion.html',datos=get_table(),Nombre="Estos son los nombres de las tablas de nuestra base de datos.")

@app.route("/tablas/<tabla>/")
def mostrar_tabla(tabla):
    datos=get_table()
    if (tabla,) in datos:
        cur = get_db().execute("SELECT * FROM "+tabla+";")
        rv = cur.fetchall()
        cur.close()
        return json.dumps(rv)
    else:
        return "La tabla no existe"
        

@app.route("/tablas/<tabla>/info/")
def mostrar_info_tabla(tabla):
    datos=get_table()
    if (tabla,) in datos:
        cur = get_db().execute("SELECT * FROM "+tabla+";")
        rv = cur.description
        rp = cur.fetchall() 
        cur.close()
        res=[]
        for columna in rv:
            res.append(columna[0])
        res.append(repr(len(rp))+" Filas de datos tiene esta tabla")
        return json.dumps(res)
    else:
        return "La tabla no existe"

@app.route("/html/tablas/<tabla>/info/")
def mostrar_info_tabla_html(tabla):
    datos=get_table()
    if (tabla,) in datos:
        cur = get_db().execute("SELECT * FROM "+tabla+";")
        rv = cur.description
        rp = cur.fetchall()
        cur.close()
        res=[]
        for columna in rv:
            res.append(columna[0])
        res.append(repr(len(rp))+" Filas de datos tiene esta tabla")
        return render_template('configuracion.html',datos=res,Nombre="Estos son los nombres de las columnas de la tabla "+tabla)
    else:
        return "La tabla no existe"

@app.route("/html/tablas/<tabla>/")
def mostrar_tabla_html(tabla):
    datos=get_table()
    if (tabla,) in datos:
        cur = get_db().execute("SELECT * FROM "+tabla+";")
        rv = cur.fetchall()
        cur.close()
        return render_template('configuracion.html',datos=rv,Nombre="Estos son los datos de la tabla "+tabla)
    else:
        return "La tabla no existe"
    

if __name__=="__main__":
    app.run()
