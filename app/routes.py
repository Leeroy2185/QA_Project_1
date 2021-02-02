from app import app, db
from app.flaskform import Add, Vehicle
from app.dblayer import Owners, Vehicles
from flask import Flask, render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def add():
    error = ""
    form = Add()

    if request.method == 'POST':
        First_name = form.First_name.data,
        Last_name = form.Last_name.data,
        Age = form.Age.data,
        Location = form.Location.data,
        email = form.Email.data

        if len(First_name) == 0 or len(Last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'thank_you'
    #db.session.add
    db.session.commit()

    return render_template('Add.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')


@app.route('/read')
def read():
    all_owners = Owners.query.all()
    all_vehicles = Vehicles.query.all()
    return all_owners, all_vehicles
