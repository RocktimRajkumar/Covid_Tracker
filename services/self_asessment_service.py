from model.self_asessment import SelfAsessment


class SelfAsessmentService:

    self_asessments = {}

    def add_self_asessment(self, user_id, symptoms, travel_history, contact_with_covid_patient):
        self_asessment = SelfAsessment()
        self_asessment.set_user_id(user_id)
        self_asessment.set_symptoms(symptoms)
        self_asessment.set_travel_history(travel_history)
        self_asessment.set_contact_with_covid_patient(
            contact_with_covid_patient)
        SelfAsessmentService.self_asessments[user_id] = self_asessment
        covid_risk = self.calculate_risk(
            symptoms, travel_history, contact_with_covid_patient)
        return {"riskPercentage": covid_risk}

    def calculate_risk(self, symptoms, travel_history, contact_with_covid_patient):
        symptoms_count = len(symptoms)
        if symptoms_count == 0 and not travel_history and not contact_with_covid_patient:
            return 5
        elif travel_history or contact_with_covid_patient:
            if symptoms_count == 1:
                return 50
            elif symptoms_count == 2:
                return 75
            else:
                return 95
        return 10

    def get_self_asessment_reports(self):
        asessment = []
        for asessment_key in SelfAsessmentService.self_asessments:
            self_asessment = SelfAsessmentService.self_asessments[asessment_key]
            user_id = self_asessment.get_user_id()
            symptoms = self_asessment.get_symptoms()
            travel_history = self_asessment.get_travel_history()
            contact_with_covid_patient = self_asessment.contact_with_covid_patient()

            asessment_obj = {}
            asessment_obj["userId"] = user_id
            asessment_obj["symptoms"] = symptoms
            asessment_obj["travel_history"] = travel_history
            asessment_obj["contact_with_covid_patient"] = contact_with_covid_patient
            asessment.append(asessment_obj)
        return {"selfAsessmentReport": asessment}
