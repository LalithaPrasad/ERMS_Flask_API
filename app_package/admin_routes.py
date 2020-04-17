import json
from flask import request
from app_package import app, db
from app_package.models import Admin

@app.route("/create_admin", methods=["POST"])
def create_admin():
    admin=Admin.query.get(1)
    if admin:
        return json.dumps({"message":"Admin exists. Only one admin is allowed"})
    else:
        data=request.get_json() or {}
        if not data:
            return json.dumps({"message":"No data"})
        else:
            un=data['username']
            pw=data['password']
            admin=Admin(username=un)
            admin.set_password(pw)
            db.session.add(admin)
            db.session.commit()
            return json.dumps({"message":"Admin added"})

@app.route("/get_token", methods=["GET"])
def get_token():
    data=request.get_json() or {}
    if not data:
        return json.dumps({"message":"No data"})
    else:
        un=data['username']
        pw=data['password']
        admin=Admin.query.filter_by(username=un).first()
        if admin and admin.check_password(pw):
            token=admin.get_token()
            db.session.commit()
            return json.dumps({"token":token})
