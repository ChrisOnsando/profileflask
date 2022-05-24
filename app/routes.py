from flask import request,abort
from app import app
from app.models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.models import db
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify

@app.route("/register", methods=["POST"])
def register():
    data = request.json
   
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    phonenumber = data.get("phonenumber")
    feedback = data.get("feedback")
    errors = {}
    
    if not email:
        errors["email"] = "Email is required!"
    if not username:
        errors["username"] = "Username is required!"
    if not password:
        errors["password"] = "Password is required!"
    if not phonenumber:
        errors["phonenumber"] = "Phonenumber is required!"
    if not feedback:
        errors["feedback"] = "Feedback is required!"    

    if len(errors.keys()) != 0:
        abort(400, {"errors": errors})

    user = User(email=email, username=username,password=generate_password_hash(password),phonenumber=phonenumber, feedback=feedback)
    db.session.add(user)
    db.session.commit()
    return {"message": "User Account Successfully Created!"}, 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username = username).first()

    if user:
        response = check_password_hash(user.password, password)
        if response:
            access_token = create_access_token(identity= 
{"username": user.username, "email":user.email})
            return jsonify(access_token=access_token), 200
        else:
            return {"message": "Invalid User Credentials!"}, 400

@app.route("/update/<id>", methods=["PUT"])
@jwt_required()
def update(id):
    data = request.json
    user = User.query.filter_by(id=id).first()
    if user:
        user.email= data.get("email")
        user.username= data.get("username")
        user.password= data.get("password")
        user.phonenumber= data.get("phonenumber")
        user.feedback= data.get("feeback")

        db.session.commit()
        return {"message":"User Details Updated Successfully!"}, 200
    # return {"message":"User not found"}, 404

@app.route("/delete", methods=['GET','POST'])
@jwt_required()
def delete(id):
    user=User.query.filter_by(id=id).first()
    if request.method == "POST":
        if user:
           db.session.delete(user)
           db.session.commit()
           return {"message":"The User Details Deleted Successfully!"}, 200

@app.route("/logout", methods=["POST", "GET"])
@jwt_required()
def logout():
    response = jsonify({'msg':"You have Successfully Logout!"})
    unset_jwt_cookies(response)
    return response,200     

@app.route("/index", methods=["GET"])
@jwt_required()
def home():
    identity = get_jwt_identity()
    return identity