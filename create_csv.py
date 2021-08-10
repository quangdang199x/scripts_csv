from os import error
from numpy import dtype, flatiter
import pandas as pd
from pandas.core.frame import DataFrame


df_1 = pd.read_csv("new_info.csv", header=0)
activePower_numpy = DataFrame(df_1, columns=["active_power"]).values

df_2 = pd.read_csv("inverter1.csv", header=0)

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

web_dailyEnergy = 422000 #int(input("Nhap vao so dailyEnergy tren Website: "))
energy_15p = []
if max(round_dailyEnergy) <= web_dailyEnergy:
    socanbu = web_dailyEnergy - max(round_dailyEnergy)
    for add in sub_daliyEnergy:
        if socanbu <= 5000:
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
                    print(f"Out range!!")
                energy_15p.append(add)
                
            elif add != max(sub_daliyEnergy):
                add = add
                energy_15p.append(add)
               
        elif 5000 < add < 15000:
            pass
        
        
    pass
    
elif max(round_dailyEnergy) > web_dailyEnergy:
    socanbu = max(round_dailyEnergy) - web_dailyEnergy     

    pass

thamchieu = 90000000 #Example, dung function or input() 
active_energy = [thamchieu]
count = 0
for energy in energy_15p:
    energy = active_energy[count] + energy
    active_energy.append(energy)
    count += 1

delete_firstvalue = active_energy.pop(0)

if max(active_energy) - min(active_energy) == web_dailyEnergy:
    list_Asset = [input("Nhap vao Asset: ")]
    list_Scope = [input("Nhap vao Scope: ")]
    dataframe = pd.DataFrame(
        {
            "time" : df_2["time"],
            "asset" : list_Asset*53,
            "scope" : list_Scope*53,
            "active_power" : df_1["active_power"],
            "active_energy" :  active_energy,
        }
    )
    dataframe.to_csv("inverter.csv", index=False)
    print(f"Successfully!")
else: 
    print(f"Gia tri tinh toan {max(active_energy) - min(active_energy)} khong trung khop voi gia tri {web_dailyEnergy} tren website hang!!")
             