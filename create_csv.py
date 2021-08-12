from numpy import dtype, flatiter
import pandas as pd
from pandas.core.frame import DataFrame


active_power = pd.read_csv("active_power.csv", header=0)
activePower_numpy = DataFrame(active_power, columns=["active_power"]).values
time = pd.read_csv("time.csv", header=0)
class CreateCSVfile:
    def MyInput(
            asset = None, 
            scope = None, 
            thamchieu = None, 
            web_dailyEnergy = None
            ):

        x = 0
        activePower = []
        for i in activePower_numpy:
            i = float(i)
            activePower.append(i)
            x += 1

        y = 0
        dailyEnergy = []
        for value in activePower:
            if value == 0:
                value = value*0.25 + 0
                dailyEnergy.append(value)
            elif value != 0:
                value = value*0.25 + dailyEnergy[y]
                dailyEnergy.append(value)
                y += 1

        round_dailyEnergy = []
        for eg  in dailyEnergy:
            eg = int(round(eg, -3))
            round_dailyEnergy.append(eg)

        k = 1
        q = 0
        sub_daliyEnergy = []
        for giatri in round_dailyEnergy:
            if giatri == 0:
                giatri = giatri
                sub_daliyEnergy.append(giatri)
            elif giatri != 0:
                giatri = round_dailyEnergy[k] - round_dailyEnergy[q]
                sub_daliyEnergy.append(giatri)
                k += 1
                q += 1

        energy_15p = []
        active_energy = [thamchieu]

        if max(round_dailyEnergy) <= web_dailyEnergy:
            socanbu = web_dailyEnergy - max(round_dailyEnergy)
            for add in sub_daliyEnergy:
                if 0 < socanbu <= 5000:
                    if add == max(sub_daliyEnergy):
                        if sub_daliyEnergy.count(max(sub_daliyEnergy)) == 1:
                            add = max(sub_daliyEnergy) + socanbu
                            phandu = 0
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 2:
                            if socanbu % 2000 == 0:
                                add = max(sub_daliyEnergy) + socanbu
                            elif socanbu % 2000 != 0:
                                add = max(sub_daliyEnergy)  + (socanbu//2000)*1000
                                phandu = socanbu - 2000*(socanbu//2000)
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 3:
                            if socanbu % 3000 == 0:
                                add = max(sub_daliyEnergy) + socanbu
                            elif socanbu % 3000 != 0:
                                add = max(sub_daliyEnergy) + (socanbu//3000)*1000
                                phandu = socanbu - 3000*(socanbu//3000)   
                        else:
                            print(f"Out range for max peak!. Max peak is: {sub_daliyEnergy.count(max(sub_daliyEnergy))}")
                        energy_15p.append(add)
                        
                    elif add != max(sub_daliyEnergy):
                        add = add
                        energy_15p.append(add)             
                    
                elif socanbu > 5000:
                    if add == max(sub_daliyEnergy):
                        if sub_daliyEnergy.count(max(sub_daliyEnergy)) == 1:
                            add = max(sub_daliyEnergy) + (socanbu - (socanbu//5000)*5000)
                            phandu = (socanbu//5000)*5000
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 2:
                            add = max(sub_daliyEnergy) + (socanbu - (socanbu//5000)*5000)
                            phandu = 2*(socanbu//5000)*5000 - socanbu
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 3:
                            add = max(sub_daliyEnergy) + (socanbu - (socanbu//5000)*5000)
                            phandu = 3*(socanbu//5000)*5000 - 2*socanbu
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 4:
                            add = max(sub_daliyEnergy) + (socanbu - (socanbu//5000)*5000)
                            phandu = 4*(socanbu//5000)*5000 - 3*socanbu
                        elif sub_daliyEnergy.count(max(sub_daliyEnergy)) == 5:
                            add = max(sub_daliyEnergy) + (socanbu - (socanbu//5000)*5000)
                        else:
                            print(f"Out range for max peak!. Max peak is: {sub_daliyEnergy.count(max(sub_daliyEnergy))}")
                        energy_15p.append(add)

                    elif add != max(sub_daliyEnergy):
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
            
        elif max(round_dailyEnergy) > web_dailyEnergy:
            socanbu = max(round_dailyEnergy) - web_dailyEnergy 
            for add in sub_daliyEnergy:
                if socanbu >= 0:
                    if add == max(sub_daliyEnergy):
                        add = max(sub_daliyEnergy)
                        phandu = socanbu
                        energy_15p.append(add)
                    elif add != max(sub_daliyEnergy):
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
            dataframe = pd.DataFrame(
                {
                    "time" : time["time"],
                    "asset" : asset,
                    "scope" : scope,
                    "active_power" : [None]*22 + activePower + [None]*19,
                    "active_energy" : [None]*22 + active_energy + [None]*19,
                }
            )
            dataframe.to_csv("inverter.csv", index=False)
            print(f"Successfully!")
        else: 
            print(f"Gia tri tinh toan {max(active_energy) - min(active_energy)} khong trung khop voi gia tri {web_dailyEnergy} tren website hang!!")
