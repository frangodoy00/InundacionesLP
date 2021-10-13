from flask import redirect, render_template, request, url_for, session

from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.issue import Issue
from app.db import db
from sqlalchemy import update
from sqlalchemy import select
# Public resources

def conf():
    #return a la vista
    return render_template("config.html")
def configurado():
    #Acá actualizo en la bd los nuevos valores ingresados
    orden = Ordenacion.query.filter_by(id = 1).first()
    if orden is not None: 
        orden.id_orden = int(request.form.get('category_id'))
    db.session.commit()    
    elem = Elementos.query.filter_by(id = 1).first()
    if elem is not None:
        elem.cant = int(request.form.get('numero'))
    db.session.commit()
    return redirect(url_for("home"))