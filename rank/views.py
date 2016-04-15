from flask import render_template, request, abort, redirect
from . import app
from .database.models import *
from .database import Session

@app.route('/')
def show_rank():
    r = Session.query(RankPage).order_by(RankPage.id.desc()).first()
    html = '<p>updated at %s</p>' %(r.time)
    return html + r.html
