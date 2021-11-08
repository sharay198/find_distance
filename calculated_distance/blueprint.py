from flask import Blueprint, render_template, make_response, url_for
from werkzeug.utils import redirect
from calculated_distance.forms import CalculateDistanceForm
from flask import request, flash
from loguru import logger
import requests

API_KEY = 'cbddbd2c-95ce-4aa1-ba5a-5d0416597c20'
calculated_distance = Blueprint('calculated_distance', __name__, template_folder='templates')


def make_url(address):
    return f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json'


def get_data_from_response(url):
    req = requests.get(url)
    data = req.json()
    return data


# logging.basicConfig(level=20, filename='my_log.log')


# @calculated_distance.route('/', methods=['POST', 'GET'])
# def index():
#     form = CalculateDistanceForm()
#     if request.method == 'POST':
#
#         address = request.form['address']
#         bound_form = CalculateDistanceForm(address=address)
#         # print(f'bound_form["address"]: {bound_form.address.data}')
#         if bound_form.validate():
#             url = make_url(address)
#             data = get_data_from_response(url)
#             print(type(data))
#             # print(response.is_json)
#             logger.add('info.log', format='{time} {message}', level='INFO')
#             logger.info(f'{address} {data}')
#             print('Helloo')
#             # response = make_response()
#             return redirect(make_url(address))
#         else:
#             form = CalculateDistanceForm(address=address)
#             print(form.address.errors)
#
#             return render_template('calculated_distance/index.html', form=form)
#     return render_template('calculated_distance/index.html', form=form)

@calculated_distance.route('/', methods=['POST', 'GET'])
def index():
    form = CalculateDistanceForm()

    # if request.method == 'POST':

    if request.method == 'POST':
        print('It is POST again')
        if form.errors and form.data:
            # form = CalculateDistanceForm()
            return redirect(url_for('calculated_distance.index'))
        address = request.form['address']
        bound_form = CalculateDistanceForm(data={'address': address})
        if bound_form.validate():
            distance = f'The distance between {address}: '
            bound_form = CalculateDistanceForm(data={'address': address, 'distance': distance})

            url = make_url(address)
            return redirect(url)
            # return render_template('calculated_distance/index.html', form=bound_form)
        elif not bound_form.validate() and bound_form.data:
            return redirect(url_for('calculated_distance.index'))
        elif not bound_form.validate():
            print(f'bound_form.errors still have error {bound_form.errors}')
            print(f'{form} is not pass validation')
            # bound_form = CalculateDistanceForm(address=address)
            print(f'There are errors {bound_form.address.errors}')
            return render_template('calculated_distance/index.html', form=bound_form)

    if request.method == 'GET':
        form = CalculateDistanceForm()
        print('I am here')
        return render_template('calculated_distance/index.html', form=form)