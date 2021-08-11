#Nhap
from numpy import e

dailyEnergy = [0, 0, 0, 0, 0, 1000, 2000, 2000, 2000, 2000, 4000, 3000, 4000, 5000, 6000, 5000, 7000, 8000, 7000, 14000, 12000, 11000, 7000, 13000, 18000, 12000, 12000, 16000, 18000, 6000, 11000, 18000, 15000, 8000, 15000, 19000, 23000, 23000, 7000, 6000, 7000, 7000, 7000, 7000, 11000, 10000, 9000, 9000, 6000, 
4000, 3000, 0, 0]
# firstValue = int(input("Nhap vao so tham chieu: "))
# totalDailyEnergy = int(input("Nhap vao cong suat ngay: "))
# active_energy = [firstValue]

# print(max(dailyEnergy))
# print(dailyEnergy.count(max(dailyEnergy)))
sothem = 6000
Energy_15m = []
for energy in dailyEnergy:
    if energy == max(dailyEnergy):
        if dailyEnergy.count(max(dailyEnergy)) == 1:
            energy = max(dailyEnergy) + sothem
            phandu = 0
        elif dailyEnergy.count(max(dailyEnergy)) == 2:
            if sothem % 2000 == 0:
                energy = max(dailyEnergy) + int((sothem/2000))*1000
                phandu = 0
            elif sothem % 2000 != 0:
                energy = max(dailyEnergy) + int((sothem//2000))*1000
                phandu = sothem - (sothem//2000)*2000

        elif dailyEnergy.count(max(dailyEnergy)) == 3:
            energy = max(dailyEnergy) + 3000
        Energy_15m.append(energy)
    elif energy != max(dailyEnergy):
        energy = energy
        Energy_15m.append(energy)

sothamchieu = 90000000 
active_energy =  [sothamchieu]
count = 0

if phandu == 0:
    for add in Energy_15m:
        add = active_energy[count] + add
        active_energy.append(add)
        count += 1
elif phandu != 0:
    Energy_15m[26] = Energy_15m[26] + phandu
    for add in Energy_15m:
        add = active_energy[count] + add
        active_energy.append(add)
        count += 1

print(active_energy)
     

# print(sum(dailyEnergy))
# print(Energy_15m)
# print(sum(Energy_15m))






# if totalDailyEnergy - round(max(dailyEnergy)) > 0:
#     a = totalDailyEnergy - round(max(dailyEnergy))
    
# for value in dailyEnergy:
#     value = active_energy[i] + value
#     active_energy.append(value)
#     i += 1

# print(active_energy)

