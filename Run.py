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
option = devices[0]["options"]
number_day = devices[1]["number_day"]
number_inverter = devices[2]["number_inverter"]
generated_energy = devices[3]["generated_energy"]
list_days = devices[4]["days"]

def get_entity_name():
    entity_name = []
    count = 5
    for value in devices[5: ]:
        value = devices[count]["entity_name"]
        entity_name.append(value)
        count += 1
    del entity_name[number_inverter: ]
    return entity_name

def list_asset():
    list_asset_1 = []
    count = 5
    for value in devices[5: ]:
        value = devices[count]["asset"]
        list_asset_1.append(value)
        count += 1
    return list_asset_1
def list_scope():
    list_scope_1 = []
    count = 5
    for value in devices[5: ]:
        value = devices[count]["scope"]
        list_scope_1.append(value)
        count += 1
    return list_scope_1
def list_active_energy():
    list_active_energy = []
    count = 5
    for value in devices[5: ]:
        value = devices[count]["active_energy"]
        list_active_energy.append(value)
        count += 1
    return list_active_energy

def output_days():
    list_od = []
    for day in list_days:
        day_set = Timeline(day).get_time()
        list_od.append(day_set)
    return list_od

##Inputs:
web_inverter = entity_Name(colums_Name=get_entity_name()).entity_name()
co_web = entity_Name(options=option, colums_Name=get_entity_name()).en_entity_name()
columns_name = get_entity_name()
list_sheet_days = [sheet_day("Day_1"), sheet_day("Day_2"), sheet_day("Day_3"), sheet_day("Day_4"), sheet_day("Day_5"), sheet_day("Day_6"), sheet_day("Day_7")]
list_output_days = output_days()
list_asset_1 = list_asset()
list_scope_1 = list_scope()

def cov_Wh():
    count = 0
    list_1 = []
    for value in list_active_energy()[0: number_inverter]:
        value = value
        days_Wh = get_last_day_list(option, list_active_energy()[count], co_web[count]).get_list()
        list_1.append(days_Wh)
        count += 1
    return list_1

def final_df():
    x = 0
    y = 1
    fn_df = []
    while x != number_inverter:
        inverter = Inverter_for_days(options=option , number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[x], days_enery=cov_Wh()[x], list_web_energy_inverter = web_inverter[x], list_output_days=list_output_days, asset_name=list_asset_1[x], scope_name=list_scope_1[x])
        fn_df.append(inverter.create_df())
        x += 1
    while y != len(fn_df):
        fn_df[0] = fn_df[0].append(fn_df[y])
        y += 1
    return fn_df[0]

if __name__ == "__main__":
    check_data = Check_final_data(number_inverter=number_inverter, list=web_inverter).result()
    if number_inverter == 1:
        if check_data == generated_energy:
            single_df(final_df()[0])
            print(f"Successfully for creating CSV files! {len(final_df())} rows have created.")
        else:
            print(f"Error! List total website energy: {generated_energy} doesn't equal list check_data: {check_data}!")
    elif number_inverter != 1:
        if check_data == generated_energy:
            single_df(final_df())
            print(f"Successfully for creating CSV files! {len(final_df())} rows have created.")
        else:
            print(f"Error! List total website energy: {generated_energy} doesn't equal list check_data: {check_data}!")
            