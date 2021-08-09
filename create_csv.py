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
    eg = round(eg)
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



list_Asset = [input("Nhap vao Asset: ")]
list_Scope = [input("Nhap vao Scope: ")]

dataframe = pd.DataFrame(
    {
        "time" : df_2["time"],
        "asset" : list_Asset*53,
        "scope" : list_Scope*53,
        "active_power" : df_1["active_power"],
        "active_energy" :  round_dailyEnergy,
        "sub_dailyEnergy" : sub_daliyEnergy,
    }
)
dataframe.to_csv("my_data.csv", index=False)

              