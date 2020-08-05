'''
@author: Nabil
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    return {"Name":"Microservice Application"}



@app.route('/addUe')
def addUe():
    'recuperer le nom de ue et description et resp'
    nom=request.args.get('nom');
    desc=request.args.get('desc');
    res=request.args.get('resp');
    if nom !=None and desc!=None and res!=None:
        if db.insert(nom,desc,res):
            return {"debug":"inserted"}
        else:
            return {"debug":"Not Inserted"}

    else:
        return {"name":"null paramettre"}


@app.route('/getAll')
def getall():
    data = db.get_ue_info(None)
    return jsonify(data)
 
   
@app.route('/getUE/<int:id>/')
def getUE(id):
    data = db.get_ue_info(id)
    return jsonify(data)

@app.route('/deleteUe')
def deleteUe():
    nom=request.args.get('nom');
    if nom !=None: 
    	if db.delete(nom):
    	    return {"debug":"deleteed"}
    	else:
    	    return {"debug":"Not Inserted"}

    else:
        return {"name":"null paramettre"} 
        


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
