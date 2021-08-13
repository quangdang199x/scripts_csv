from numpy import dtype, flatiter, result_type
import pandas as pd
from pandas.core.frame import DataFrame
import sys

def input_activePower():
    active_power = pd.read_csv("active_power.csv", header=0)
    activePower_numpy = DataFrame(active_power, columns=["active_power"]).values
    return activePower_numpy

def input_time():
    time = pd.read_csv("time.csv", header=0)
    return time["time"]

def activePower():
    x = 0
    activePower = []
    for i in input_activePower():
        i = float(i)
        activePower.append(i)
        x += 1
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
    def increase_activeEnergy(thamchieu = None, web_dailyEnergy = None):    
        energy_15p = []
        active_energy = [thamchieu]

        if max(round_DailyEnergy()) <= web_dailyEnergy:
            socanbu = web_dailyEnergy - max(round_DailyEnergy())
            for add in subtract_dailyEnergy():
                if 0 < socanbu <= 5000:
                    if add == max(subtract_dailyEnergy()):
                        if subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 1:
                            add = max(subtract_dailyEnergy()) + socanbu
                            phandu = 0
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 2:
                            if socanbu % 2000 == 0:
                                add = max(subtract_dailyEnergy()) + socanbu
                            elif socanbu % 2000 != 0:
                                add = max(subtract_dailyEnergy())  + (socanbu//2000)*1000
                                phandu = socanbu - 2000*(socanbu//2000)
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 3:
                            if socanbu % 3000 == 0:
                                add = max(subtract_dailyEnergy()) + socanbu
                            elif socanbu % 3000 != 0:
                                add = max(subtract_dailyEnergy()) + (socanbu//3000)*1000
                                phandu = socanbu - 3000*(socanbu//3000)   
                        else:
                            print(f"Out range for max peak!. Max peak is: {subtract_dailyEnergy().count(max(subtract_dailyEnergy()))}")
                        energy_15p.append(add)
                        
                    elif add != max(subtract_dailyEnergy()):
                        add = add
                        energy_15p.append(add)             
                    
                elif socanbu > 5000:
                    if add == max(subtract_dailyEnergy()):
                        if subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 1:
                            add = max(subtract_dailyEnergy()) + (socanbu - (socanbu//5000)*5000)
                            phandu = (socanbu//5000)*5000
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 2:
                            add = max(subtract_dailyEnergy()) + (socanbu - (socanbu//5000)*5000)
                            phandu = 2*(socanbu//5000)*5000 - socanbu
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 3:
                            add = max(subtract_dailyEnergy()) + (socanbu - (socanbu//5000)*5000)
                            phandu = 3*(socanbu//5000)*5000 - 2*socanbu
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 4:
                            add = max(subtract_dailyEnergy()) + (socanbu - (socanbu//5000)*5000)
                            phandu = 4*(socanbu//5000)*5000 - 3*socanbu
                        elif subtract_dailyEnergy().count(max(subtract_dailyEnergy())) == 5:
                            add = max(subtract_dailyEnergy()) + (socanbu - (socanbu//5000)*5000)
                        else:
                            print(f"Out range for max peak!. Max peak is: {subtract_dailyEnergy().count(max(subtract_dailyEnergy()))}")
                        energy_15p.append(add)

                    elif add != max(subtract_dailyEnergy()):
                        add = add              
                        energy_15p.append(add)   

            if 0 < socanbu <= 5000:
                count = 0
                if phandu == 0: 
                    for energy in energy_15p:
                        energy = active_energy[count] + energy
                        active_energy.append(energy)
                        count += 1
                elif phandu != 0:
                    energy_15p[26] = energy_15p[26] + phandu 
                    for energy in energy_15p:
                        energy = active_energy[count] + energy
                        active_energy.append(energy)
                        count += 1
            elif socanbu > 5000:
                count = 0
                m = 0
                if phandu == 0: 
                    for energy in energy_15p:
                        energy = active_energy[count] + energy
                        active_energy.append(energy)
                        count += 1
                elif phandu != 0:
                    while m != (((socanbu//5000)*5000)/1000):
                        energy_15p[20+m] = energy_15p[20+m] + 1000
                        m += 1          
                    for energy in energy_15p:
                        energy = active_energy[count] + energy
                        active_energy.append(energy)
                        count += 1   
            
        elif max(round_DailyEnergy()) > web_dailyEnergy:
            socanbu = max(round_DailyEnergy()) - web_dailyEnergy 
            for add in subtract_dailyEnergy():
                if socanbu >= 0:
                    if add == max(subtract_dailyEnergy()):
                        add = max(subtract_dailyEnergy())
                        phandu = socanbu
                        energy_15p.append(add)
                    elif add != max(subtract_dailyEnergy()):
                        add = add
                        energy_15p.append(add)

            count = 0
            m = 0
            if 0 not in activePower[19:45] and phandu != 0:
                while m != (socanbu/1000):
                    energy_15p[20+m] = energy_15p[20+m] - 1000
                    m += 1 
                for energy in energy_15p:
                    energy = active_energy[count] + energy         
                    active_energy.append(energy)
                    count += 1
            elif phandu == 0:
                energy_15p = energy_15p
                for energy in energy_15p:
                    energy = active_energy[count] + energy
                    active_energy.append(energy)
                    count += 1
            else:
                print("Co gia tri power bang 0.")

        delete_firstvalue = active_energy.pop(0)
        if max(active_energy) - min(active_energy) == web_dailyEnergy:
            return active_energy
        else:
            print(f"Gia tri tinh toan {max(active_energy) - min(active_energy)} khong trung khop voi gia tri {web_dailyEnergy} tren website hang!!")
            sys.exit()

    def decrease_activeEnergy(thamchieu = None, web_dailyEnergy = None):
        energy_15min = []
        active_energy = [thamchieu]
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
            energy_15min.reverse()
        elif max(round_DailyEnergy()) > web_dailyEnergy:
            socanbu = max(round_DailyEnergy()) - web_dailyEnergy
            if 0 not in activePower[19:45]:
                while count != (socanbu/1000):
                    energy_15min[20+count] = energy_15min[20+count] - 1000
                    count += 1
                energy_15min.reverse()
            else:
                print(f"Co gia tri power bang 0!")
        
        for energy in energy_15min:
            energy = active_energy[m] - energy
            active_energy.append(energy)
            m += 1
        active_energy.pop(0)
        active_energy.reverse()
        return active_energy

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
