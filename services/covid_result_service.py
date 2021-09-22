from model.covid_result import CovidResult


class CovidResultService:

    covid_result = {}

    def add_covid_result(self, user_id, admin_id, result):
        covid_result = CovidResult()
        covid_result.set_user_id(user_id)
        covid_result.set_result(result)
        covid_result.set_created_by(admin_id)
        CovidResultService.covid_result[user_id] = covid_result
        return {"updated": True}
