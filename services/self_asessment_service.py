from utils.db_connect import connect


class SelfAsessmentService:

    self_asessments = {}

    def add_self_asessment(self, user_id, symptoms, travel_history, contact_with_covid_patient):
        con_obj = connect()
        cnx = con_obj.cursor()
        cnx.execute(
            f"insert into selfasessment(userId,symptoms,travelHistory,contactWithCovidPatient) values('{user_id}','{','.join(symptoms)}',{travel_history},{contact_with_covid_patient})")
        cnx.commit()
        con_obj.close()
        return {"riskPercentage": 1}
