from create_csv import Timeline

###Inputs:
number_Day = 7
number_inverter = 3

class Columns:
    inverter_1 = "PVS-100-TL-OUTD SN 115179-3Q15-4020"
    inverter_2 = "PVS-100-TL-OUTD SN 115190-3Q15-4020"
    inverter_3 = "PVS-100-TL-OUTD SN 115228-3Q15-4020"
    inverter_4 = ""
    inverter_5 = ""
    inverter_6 = ""
    inverter_7 = ""

class total_dailyEnergy_site:
    day_1 = 1554000
    day_2 = 1554000
    day_3 = 1626000
    day_4 = 1391000
    day_5 = 1454000
    day_6 = 1327000
    day_7 = 1640000

class Website_Energy_inverter_1:
    day_number_1 = 517000
    day_number_2 = 515000
    day_number_3 = 548000
    day_number_4 = 459000
    day_number_5 = 473000
    day_number_6 = 447000
    day_number_7 = 531000
class Website_Energy_inverter_2:
    day_number_1 = 501000
    day_number_2 = 513000
    day_number_3 = 521000
    day_number_4 = 446000
    day_number_5 = 480000
    day_number_6 = 426000
    day_number_7 = 539000
class Website_Energy_inverter_3:
    day_number_1 = 536000
    day_number_2 = 526000
    day_number_3 = 557000
    day_number_4 = 486000
    day_number_5 = 501000
    day_number_6 = 454000
    day_number_7 = 570000
class Website_Energy_inverter_4:
    day_number_1 = None
    day_number_2 = None
    day_number_3 = None
    day_number_4 = None
    day_number_5 = None
    day_number_6 = None
    day_number_7 = None
class Website_Energy_inverter_5:
    day_number_1 = None
    day_number_2 = None
    day_number_3 = None
    day_number_4 = None
    day_number_5 = None
    day_number_6 = None
    day_number_7 = None
class Website_Energy_inverter_6:
    day_number_1 = None
    day_number_2 = None
    day_number_3 = None
    day_number_4 = None
    day_number_5 = None
    day_number_6 = None
    day_number_7 = None
class Website_Energy_inverter_7:
    day_number_1 = None
    day_number_2 = None
    day_number_3 = None
    day_number_4 = None
    day_number_5 = None
    day_number_6 = None
    day_number_7 = None

class latest_day_energy:
    inverter_1 = 112751000
    inverter_2 = 103890000
    inverter_3 = 54809000
    inverter_4 = None
    inverter_5 = None
    inverter_6 = None
    inverter_7 = None

###Outputs:
class Output_day:
    day_1_Setup = Timeline(day_month_year="1/8/2021").August()
    day_2_Setup = Timeline(day_month_year="2/8/2021").August()
    day_3_Setup = Timeline(day_month_year="3/8/2021").August()
    day_4_Setup = Timeline(day_month_year="4/8/2021").August()
    day_5_Setup = Timeline(day_month_year="5/8/2021").August()
    day_6_Setup = Timeline(day_month_year="6/8/2021").August()
    day_7_Setup = Timeline(day_month_year="7/8/2021").August()

class Asset:
    inverter_1 = "ABB-115179-3Q15-4020"
    inverter_2 = "ABB-115190-3Q15-4020"
    inverter_3 = "ABB-115228-3Q15-4020"
    inverter_4 = ""
    inverter_5 = ""
    inverter_6 = ""
    inverter_7 = ""

class Scope:
    scope_all_in_site = "b107e879-e80b-499d-9e12-2b8c0a6cb4bf"
