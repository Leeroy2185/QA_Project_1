from app import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length

class Owners (db.Model):
    O_id = db.Column(db.Integer,primary_key=True)
    First_name = db.Column(db.String(30),nullable=False)
    Last_name =db.Column(db.String(30),nullable=False)
    Age=db.Column(db.Integer,nullable=False)
    Location=db.Column(db.String(30),nullable=False)
    Email=db.Column(db.String(40),nullable=False)
    vehicles=db.relationship("Vehicles ",backref="owners")
class Vehicles (db.Model):
    V_id = db.Column(db.Integer,primary_key=True)
    owners_ID = db.Column(db.Integer,db.ForeignKey("owners.O_id"),nullable =False)
    Model = db.Column(db.String(30),nullable=False)
    Make =db.Column(db.String(30),nullable=False)
    Year=db.Column(db.Integer,nullable=False)
    Registration=db.Column(db.String(7),nullable=False)
    Seats=db.Column(db.Integer,nullable=False)



