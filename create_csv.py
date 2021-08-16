from numpy import dtype, flatiter
import pandas as pd
from pandas.core.frame import DataFrame
import sys

def input_time():
    time = pd.read_csv("time.csv", header=0)
    return time["time"]

class MyInverter:
    active_power = pd.read_csv("active_power.csv", header = 0)
    input_activePower = DataFrame(active_power, columns = ["active_power"]).values
    def setInverter(self, active_power):
        self.input_activePower = active_power
    def getInverter(self):
        return self.input_activePower

inverter_1 = MyInverter()
inverter_2 = MyInverter()
inverter_3 = MyInverter()
inverter_4 = MyInverter()
inverter_5 = MyInverter()
inverter_1.setInverter(DataFrame(MyInverter.active_power, columns=["active_power"]).values)
inverter_2.setInverter(DataFrame(MyInverter.active_power, columns=["active_power_2"]).values)
inverter_2.setInverter(DataFrame(MyInverter.active_power, columns=["active_power_3"]).values)
inverter_2.setInverter(DataFrame(MyInverter.active_power, columns=["active_power_4"]).values)
inverter_2.setInverter(DataFrame(MyInverter.active_power, columns=["active_power_5"]).values)

def activePower():
    activePower = []
    for i in inverter_1.getInverter():
        i = float(i)
        activePower.append(i)
    return activePower

def dailyEnergy():
    y = 0
    dailyEnergy = []
    for value in activePower():
        if value == 0:
            value = value*0.25 + 0
            dailyEnergy.append(value)
        elif value != 0:
            value = value*0.25 + dailyEnergy[y]
            dailyEnergy.append(value)
            y += 1
    return dailyEnergy

def round_DailyEnergy():
    round_dailyEnergy = []
    for eg  in dailyEnergy():
        eg = int(round(eg, -3))
        round_dailyEnergy.append(eg)
    return round_dailyEnergy

def subtract_dailyEnergy():
    k = 1
    q = 0
    sub_dailyEnergy = []
    for giatri in round_DailyEnergy():
        if giatri == 0:
            giatri = giatri
            sub_dailyEnergy.append(giatri)
        elif giatri != 0:
            giatri = round_DailyEnergy()[k] - round_DailyEnergy()[q]
            sub_dailyEnergy.append(giatri)
            k += 1
            q += 1
    return sub_dailyEnergy

class activeEnergy:
    def increase_activeEnergy(lastDay_totalEnergy = None, web_dailyEnergy = None):    
        energy_15min= []
        active_energy = [lastDay_totalEnergy]
        count = 0
        m = 0
        for add in subtract_dailyEnergy():
            add = add
            energy_15min.append(add)
        if max(round_DailyEnergy()) <= web_dailyEnergy:
            socanbu = web_dailyEnergy - max(round_DailyEnergy())
            while count != (socanbu/1000):
                energy_15min[20+count] = energy_15min[20+count] + 1000
                count += 1
        elif max(round_DailyEnergy()) > web_dailyEnergy:
            socanbu = max(round_DailyEnergy) - web_dailyEnergy
            if 0 not in activePower[19:45]:
                while count != (socanbu/1000):
                    energy_15min[20+count] = energy_15min[20+count] - 1000
                    count += 1
            else:
                print(f"Co gia tri power bang 0!")

        for energy in energy_15min:
            energy  = active_energy[m] + energy
            active_energy.append(energy)
            m += 1
        active_energy.pop(0)
        if max(active_energy) - min(active_energy) == web_dailyEnergy:
            return active_energy
        else:
            return sys.exit()

    def decrease_activeEnergy(lastDay_totalEnergy = None, web_dailyEnergy = None):
        energy_15min = []
        active_energy = [lastDay_totalEnergy]
        count = 0
        m = 0
        for add in subtract_dailyEnergy():
            add = add
            energy_15min.append(add)
        if max(round_DailyEnergy()) <= web_dailyEnergy:
            socanbu = web_dailyEnergy - max(round_DailyEnergy())
            while count != (socanbu/1000):
                energy_15min[20+count] = energy_15min[20+count] + 1000
                count += 1
            energy_15min.pop(0)
            energy_15min.append(0)
            energy_15min.reverse()
        elif max(round_DailyEnergy()) > web_dailyEnergy:
            socanbu = max(round_DailyEnergy()) - web_dailyEnergy
            if 0 not in activePower[19:45]:
                while count != (socanbu/1000):
                    energy_15min[20+count] = energy_15min[20+count] - 1000
                    count += 1
                energy_15min.pop(0)
                energy_15min.append(0)
                energy_15min.reverse()
            else:
                print(f"Co gia tri power bang 0!")

        for energy in energy_15min:
            energy = active_energy[m] - energy
            active_energy.append(energy)
            m += 1
        active_energy.pop(0)
        active_energy.reverse()
        if max(active_energy) - min(active_energy) == web_dailyEnergy:
            return active_energy
        else:
            return sys.exit()

class CreateCSVfile:
    def Output(asset = None, scope = None, activeEnergy = None):     
            dataframe = pd.DataFrame(
                {
                    "time" : input_time(),
                    "asset" : asset,
                    "scope" : scope,
                    "active_power" : [None]*22 + activePower() + [None]*19,
                    "active_energy" : [None]*22 + activeEnergy + [None]*19,
                }
            )
            dataframe.to_csv("inverter.csv", index=False)
            print(f"Successfully!")       
