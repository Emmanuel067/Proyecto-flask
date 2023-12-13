from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, flash

from database import Database
from database import engine
from database import db_session
from sqlalchemy import asc
import models

print("Iniciando servidor...")

app = Flask(__name__)

Database.metadata.create_all(engine)

@app.get('/')
def home():
    return render_template("home.html")

@app.get('/crear')
def crear():
    return render_template("registro_cita.html")

@app.get('/act/<id>/update')
def act(id):
    cita = db_session.query(models.Citas).get(id)
    return render_template("actualizar.html", cita=cita)

@app.get('/vista')
def inicio():
    citas = db_session.query(models.Citas).order_by(asc(models.Citas.id)).all()
    return render_template("vista_citas.html", citas=citas)

@app.post('/registro')
def registro():
    _nombre_mascota = request.form['txt_nombre_mascota']
    _tipo_animal = request.form['txt_tipo_animal']
    _fecha_cita = datetime.strptime(request.form['txt_fecha_cita'], '%Y-%m-%d %H:%M:%S')
    _observaciones = request.form['txt_observaciones']

    nueva_cita = models.Citas(
        nombre_mascota=_nombre_mascota,
        tipo_animal=_tipo_animal,
        fecha_cita=_fecha_cita,
        observaciones=_observaciones
    )
    db_session.add(nueva_cita)
    db_session.commit()
    return redirect(url_for('inicio'))

@app.get('/eliminar/<id>/delete')
def eliminar(id):
    cita = db_session.query(models.Citas).get(id)

    db_session.delete(cita)
    db_session.commit()

    return redirect(url_for('inicio'))

@app.post('/actualizar/<id>/update')
def actualizar(id):
    cita = db_session.query(models.Citas).get(id)
    nueva_id = request.form['id_a']
    nuevo_nombre_mascota = request.form['txt_nombre_mascota_a']
    nuevo_tipo_animal = request.form['txt_tipo_animal_a']
    nueva_fecha_cita = datetime.strptime(request.form['txt_fecha_cita_a'], '%Y-%m-%d %H:%M:%S')
    nueva_observaciones = request.form['txt_observaciones_a']

    cita.id = nueva_id
    cita.nombre_mascota = nuevo_nombre_mascota
    cita.tipo_animal = nuevo_tipo_animal
    cita.fecha_cita = nueva_fecha_cita
    cita.observaciones = nueva_observaciones

    db_session.add(cita)
    db_session.commit()
    citas = db_session.query(models.Citas).all()
    return render_template("vista_citas.html", citas=citas)



app.run('0.0.0.0', 8080, debug=True)
