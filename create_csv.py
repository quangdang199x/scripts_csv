import pandas as pd
from pandas.core.frame import DataFrame
import sys

def sheet_day(sheet_data = None):
    read_file = pd.read_excel("download.xlsx",sheet_name=sheet_data, header = 0)
    return read_file

class Inverter:
    def __init__(self, options = None, dataframe = None, latest_day_energy = None, web_dailyEnergy = None):
        self.options = options
        self.dataframe = dataframe
        self.latest_day_energy = latest_day_energy
        self.web_dailyEnergy = web_dailyEnergy

    def get_power_inverter(self):
        active_power = []
        for value in self.dataframe:
            value = float(value)
            active_power.append(value)
        return active_power

    def dailyEnergy(self):
        count = 0
        dailyEnergy = [0]
        for value in self.get_power_inverter():
            value = value*0.25 + dailyEnergy[count]
            dailyEnergy.append(value)
            count += 1
        dailyEnergy.pop(0)
        return dailyEnergy

    def round_dailyEnergy(self):
        round_dailyEnergy = []
        for value in self.dailyEnergy():
            value = int(round(value, -3))
            round_dailyEnergy.append(value)
        return round_dailyEnergy

    def subtract_dailyEnergy(self):
        subtract_dailyEnergy = []
        example = [0]
        x = 0
        for add in self.round_dailyEnergy():
            add = add
            example.append(add)
        example.pop(-1)
        for value in self.round_dailyEnergy():
            value = (self.round_dailyEnergy()[x]) - example[x]
            subtract_dailyEnergy.append(value)
            x += 1
        return subtract_dailyEnergy  

    def activeEnergy(self):
        op = self.options
        energy_15min = []
        active_energy = [self.latest_day_energy]
        count_1 = 0
        count_2 = 0
        for value in self.subtract_dailyEnergy():
            value = value
            energy_15min.append(value)
        if op == "increase":
            if max(self.round_dailyEnergy()) <= self.web_dailyEnergy:
                comp = self.web_dailyEnergy - max(self.round_dailyEnergy())
                if comp <= 20:
                    while count_1 != (comp/1000):
                        energy_15min[20+count_1] = energy_15min[20+count_1] + 1000
                        count_1 += 1
                elif comp > 20:
                    while count_1 != (comp/1000):
                        energy_15min[12+count_1] = energy_15min[12+count_1] + 1000
                        count_1 += 1
            elif max(self.round_dailyEnergy()) > self.web_dailyEnergy:
                comp = max(self.round_dailyEnergy()) - self.web_dailyEnergy
                if comp <= 20:    
                    while count_1 != (comp/1000):
                        energy_15min[20+count_1] = energy_15min[20+count_1] - 1000
                        count_1 += 1
                elif comp > 20:
                    while count_1 != (comp/1000):
                        energy_15min[15+count_1] = energy_15min[15+count_1] - 1000
                        count_1 += 1

            for energy in energy_15min:
                energy = active_energy[count_2] + energy
                active_energy.append(energy)
                count_2 += 1
            active_energy.pop(0)
            if max(active_energy) - min(active_energy) == self.web_dailyEnergy:
                return active_energy
            else:
                sys.exit()
        elif op == "decrease":
            if max(self.round_dailyEnergy()) <= self.web_dailyEnergy:
                comp = self.web_dailyEnergy - max(self.round_dailyEnergy())
                if comp <= 20:
                    while count_1 != (comp/1000):
                        energy_15min[20+count_1] = energy_15min[20+count_1] + 1000
                        count_1 += 1
                    energy_15min.reverse()
                elif comp > 20:
                    while count_1 != (comp/1000):
                        energy_15min[12+count_1] = energy_15min[12+count_1] + 1000
                        count_1 += 1
                    energy_15min.reverse()
            elif max(self.round_dailyEnergy()) > self.web_dailyEnergy:
                comp = max(self.round_dailyEnergy()) - self.web_dailyEnergy
                if comp <= 20:    
                    while count_1 != (comp/1000):
                        energy_15min[20+count_1] = energy_15min[20+count_1] - 1000
                        count_1 += 1
                    energy_15min.reverse()
                elif comp > 20:
                    while count_1 != (comp/1000):
                        energy_15min[15+count_1] = energy_15min[15+count_1] - 1000
                        count_1 += 1
                    energy_15min.reverse()
            
            for energy in energy_15min:
                energy = active_energy[count_2] - energy
                active_energy.append(energy)
                count_2 += 1
            active_energy.pop(0)
            active_energy.reverse()
            if max(active_energy) - min(active_energy) == self.web_dailyEnergy:
                return active_energy
            else:
                sys.exit()
        else:
            sys.exit()

    def create_CSV_files(self, asset = None, scope = None, time = None):
        dataframe = pd.DataFrame(
            {
                "time" : time,
                "asset" : asset,
                "scope" : scope,
                "active_power" : [None]*22 + self.get_power_inverter() + [None]*19,
                "active_energy" : [None]*22 + self.activeEnergy() + [None]*19,
            }
        )
        return dataframe      

class Timeline:
    def __init__(self, day_month_year = None):
        self.day_month_year = day_month_year
    def get_time(self):
        get_time = pd.read_csv("time_store/time.csv", header=0)
        return get_time[self.day_month_year]

class Setup_Inverter:
    def __init__(self, options = None, choose_sheet_day=None , choose_columns=None, latest_day_energy=None, web_dailyEnergy=None, output_day=None, asset=None, scope=None):
        self.options = options
        self.choose_sheet_day = choose_sheet_day
        self.output_day = output_day
        self.choose_columns = choose_columns
        self.latest_day_energy = latest_day_energy
        self.web_dailyEnergy = web_dailyEnergy
        self.asset = asset
        self.scope = scope
    
    def setup_1(self):
        inverter = Inverter(options= self.options, dataframe=DataFrame(self.choose_sheet_day, columns=[self.choose_columns]).values, latest_day_energy=self.latest_day_energy ,web_dailyEnergy=self.web_dailyEnergy)
        return inverter
    def get_dataframe(self):
        df = self.setup_1().create_CSV_files(time=self.output_day, asset=self.asset, scope=self.scope)
        return df

class get_last_day_list:
    def __init__(self, options=None, last_day_energy=None, website_energy_inverter=None):
        self.options=options
        self.last_day_energy = last_day_energy
        self.website_energy_inverter = website_energy_inverter
    def get_list(self):
        opt = self.options
        list_last_day_energy = [self.last_day_energy]
        count_1 = 0
        if opt == "increase":
            for value in self.website_energy_inverter:
                value = value + list_last_day_energy[count_1]
                list_last_day_energy.append(value)
                count_1 += 1
            list_last_day_energy.pop(-1)
            return list_last_day_energy
        elif opt == "decrease":
            for value in self.website_energy_inverter:
                value = list_last_day_energy[count_1] - value
                list_last_day_energy.append(value)
                count_1 += 1
            list_last_day_energy.pop(-1)
            list_last_day_energy.reverse()
            return list_last_day_energy

class Inverter_for_days:
    def __init__(self, options = None, number_Days = None, list_sheet_days=None, columns_name=None, days_enery=None, list_web_energy_inverter=None, list_output_days=None, asset_name=None, scope_name=None):
        self.options = options
        self.number_Days = number_Days
        self.list_sheet_days = list_sheet_days
        self.columns_name = columns_name
        self.days_energy = days_enery
        self.list_web_energy_inverter=list_web_energy_inverter
        self.list_output_days = list_output_days
        self.asset_name = asset_name
        self.scope_name = scope_name
    def create_df(self):
        df_tem = []
        x = 0
        y = 1
        while x != self.number_Days:
            per_inverter = Setup_Inverter(
                options=self.options,
                choose_sheet_day=self.list_sheet_days[x],
                choose_columns=self.columns_name,
                latest_day_energy=self.days_energy[x],
                web_dailyEnergy=self.list_web_energy_inverter[x],
                output_day=self.list_output_days[x],
                asset=self.asset_name,
                scope=self.scope_name,
            )
            dframe = per_inverter.get_dataframe()
            x += 1
            df_tem.append(dframe)
        while y != len(df_tem):
            df_tem[0] = df_tem[0].append(df_tem[y])
            y += 1
        return df_tem[0]

class entity_Name:
    def __init__(self, options = None, colums_Name = None):
        self.options = options
        self.columns_Name = colums_Name
    def entity_name(self):
        n_list = []
        counts = 0
        while counts != len(self.columns_Name):
            values = DataFrame(sheet_day("Daily_energy"), columns=[self.columns_Name[counts]]).values    
            list_1 = []        
            for value in values:
                value = int(value)*1000
                list_1.append(value)
            n_list.append(list_1)
            counts += 1
        return n_list
    def en_entity_name(self):
        n_list = []
        counts = 0
        while counts != len(self.columns_Name):
            values = DataFrame(sheet_day("Daily_energy"), columns=[self.columns_Name[counts]]).values    
            list_1 = []        
            for value in values:
                value = int(value)*1000
                list_1.append(value)
            if self.options == "increase":
                n_list.append(list_1)
            elif self.options == "decrease":
                list_1.reverse()
                n_list.append(list_1)
            counts += 1
        return n_list

class Check_final_data:
    def __init__(self, number_inverter = None, list=None):
        self.list = list
        self.number_inverter = number_inverter
    def result(self):
        (self.list).append(self.list[0].copy())
        count = 0
        for check in self.list[0]:
            x = 1
            while x != self.number_inverter:
                self.list[-1][count] = self.list[-1][count] + self.list[x][count]
                x += 1
            count += 1
        resuft = self.list.pop(-1)
        return resuft

def single_df(df=None):
    return df.to_csv("inverter.csv", index=False)
