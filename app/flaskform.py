from app import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length

class Add(FlaskForm):
    O_id = StringField('Owner ID',[Length(min=1, max=40)])
    First_name = StringField('First name', [Length(min=1, max=30)])
    Last_name = StringField('Last name', [Length(min=1, max=30)])
    Age = IntegerField('Age', validators=[DataRequired(), NumberRange(1,200)])
    Location = StringField('Current town', [Length(min=1, max=30)])
    Email= StringField('Email address', [Length(min=1, max=40)])
    submit = SubmitField ("Add user")

class Vehicle(FlaskForm):
    V_id = StringField ('Vehicle ID'),[Length(min=1, max =30)]
    Model = StringField('Model of car'), [Length(min=1, max=30)]
    Make = StringField('Make of vehicle'), [Length(min=1, max=30)]
    Year = IntegerField ('Year of vehicle'),[NumberRange(1900,2030)]
    Registration = StringField('Registration number'), [Length(min=1, max=7)]
    Seats = IntegerField('Number of seats'), [NumberRange(1,20)]
    submit = SubmitField("Add vehicle")

    #updateform
    #deleteform-- class deleteform(flaskform):
    #              Vehiclename=QuerySelectfield ('select vehicle to delete')