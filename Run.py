from create_csv import merge_df_day, sheet_day, single_df, Timeline, get_last_day_list, Inverter_for_days, Check_final_data
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

def entity_name():
    entity_name = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["entity_name"]
        entity_name.append(value)
        count += 1
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

def list_daily_energy():
    list_daily_energy = []
    count = 4
    for value in devices[4: ]:
        value = devices[count]["daily_energy"]
        list_daily_energy.append(value)
        count += 1
    return list_daily_energy

def energyDay_1():
    energyDay_1 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_1"]
        energyDay_1.append(value)
        count += 1
    return energyDay_1
def energyDay_2():
    energyDay_2 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_2"]
        energyDay_2.append(value)
        count += 1
    return energyDay_2
def energyDay_3():
    energyDay_3 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_3"]
        energyDay_3.append(value)
        count += 1
    return energyDay_3    
def energyDay_4():
    energyDay_4 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_4"]
        energyDay_4.append(value)
        count += 1
    return energyDay_4   
def energyDay_5():
    energyDay_5 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_5"]
        energyDay_5.append(value)
        count += 1
    return energyDay_5
def energyDay_6():
    energyDay_6 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_6"]
        energyDay_6.append(value)
        count += 1
    return energyDay_6
def energyDay_7():
    energyDay_7 = []
    count = 0
    for value in list_daily_energy():
        value = list_daily_energy()[count]["day_7"]
        energyDay_7.append(value)
        count += 1
    return energyDay_7

###Sheet_data (no change!):
class stt_day:
    Day_1 = sheet_day("Day_1")
    Day_2 = sheet_day("Day_2")
    Day_3 = sheet_day("Day_3")
    Day_4 = sheet_day("Day_4")
    Day_5 = sheet_day("Day_5")
    Day_6 = sheet_day("Day_6")
    Day_7 = sheet_day("Day_7")
class Output_day:
    day_1_Setup = Timeline(day_month_year=list_day()[0]).get_time()
    day_2_Setup = Timeline(day_month_year=list_day()[1]).get_time()
    day_3_Setup = Timeline(day_month_year=list_day()[2]).get_time()
    day_4_Setup = Timeline(day_month_year=list_day()[3]).get_time()
    day_5_Setup = Timeline(day_month_year=list_day()[4]).get_time()
    day_6_Setup = Timeline(day_month_year=list_day()[5]).get_time()
    day_7_Setup = Timeline(day_month_year=list_day()[6]).get_time()

if __name__ == "__main__":
    ##Inputs:
    columns_name = entity_name()
    total_dailyEnergy = tt_web_energy()
    list_sheet_days = [stt_day.Day_1, stt_day.Day_2, stt_day.Day_3, stt_day.Day_4, stt_day.Day_5, stt_day.Day_6, stt_day.Day_7]
    web_I1 = [energyDay_1()[0], energyDay_2()[0], energyDay_3()[0], energyDay_4()[0], energyDay_5()[0], energyDay_6()[0], energyDay_7()[0]]
    web_I2 = [energyDay_1()[1], energyDay_2()[1], energyDay_3()[1], energyDay_4()[1], energyDay_5()[1], energyDay_6()[1], energyDay_7()[1]]
    web_I3 = [energyDay_1()[2], energyDay_2()[2], energyDay_3()[2], energyDay_4()[2], energyDay_5()[2], energyDay_6()[2], energyDay_7()[2]]
    web_I4 = [energyDay_1()[3], energyDay_2()[3], energyDay_3()[3], energyDay_4()[3], energyDay_5()[3], energyDay_6()[3], energyDay_7()[3]]
    web_I5 = [energyDay_1()[4], energyDay_2()[4], energyDay_3()[4], energyDay_4()[4], energyDay_5()[4], energyDay_6()[4], energyDay_7()[4]]
    web_I6 = [energyDay_1()[5], energyDay_2()[5], energyDay_3()[5], energyDay_4()[5], energyDay_5()[5], energyDay_6()[5], energyDay_7()[5]]
    web_I7 = [energyDay_1()[6], energyDay_2()[6], energyDay_3()[6], energyDay_4()[6], energyDay_5()[6], energyDay_6()[6], energyDay_7()[6]]

    ##Outputs:
    list_output_days = [Output_day.day_1_Setup, Output_day.day_2_Setup, Output_day.day_3_Setup, Output_day.day_4_Setup, Output_day.day_5_Setup, Output_day.day_6_Setup, Output_day.day_7_Setup]
    list_asset_1 = list_asset()
    list_scope_1 = list_scope()[0]

    if number_inverter == 1:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy(), website_energy_inverter=web_I1).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1,)
        df_1 = inverter_1.create_df()
        check_data = Check_final_data(1,web_I1).result()
        if total_dailyEnergy == check_data:
            df_in_site = single_df(df_1)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 2:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        check_data = Check_final_data(2,web_I1, web_I2).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 3:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=list_active_energy()[2], website_energy_inverter=web_I3).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        inverter_3 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = web_I3, list_output_days=list_output_days, asset_name=list_asset_1[2], scope_name=list_scope_1)
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        check_data = Check_final_data(3,web_I1, web_I2, web_I3).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 4:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=list_active_energy()[2], website_energy_inverter=web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=list_active_energy()[3], website_energy_inverter=web_I4).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        inverter_3 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = web_I3, list_output_days=list_output_days, asset_name=list_asset_1[2], scope_name=list_scope_1)
        inverter_4 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = web_I4, list_output_days=list_output_days, asset_name=list_asset_1[3], scope_name=list_scope_1)
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        check_data = Check_final_data(4,web_I1, web_I2, web_I3, web_I4).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 5:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=list_active_energy()[2], website_energy_inverter=web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=list_active_energy()[3], website_energy_inverter=web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=list_active_energy()[4], website_energy_inverter=web_I5).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        inverter_3 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = web_I3, list_output_days=list_output_days, asset_name=list_asset_1[2], scope_name=list_scope_1)
        inverter_4 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = web_I4, list_output_days=list_output_days, asset_name=list_asset_1[3], scope_name=list_scope_1)
        inverter_5 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = web_I5, list_output_days=list_output_days, asset_name=list_asset_1[4], scope_name=list_scope_1)
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        check_data = Check_final_data(5,web_I1, web_I2, web_I3, web_I4, web_I5).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 6:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=list_active_energy()[2], website_energy_inverter=web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=list_active_energy()[3], website_energy_inverter=web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=list_active_energy()[4], website_energy_inverter=web_I5).get_list()
        days_Wh_6 = get_last_day_list(last_day_energy=list_active_energy()[5], website_energy_inverter=web_I6).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        inverter_3 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = web_I3, list_output_days=list_output_days, asset_name=list_asset_1[2], scope_name=list_scope_1)
        inverter_4 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = web_I4, list_output_days=list_output_days, asset_name=list_asset_1[3], scope_name=list_scope_1)
        inverter_5 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = web_I5, list_output_days=list_output_days, asset_name=list_asset_1[4], scope_name=list_scope_1)
        inverter_6 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[5], days_enery=days_Wh_6, list_web_energy_inverter = web_I6, list_output_days=list_output_days, asset_name=list_asset_1[5], scope_name=list_scope_1)
        check_data = Check_final_data(7,web_I1, web_I2, web_I3, web_I4, web_I5, web_I6, web_I7).result()
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        df_6 = inverter_6.create_df()
        check_data = Check_final_data(6,web_I1, web_I2, web_I3, web_I4, web_I5, web_I6).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5, df_6)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")

    elif number_inverter == 7:
        days_Wh_1 = get_last_day_list(last_day_energy=list_active_energy()[0], website_energy_inverter=web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=list_active_energy()[1], website_energy_inverter=web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=list_active_energy()[2], website_energy_inverter=web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=list_active_energy()[3], website_energy_inverter=web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=list_active_energy()[4], website_energy_inverter=web_I5).get_list()
        days_Wh_6 = get_last_day_list(last_day_energy=list_active_energy()[5], website_energy_inverter=web_I6).get_list()
        days_Wh_7 = get_last_day_list(last_day_energy=list_active_energy()[6], website_energy_inverter=web_I7).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = web_I1, list_output_days=list_output_days, asset_name=list_asset_1[0], scope_name=list_scope_1)
        inverter_2 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = web_I2, list_output_days=list_output_days, asset_name=list_asset_1[1], scope_name=list_scope_1)
        inverter_3 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = web_I3, list_output_days=list_output_days, asset_name=list_asset_1[2], scope_name=list_scope_1)
        inverter_4 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = web_I4, list_output_days=list_output_days, asset_name=list_asset_1[3], scope_name=list_scope_1)
        inverter_5 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = web_I5, list_output_days=list_output_days, asset_name=list_asset_1[4], scope_name=list_scope_1)
        inverter_6 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[5], days_enery=days_Wh_6, list_web_energy_inverter = web_I6, list_output_days=list_output_days, asset_name=list_asset_1[5], scope_name=list_scope_1)
        inverter_7 = Inverter_for_days(number_Days = number_day, list_sheet_days = list_sheet_days, columns_name=columns_name[6], days_enery=days_Wh_7, list_web_energy_inverter = web_I7, list_output_days=list_output_days, asset_name=list_asset_1[6], scope_name=list_scope_1)
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        df_6 = inverter_6.create_df()
        df_7 = inverter_7.create_df()
        check_data = Check_final_data(7,web_I1, web_I2, web_I3, web_I4, web_I5, web_I6, web_I7).result()
        if total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5, df_6, df_7)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {total_dailyEnergy}.")
