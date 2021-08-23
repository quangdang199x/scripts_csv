from create_csv import Timeline

###Inputs:
number_Day = 3
number_inverter = 3

# Nhập vào "Entity name":
class Columns:
    inverter_1 = "PVS-100-TL-OUTD SN 115179-3Q15-4020"
    inverter_2 = "PVS-100-TL-OUTD SN 115190-3Q15-4020"
    inverter_3 = "PVS-100-TL-OUTD SN 115228-3Q15-4020"
    inverter_4 = ""
    inverter_5 = ""
    inverter_6 = ""
    inverter_7 = ""

# Nhập vào "total Website energy" cho mỗi ngày:
class total_dailyEnergy_site:
    day_1 = 1150000
    day_2 = 1563000
    day_3 = 1663000
    day_4 = 0
    day_5 = 0
    day_6 = 0
    day_7 = 0

# Nhập vào "Daily energy" cho mỗi inverter:
class Website_Energy_inverter_1:
    day_number_1 = 355000
    day_number_2 = 539000
    day_number_3 = 563000
    day_number_4 = 0
    day_number_5 = 0
    day_number_6 = 0
    day_number_7 = 0
class Website_Energy_inverter_2:
    day_number_1 = 381000
    day_number_2 = 486000
    day_number_3 = 522000
    day_number_4 = 0
    day_number_5 = 0
    day_number_6 = 0
    day_number_7 = 0
class Website_Energy_inverter_3:
    day_number_1 = 414000
    day_number_2 = 538000
    day_number_3 = 578000
    day_number_4 = 0
    day_number_5 = 0
    day_number_6 = 0
    day_number_7 = 0
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

# Nhập vào số "Latest active energy" đã xác định được trên database:
class latest_day_energy:
    inverter_1 = 119332000
    inverter_2 = 110292000
    inverter_3 = 61662000
    inverter_4 = None
    inverter_5 = None
    inverter_6 = None
    inverter_7 = None

###Outputs:
# Chọn ngày và tháng:
class Output_day:
    day_1_Setup = Timeline(day_month_year="15/8/2021").August()
    day_2_Setup = Timeline(day_month_year="16/8/2021").August()
    day_3_Setup = Timeline(day_month_year="17/8/2021").August()
    day_4_Setup = Timeline(day_month_year="11/8/2021").August()
    day_5_Setup = Timeline(day_month_year="12/8/2021").August()
    day_6_Setup = Timeline(day_month_year="13/8/2021").August()
    day_7_Setup = Timeline(day_month_year="14/8/2021").August()

# Nhập vào "asset" và "scope" đã xác định được trên database cho mỗi inverter:
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
