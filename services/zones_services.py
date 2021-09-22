from model.zones import Zones
from services.covid_result_service import CovidResultService
from services.user_service import UserService


class ZoneServices:
    zone_services = {}

    def add_zones(self, pincode):
        zone_info = {"zoneType": "GREEN", "numCases": 0}
        if pincode not in ZoneServices.zone_services:
            cases_count = self.count_cases(pincode)
            if cases_count > 0 and cases_count < 5:
                zone_info["zoneType"] = "ORANGE"
                zone_info["numCases"] = cases_count
            elif cases_count > 5:
                zone_info["zoneType"] = "RED"
                zone_info["numCases"] = cases_count
            ZoneServices.zone_services[pincode] = zone_info
        else:
            zone_data = ZoneService.zone_services.get(pincode)
            zone_info["numCases"] = zone_data.get_numcases()
            zone_info["zoneType"] = zone_data.get_zone_type()

        return zone_info

    def count_cases(self, pincode):
        covid_report = CovidResultService.covid_result
        user_detail = UserService.user_detail
        positive_cases = 0
        for cases in covid_report:
            covid_result = covid_report.get(cases)
            user_pincode = user_detail.get(cases).get_pincode()
            if user_pincode == pincode and covid_result.get_result() == 'positive':
                positive_cases += 1

        return positive_cases
