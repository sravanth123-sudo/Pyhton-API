import requests
from behave import given, when, then
from db.db_connector import get_user_from_db
import configparser

config = configparser.ConfigParser()
config.read('configs/config.ini')

API_BASE = config['DEFAULT']['api_base_url']

@given('the user ID is {user_id}')
def step_given_user_id(context, user_id):
    context.user_id = user_id

@when('I send a GET request to the user endpoint')
def step_when_get_request(context):
    url = f"{API_BASE}/users/{context.user_id}"
    context.response = requests.get(url)

@then('the response status code should be 200')
def step_then_check_status(context):
    assert context.response.status_code == 200

@then('the response should match the data from database')
def step_then_compare_db(context):
    api_data = context.response.json()['data']
    db_data = get_user_from_db(context.user_id)
    assert api_data['email'] == db_data['email']
    assert api_data['first_name'] == db_data['first_name']
    assert api_data['last_name'] == db_data['last_name']
