from flask import render_template, request, redirect, session,  url_for

from tasks.task import ExcelExecutor

from app import database as db

from app.models import User, Unit, Employment
from . import home_blueprint

import json

from flask_login import current_user, login_required

@home_blueprint.route('/all-users', methods=['GET'])
def all_users():

    all_users = User.query.all()
    all_units = Unit.query.all()

    return render_template('home/home.html', users = all_users, units = all_units, title = "Users")



@home_blueprint.route('/users/<int:user_id>', methods=['GET'])
@login_required
def user_detail(user_id):

    user = User.query.get_or_404(user_id)

    return render_template('home/userdetail.html', user = user)


@home_blueprint.route('/units', methods=['GET'])
@login_required
def company_stats():

    all_units = Unit.query.all()
    data_labels = []
    data_values = []
    for obj in all_units:
        data_labels.append(obj.name)
        data_values.append(obj.total_years)

    return render_template('home/company_stats.html', units = all_units, data_labels = data_labels, data_values = data_values)


@home_blueprint.route('/upload-excel', methods = ['POST', 'GET'])
@login_required
def upload_excel():

    if request.method != 'POST':

        return render_template('posts/uploadexcel.html', title = "POST")

    file = request.files['file']

    # save file in local directory
    file.save(file.filename)
 
    # Parse the data as a Pandas DataFrame type

    try:
        executor = ExcelExecutor(file)
    except Exception as e:
        return "<h2>Bad file upload: Kindly upload a vilid .xlx, .xlsx file</h2>"

    
    data = executor.read_flat()

    json_records = data.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)

    executor.save_to_db()

    # return data.to_html()

    return render_template('posts/uploadexcel.html',  data = data, titles = ['Units', 'Tenure'])