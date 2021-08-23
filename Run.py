from create_csv import merge_df_day, sheet_day, single_df, get_last_day_list, Inverter_for_days, Check_final_data
from inputs import Columns, total_dailyEnergy_site, Website_Energy_inverter_1, Website_Energy_inverter_2, Website_Energy_inverter_3, Website_Energy_inverter_4, Website_Energy_inverter_5, Website_Energy_inverter_6, Website_Energy_inverter_7
from inputs import latest_day_energy, Output_day, Asset, Scope, number_Day, number_inverter

###Sheet_data (no change!):
class stt_day:
    Day_1 = sheet_day("Day_1")
    Day_2 = sheet_day("Day_2")
    Day_3 = sheet_day("Day_3")
    Day_4 = sheet_day("Day_4")
    Day_5 = sheet_day("Day_5")
    Day_6 = sheet_day("Day_6")
    Day_7 = sheet_day("Day_7")

if __name__ == "__main__":
    ##Inputs:
    list_columns_name = [Columns.inverter_1, Columns.inverter_2, Columns.inverter_3, Columns.inverter_4, Columns.inverter_5, Columns.inverter_6, Columns.inverter_7]
    list_total_dailyEnergy = [total_dailyEnergy_site.day_1, total_dailyEnergy_site.day_2, total_dailyEnergy_site.day_3, total_dailyEnergy_site.day_4, total_dailyEnergy_site.day_5, total_dailyEnergy_site.day_6, total_dailyEnergy_site.day_7]
    list_sheet_days = [stt_day.Day_1, stt_day.Day_2, stt_day.Day_3, stt_day.Day_4, stt_day.Day_5, stt_day.Day_6, stt_day.Day_7]
    list_web_I1 = [Website_Energy_inverter_1.day_number_1, Website_Energy_inverter_1.day_number_2,Website_Energy_inverter_1.day_number_3,Website_Energy_inverter_1.day_number_4,Website_Energy_inverter_1.day_number_5,Website_Energy_inverter_1.day_number_6,Website_Energy_inverter_1.day_number_7]
    list_web_I2 = [Website_Energy_inverter_2.day_number_1, Website_Energy_inverter_2.day_number_2,Website_Energy_inverter_2.day_number_3,Website_Energy_inverter_2.day_number_4,Website_Energy_inverter_2.day_number_5,Website_Energy_inverter_2.day_number_6,Website_Energy_inverter_2.day_number_7]
    list_web_I3 = [Website_Energy_inverter_3.day_number_1, Website_Energy_inverter_3.day_number_2,Website_Energy_inverter_3.day_number_3,Website_Energy_inverter_3.day_number_4,Website_Energy_inverter_3.day_number_5,Website_Energy_inverter_3.day_number_6,Website_Energy_inverter_3.day_number_7]
    list_web_I4 = [Website_Energy_inverter_4.day_number_1, Website_Energy_inverter_4.day_number_2,Website_Energy_inverter_4.day_number_3,Website_Energy_inverter_4.day_number_4,Website_Energy_inverter_4.day_number_5,Website_Energy_inverter_4.day_number_6,Website_Energy_inverter_4.day_number_7]
    list_web_I5 = [Website_Energy_inverter_5.day_number_1, Website_Energy_inverter_5.day_number_2,Website_Energy_inverter_5.day_number_3,Website_Energy_inverter_5.day_number_4,Website_Energy_inverter_5.day_number_5,Website_Energy_inverter_5.day_number_6,Website_Energy_inverter_5.day_number_7]
    list_web_I6 = [Website_Energy_inverter_6.day_number_1, Website_Energy_inverter_6.day_number_2,Website_Energy_inverter_6.day_number_3,Website_Energy_inverter_6.day_number_4,Website_Energy_inverter_6.day_number_5,Website_Energy_inverter_6.day_number_6,Website_Energy_inverter_6.day_number_7]
    list_web_I7 = [Website_Energy_inverter_7.day_number_1, Website_Energy_inverter_7.day_number_2,Website_Energy_inverter_7.day_number_3,Website_Energy_inverter_7.day_number_4,Website_Energy_inverter_7.day_number_5,Website_Energy_inverter_7.day_number_6,Website_Energy_inverter_7.day_number_7]
    
    ##Outputs:
    list_output_days = [Output_day.day_1_Setup, Output_day.day_2_Setup, Output_day.day_3_Setup, Output_day.day_4_Setup, Output_day.day_5_Setup, Output_day.day_6_Setup, Output_day.day_7_Setup]
    list_asset = [Asset.inverter_1, Asset.inverter_2, Asset.inverter_3, Asset.inverter_4, Asset.inverter_5, Asset.inverter_6, Asset.inverter_7]
    list_scope = [Scope.scope_all_in_site]

    if number_inverter == 1:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0],)
        df_1 = inverter_1.create_df()
        check_data = Check_final_data(1,list_web_I1).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = single_df(df_1)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 2:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        check_data = Check_final_data(2,list_web_I1, list_web_I2).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 3:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=latest_day_energy.inverter_3, website_energy_inverter=list_web_I3).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        inverter_3 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = list_web_I3, list_output_days=list_output_days, asset_name=list_asset[2], scope_name=list_scope[0])
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        check_data = Check_final_data(3,list_web_I1, list_web_I2, list_web_I3).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 4:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=latest_day_energy.inverter_3, website_energy_inverter=list_web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=latest_day_energy.inverter_4, website_energy_inverter=list_web_I4).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        inverter_3 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = list_web_I3, list_output_days=list_output_days, asset_name=list_asset[2], scope_name=list_scope[0])
        inverter_4 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = list_web_I4, list_output_days=list_output_days, asset_name=list_asset[3], scope_name=list_scope[0])
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        check_data = Check_final_data(4,list_web_I1, list_web_I2, list_web_I3, list_web_I4).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 5:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=latest_day_energy.inverter_3, website_energy_inverter=list_web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=latest_day_energy.inverter_4, website_energy_inverter=list_web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=latest_day_energy.inverter_5, website_energy_inverter=list_web_I5).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        inverter_3 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = list_web_I3, list_output_days=list_output_days, asset_name=list_asset[2], scope_name=list_scope[0])
        inverter_4 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = list_web_I4, list_output_days=list_output_days, asset_name=list_asset[3], scope_name=list_scope[0])
        inverter_5 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = list_web_I5, list_output_days=list_output_days, asset_name=list_asset[4], scope_name=list_scope[0])
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        check_data = Check_final_data(5,list_web_I1, list_web_I2, list_web_I3, list_web_I4, list_web_I5).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 6:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=latest_day_energy.inverter_3, website_energy_inverter=list_web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=latest_day_energy.inverter_4, website_energy_inverter=list_web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=latest_day_energy.inverter_5, website_energy_inverter=list_web_I5).get_list()
        days_Wh_6 = get_last_day_list(last_day_energy=latest_day_energy.inverter_6, website_energy_inverter=list_web_I6).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        inverter_3 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = list_web_I3, list_output_days=list_output_days, asset_name=list_asset[2], scope_name=list_scope[0])
        inverter_4 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = list_web_I4, list_output_days=list_output_days, asset_name=list_asset[3], scope_name=list_scope[0])
        inverter_5 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = list_web_I5, list_output_days=list_output_days, asset_name=list_asset[4], scope_name=list_scope[0])
        inverter_6 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[5], days_enery=days_Wh_6, list_web_energy_inverter = list_web_I6, list_output_days=list_output_days, asset_name=list_asset[5], scope_name=list_scope[0])
        check_data = Check_final_data(7,list_web_I1, list_web_I2, list_web_I3, list_web_I4, list_web_I5, list_web_I6, list_web_I7).result()
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        df_6 = inverter_6.create_df()
        check_data = Check_final_data(6,list_web_I1, list_web_I2, list_web_I3, list_web_I4, list_web_I5, list_web_I6).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5, df_6)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")

    elif number_inverter == 7:
        days_Wh_1 = get_last_day_list(last_day_energy=latest_day_energy.inverter_1, website_energy_inverter=list_web_I1).get_list()
        days_Wh_2 = get_last_day_list(last_day_energy=latest_day_energy.inverter_2, website_energy_inverter=list_web_I2).get_list()
        days_Wh_3 = get_last_day_list(last_day_energy=latest_day_energy.inverter_3, website_energy_inverter=list_web_I3).get_list()
        days_Wh_4 = get_last_day_list(last_day_energy=latest_day_energy.inverter_4, website_energy_inverter=list_web_I4).get_list()
        days_Wh_5 = get_last_day_list(last_day_energy=latest_day_energy.inverter_5, website_energy_inverter=list_web_I5).get_list()
        days_Wh_6 = get_last_day_list(last_day_energy=latest_day_energy.inverter_6, website_energy_inverter=list_web_I6).get_list()
        days_Wh_7 = get_last_day_list(last_day_energy=latest_day_energy.inverter_7, website_energy_inverter=list_web_I7).get_list()
        inverter_1 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[0], days_enery=days_Wh_1, list_web_energy_inverter = list_web_I1, list_output_days=list_output_days, asset_name=list_asset[0], scope_name=list_scope[0])
        inverter_2 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[1], days_enery=days_Wh_2, list_web_energy_inverter = list_web_I2, list_output_days=list_output_days, asset_name=list_asset[1], scope_name=list_scope[0])
        inverter_3 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[2], days_enery=days_Wh_3, list_web_energy_inverter = list_web_I3, list_output_days=list_output_days, asset_name=list_asset[2], scope_name=list_scope[0])
        inverter_4 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[3], days_enery=days_Wh_4, list_web_energy_inverter = list_web_I4, list_output_days=list_output_days, asset_name=list_asset[3], scope_name=list_scope[0])
        inverter_5 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[4], days_enery=days_Wh_5, list_web_energy_inverter = list_web_I5, list_output_days=list_output_days, asset_name=list_asset[4], scope_name=list_scope[0])
        inverter_6 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[5], days_enery=days_Wh_6, list_web_energy_inverter = list_web_I6, list_output_days=list_output_days, asset_name=list_asset[5], scope_name=list_scope[0])
        inverter_7 = Inverter_for_days(number_Days = number_Day, list_sheet_days = list_sheet_days, columns_name=list_columns_name[6], days_enery=days_Wh_7, list_web_energy_inverter = list_web_I7, list_output_days=list_output_days, asset_name=list_asset[6], scope_name=list_scope[0])
        df_1 = inverter_1.create_df()
        df_2 = inverter_2.create_df()
        df_3 = inverter_3.create_df()
        df_4 = inverter_4.create_df()
        df_5 = inverter_5.create_df()
        df_6 = inverter_6.create_df()
        df_7 = inverter_7.create_df()
        check_data = Check_final_data(7,list_web_I1, list_web_I2, list_web_I3, list_web_I4, list_web_I5, list_web_I6, list_web_I7).result()
        if list_total_dailyEnergy == check_data:
            df_in_site = merge_df_day(df_1,df_2,df_3, df_4, df_5, df_6, df_7)    
            print(f"Successfully creating CSV files!")
        else: 
            print(f"Error! Daily energy per inverter: {check_data}, does not equal total energy day on the website: {list_total_dailyEnergy}.")
