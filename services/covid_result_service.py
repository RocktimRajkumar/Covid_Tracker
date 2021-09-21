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

    def get_covid_result(self):
        results = []
        for result_key in CovidResultService.covid_result:
            covid = CovidResultService.covid_result[result_key]
            user_id = covid.get_user_id()
            admin_id = covid.get_created_by()
            result = covid.get_result()
            covid_obj = {}
            covid_obj["userId"] = user_id
            covid_obj["adminId"] = admin_id
            covid_obj["result"] = result
            results.append(covid_obj)
        return {"covidResult": results}
