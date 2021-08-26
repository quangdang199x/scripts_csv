from create_csv import sheet_day, single_df, Timeline, get_last_day_list, Inverter_for_days, Check_final_data
from create_csv import entity_Name
import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.safe_load(file_descriptor)
    return data

filepath = "inputs.yml"
data = yaml_loader(filepath)
devices = data["inverters"]
number_day = devices[0]["number_day"]
number_inverter = devices[1]["number_inverter"]

def get_entity_name():
    entity_name = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["entity_name"]
        entity_name.append(value)
        count += 1
    del entity_name[number_inverter: ]
    return entity_name
def tt_web_energy():
    tt_web_energy = [devices[2]["generated_energy"]["day_1"], devices[2]["generated_energy"]["day_2"], devices[2]["generated_energy"]["day_3"], devices[2]["generated_energy"]["day_4"], 
                    devices[2]["generated_energy"]["day_5"], devices[2]["generated_energy"]["day_6"], devices[2]["generated_energy"]["day_7"]]
    return tt_web_energy
def list_day():
    list_day = [devices[3]["days"]["day_1"], devices[3]["days"]["day_2"], devices[3]["days"]["day_3"], 
                devices[3]["days"]["day_4"], devices[3]["days"]["day_5"], devices[3]["days"]["day_6"], devices[3]["days"]["day_7"]]
    return list_day
def list_asset():
    list_asset_1 = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["asset"]
        list_asset_1.append(value)
        count += 1
    return list_asset_1
def list_scope():
    list_scope_1 = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["scope"]
        list_scope_1.append(value)
        count += 1
    return list_scope_1
def list_active_energy():
    list_active_energy = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["active_energy"]
        list_active_energy.append(value)
        count += 1
    return list_active_energy
###Sheet_data (no change!):
class Output_day:
    day_1_Setup = Timeline(day_month_year=list_day()[0]).get_time()
    day_2_Setup = Timeline(day_month_year=list_day()[1]).get_time()
    day_3_Setup = Timeline(day_month_year=list_day()[2]).get_time()
    day_4_Setup = Timeline(day_month_year=list_day()[3]).get_time()
    day_5_Setup = Timeline(day_month_year=list_day()[4]).get_time()
    day_6_Setup = Timeline(day_month_year=list_day()[5]).get_time()
    day_7_Setup = Timeline(day_month_year=list_day()[6]).get_time()
##Inputs:
daily_energy = entity_Name(colums_Name=get_entity_name()).entity_name()
columns_name = get_entity_name()
total_dailyEnergy = tt_web_energy()
list_sheet_days = [sheet_day("Day_1"), sheet_day("Day_2"), sheet_day("Day_3"), sheet_day("Day_4"), sheet_day("Day_5"), sheet_day("Day_6"), sheet_day("Day_7")]
list_output_days = [Output_day.day_1_Setup, Output_day.day_2_Setup, Output_day.day_3_Setup, Output_day.day_4_Setup, Output_day.day_5_Setup, Output_day.day_6_Setup, Output_day.day_7_Setup]
list_asset_1 = list_asset()
list_scope_1 = list_scope()
def web_inverter():
    web_inverter = []
    for en in daily_energy:
        en = en
        web_inverter.append(en)
    return web_inverter    
def cov_Wh():
    count = 0
    list_1 = []
    for value in list_active_energy()[0: number_inverter]:
        value = value
        days_Wh = get_last_day_list(list_active_energy()[count], web_inverter()[count]).get_list()
        list_1.append(days_Wh)
        count += 1
    return list_1
def final_df():
    x = 0
    y = 1
    fn_df = []
    while x != number_inverter:
        inverter = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[x], days_enery=cov_Wh()[x], list_web_energy_inverter = web_inverter()[x], list_output_days=list_output_days, asset_name=list_asset_1[x], scope_name=list_scope_1[x])
        fn_df.append(inverter.create_df())
        x += 1
    while y != len(fn_df):
        fn_df[0] = fn_df[0].append(fn_df[y])
        y += 1
    return fn_df[0]
    
if __name__ == "__main__":
    check_data = Check_final_data(number_inverter=number_inverter, list=web_inverter()).result()
    if number_inverter == 1:
        if check_data == tt_web_energy():
            single_df(final_df()[0])
            print("Successfully for creating CSV files!")
        else:
            print(f"Error! List total website energy: {tt_web_energy()} doesn't equal list check_data: {check_data}!")
    elif number_inverter != 1:
        if check_data == tt_web_energy():
            single_df(final_df())
            print("Successfully for creating CSV files!")
        else:
            print(f"Error! List total website energy: {tt_web_energy()} doesn't equal list check_data: {check_data}!")
            