import json
from flask import Flask, request
from services.user_service import UserService
from services.self_asessment_service import SelfAsessmentService

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/registerUser', methods=['POST'])
def register_user():
    req = request.data
    add_user = UserService()
    req_json = json.loads(req)
    user_id = add_user.add_user(req_json.get('name'), req_json.get(
        'phoneNumber'), req_json.get('pinCode'), 'user')
    return user_id


@app.route('/getUsers', methods=['GET'])
def get_users():
    pass


@app.route('/selfAsessment', methods=['POST'])
def self_asessment():
    req = request.data
    self_ass = SelfAsessmentService()
    req_json = json.loads(req)
    covid_risk = self_ass.add_self_asessment(req_json.get('userId'), req_json.get(
        'symptoms'), req_json.get('travelHistory'), req_json.get('contactWithCovidPatient'))
    return covid_risk


@app.route('/selfAsessments', methods=['GET'])
def get_self_asessment():
    pass


@app.route('/registerAdmin', methods=['POST'])
def register_admin():
    pass


@app.route('/updateCovidResult', methods=['PUT'])
def update_covid_result():
    pass


@app.route('/covidResult', methods=['GET'])
def get_covid_result():
    pass


@app.route('/zonesInfo', methods=['POST'])
def get_zone_info():
    pass


@app.route('/zonesInfo', methods=['GET'])
def get_all_zone_info():
    pass


if __name__ == '__main__':
    app.run(debug=True)
