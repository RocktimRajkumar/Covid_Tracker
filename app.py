import json
from flask import Flask, request
from services.user_service import UserService
from services.self_asessment_service import SelfAsessmentService
from services.covid_result_service import CovidResultService
from services.zones_services import ZoneServices

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


@app.route('/selfAsessment', methods=['POST'])
def self_asessment():
    req = request.data
    self_ass = SelfAsessmentService()
    req_json = json.loads(req)
    covid_risk = self_ass.add_self_asessment(req_json.get('userId'), req_json.get(
        'symptoms'), req_json.get('travelHistory'), req_json.get('contactWithCovidPatient'))
    return covid_risk


@app.route('/registerAdmin', methods=['POST'])
def register_admin():
    req = request.data
    add_user = UserService()
    req_json = json.loads(req)
    user_id = add_user.add_user(req_json.get('name'), req_json.get(
        'phoneNumber'), req_json.get('pinCode'), 'user')
    return user_id


@app.route('/updateCovidResult', methods=['PUT'])
def update_covid_result():
    req = request.data
    update_result = CovidResultService()
    req_json = json.loads(req)
    update_result = update_result.add_covid_result(req_json.get('userId'), req_json.get(
        'adminId'), req_json.get('result'))
    return update_result


@app.route('/zonesInfo', methods=['POST'])
def get_zone_info():
    req = request.data
    zone_info = ZoneServices()
    req_json = json.loads(req)
    zone_result = zone_info.add_zones(req_json.get('pinCode'))
    return zone_result


if __name__ == '__main__':
    app.run(debug=True)
