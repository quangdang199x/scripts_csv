import pandas as pd
from pandas.core.frame import DataFrame
import sys

class Inverter:
    read_file = pd.read_csv("download.csv", header = 0)
    def __init__(self, dataframe = None, latest_day_energy = None, web_dailyEnergy = None):
        self.dataframe = dataframe
        self.latest_day_energy = latest_day_energy
        self.web_dailyEnergy = web_dailyEnergy
    
    def input_time(self):
        time = pd.read_csv("time.csv", header=0)
        return time["time"]

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
            if 0 not in self.get_power_inverter()[19:45]:
                while count_1 != (comp/1000):
                    energy_15min[20+count_1] = energy_15min[20+count_1] - 1000
                    count_1 += 1
            else:
                return sys.exit()

        for energy in energy_15min:
            energy = active_energy[count_2] + energy
            active_energy.append(energy)
            count_2 += 1
        active_energy.pop(0)
        if max(active_energy) - min(active_energy) == self.web_dailyEnergy:
            return active_energy
        else:
            return sys.exit()

    def create_CSV_files(self, asset = None, scope = None):
        dataframe = pd.DataFrame(
            {
                "time" : self.input_time(),
                "asset" : asset,
                "scope" : scope,
                "active_power" : [None]*22 + self.get_power_inverter() + [None]*19,
                "active_energy" : [None]*22 + self.increase_activeEnergy() + [None]*19,
            }
        )
        return dataframe      
        