from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
from flask_heroku import Heroku


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://wuynfrhtljkkam:8d5fc36b22f364af2961c3530eb30492b17b595b37bea1525755a28f0cd32525@ec2-174-129-255-59.compute-1.amazonaws.com:5432/d6toe3u0ta2f4e"

heroku = Heroku(app)
db = SQLAlchemy(app)

#tables
class Reservation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  phone = db.Column(db.Integer,primary_key=True)

  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone

@app.route("/reservations/create", methods=["POST"])
def create_reservation():
  if request.content_type =="application/json":
    post_data = request.get_json()
    name = post_data.get("name")
    email = post_data.get("email")  
    phone = post_data.get("phone")  

    record = Reservation(name, email, phone)

    db.session.add(record)
    db.session.commit

  return jsonify("Reservation sent")
  return jsonify("Error: request must be sent as JSON")  

@app.route("/reservations/get", methods=["GET"])
def get_all_reservations():
  all_reservations = db.session.query(Reservation.id, Reservation.name, Reservation.email, Reservation.phone).all()
  return jsonify(all_competitors)


@app.route("/reservations/delete", methods=["DELETE"])
def delete_reservation(level):
  record = db.session.query(Reservation).filter(Reservation.id == id).first()
  db.session.delete(record)
  db.session.commit()
  return jsonify("Record Deleted")


if __name__ == "__main__":
  app.debug = True
  app.run()
