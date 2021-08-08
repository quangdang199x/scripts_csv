from numpy import dtype, flatiter
import pandas as pd
from pandas.core.frame import DataFrame


df_1 = pd.read_csv("new_info.csv", header=0)
activePower_numpy = DataFrame(df_1, columns=["active_power"]).values

df_2 = pd.read_csv("inverter1.csv", header=0)

x = 0
y = 0
dailyEnergy = []
activePower = []

for i in activePower_numpy:
    i = float(i)
    activePower.append(i)
    x += 1

for value in activePower:
    if value == activePower[0]:
        value = value*0.25 + 0
        dailyEnergy.append(value)
    elif value != activePower[0]:
        value = value*0.25 + int(dailyEnergy[y])
        dailyEnergy.append(value)
        y += 1

for n in dailyEnergy:
    print(n)




# list_Asset = [input("Nhap vao Asset: ")]
# list_Scope = [input("Nhap vao Scope: ")]

# dataframe = pd.DataFrame(
#     {
#         "time" : df_2["time"],
#         "asset" : list_Asset*53,
#         "scope" : list_Scope*53,
#         "active_power" : df_1["active_power"],
#         "active_energy" :  dailyEnergy,
#     }
# )
# dataframe.to_csv("my_data.csv", index=False)
