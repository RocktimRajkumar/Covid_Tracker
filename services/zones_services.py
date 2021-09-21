from model.zones import Zones
from services.covid_result_service import CovidResultService
from services.user_service import UserService


class ZoneServices:
    zone_info = {}

    def add_zones(self, pincode):
        zone_info = {}
        zone_type = 'GREEN'
        num_cases = 0
        num_cases = self.count_cases(pincode)
        if num_cases > 0 and num_cases <=5:
            zone_type = "ORANGE"
        elif num_cases > 5:
            zone_type = "RED"
        zone = Zones()
        zone.set_numcases(num_cases)
        zone.set_pincode(pincode)
        zone.set_zone_type(zone_type)
        ZoneServices.zone_info[pincode] = zone
        zone_info["numCases"] = num_cases
        zone_info["zoneType"] = zone_type

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

    def get_all_zone_info(self):
        zone_info = []
        for zone_key in ZoneServices.zone_info:
            zone_obj = ZoneServices.zone_info[zone_key]
            zone_pincode = zone_key
            zone_numcases = zone_obj.get_numcases()
            zone_type = zone_obj.get_zone_type()
            zone = {}
            zone["pinCode"] = zone_pincode
            zone["numCases"] = zone_numcases
            zone["zoneType"] = zone_type
            zone_info.append(zone)
        return {"zoneInfo": zone_info}
