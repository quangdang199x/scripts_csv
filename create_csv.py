import pandas as pd
from pandas.core.frame import DataFrame
import sys

class Inverter:
    read_file = pd.read_csv("download.csv", header = 0)
    def __init__(self, dataframe = None, latest_day_energy = None, web_dailyEnergy = None):
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

    def increase_activeEnergy(self):
        energy_15min = []
        active_energy = [self.latest_day_energy]
        count_1 = 0
        count_2 = 0
        for value in self.subtract_dailyEnergy():
            value = value
            energy_15min.append(value)
        if max(self.round_dailyEnergy()) <= self.web_dailyEnergy:
            comp = self.web_dailyEnergy - max(self.round_dailyEnergy())
            while count_1 != (comp/1000):
                energy_15min[20+count_1] = energy_15min[20+count_1] + 1000
                count_1 += 1
        elif max(self.round_dailyEnergy()) > self.web_dailyEnergy:
            comp = max(self.round_dailyEnergy()) - self.web_dailyEnergy
            while count_1 != (comp/1000):
                energy_15min[20+count_1] = energy_15min[20+count_1] - 1000
                count_1 += 1
        for energy in energy_15min:
            energy = active_energy[count_2] + energy
            active_energy.append(energy)
            count_2 += 1
        active_energy.pop(0)
        if max(active_energy) - min(active_energy) == self.web_dailyEnergy:
            return active_energy
        else:
            return sys.exit()

    def check_value(self):
        check = max(self.increase_activeEnergy()) - min(self.increase_activeEnergy())
        return check   
        
    def create_CSV_files(self, asset = None, scope = None, time = None):
        dataframe = pd.DataFrame(
            {
                "time" : time,
                "asset" : asset,
                "scope" : scope,
                "active_power" : [None]*22 + self.get_power_inverter() + [None]*19,
                "active_energy" : [None]*22 + self.increase_activeEnergy() + [None]*19,
            }
        )
        return dataframe      

class Timeline:
    def __init__(self, day_month_year = None):
        self.day_month_year = day_month_year  
    def January(self):
        january = pd.read_csv("time_store/January.csv", header=0)
        return january[self.day_month_year]
    def February(self):
        february = pd.read_csv("time_store/February.csv", header=0)
        return february[self.day_month_year]
    def March(self):
        march = pd.read_csv("time_store/March.csv", header=0)
        return march[self.day_month_year]
    def April(self):
        april = pd.read_csv("time_store/April.csv", header=0)
        return april[self.day_month_year]
    def May(self):
        may = pd.read_csv("time_store/May.csv", header=0)
        return may[self.day_month_year]
    def June(self):
        june = pd.read_csv("time_store/June.csv", header=0)
        return june[self.day_month_year]
    def July(self):
        july = pd.read_csv("time_store/July.csv", header=0)
        return july[self.day_month_year]
    def August(self):
        august = pd.read_csv("time_store/August.csv", header=0)
        return august[self.day_month_year]
    def September(self):
        september = pd.read_csv("time_store/September.csv", header=0)
        return september[self.day_month_year]
    def October(self):
        october = pd.read_csv("time_store/October.csv", header=0)
        return october[self.day_month_year]
    def November(self):
        november = pd.read_csv("time_store/November.csv", header=0)
        return november[self.day_month_year]
    def December(self):
        december = pd.read_csv("time_store/December.csv", header=0)
        return december[self.day_month_year]

def merge_dataFrame(df_1=None, df_2=None, df_3=None, df_4=None, df_5=None, df_6=None, df_7=None, df_8=None, df_9=None, df_10=None):
    dataFrame = df_1.append(df_2).append(df_3).append(df_4).append(df_5).append(df_6).append(df_7).append(df_8).append(df_9).append(df_10)
    return dataFrame.to_csv("inverter.csv", index = False)
