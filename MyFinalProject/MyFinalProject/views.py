"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MyFinalProject import app
from MyFinalProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from MyFinalProject.Models.QueryFormStructure import ExpandForm
from MyFinalProject.Models.QueryFormStructure import CollapseForm

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from MyFinalProject.Models.QueryFormStructure import QueryFormStructure 
from MyFinalProject.Models.QueryFormStructure import LoginFormStructure 
from MyFinalProject.Models.QueryFormStructure import UserRegistrationFormStructure 

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
db_Functions = create_LocalDatabaseServiceRoutines() 


@app.route('/')
@app.route('/home')
def home():

    print("Home")

    """Renders the home page."""
    
    return render_template(
        'index.html',
        title='Home Page',
        img_american_flag = '/static/imgs/car_accident.jpg',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():

    print("Contact")

    """Renders the contact page."""

    return render_template(
        'contact.html',
        year=datetime.now().year,
        img_tichonet = '/static/imgs/tichonet.png',
        img_oran = '/static/imgs/ron.jpg'
    )

@app.route('/about')
def about():

    print("About")

    """Renders the about page."""
    return render_template(
        'about.html',
        year=datetime.now().year,
        img_tichonet = '/static/imgs/tichonet.png'
    )

@app.route('/data')
def data():

    print("Data")

    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='My data page.',
        car_accident1 = '/static/imgs/car_accident1.jpg',
        car_accident2 = '/static/imgs/car_accident2.jpg',
        
    )



@app.route('/hebrew_text')
def hebrew_text():
    """Renders the about page."""
    return render_template(
        'hebrew_text.html'
    )

@app.route('/data/Teonot2018' , methods = ['GET' , 'POST'])
def Teonot2018():

    print("Teonot 2018")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/Teonot2018.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'Teonot2018.html',
        title='Teonot 2018',
        year=datetime.now().year,
        message='Teonot 2018 dataset page.',
        img_2018 = '/static/imgs/2018.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/Teonot2017' , methods = ['GET' , 'POST'])
def Teonot2017():

    print("Teonot 2017")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
 
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/Teonot2017.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'Teonot2017.html',
        title='Teonot 2017',
        year=datetime.now().year,
        message='Teonot 2017 dataset page.',
        img_2017 = '/static/imgs/2017.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )


