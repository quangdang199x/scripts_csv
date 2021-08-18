from create_csv import Inverter, merge_dataFrame
import pandas as pd
from pandas.core.frame import DataFrame
import sys

if __name__ == "__main__":
    total_dailyEnergy_site = None

    inverter_1 = Inverter(dataframe=DataFrame(
        Inverter.read_file, 
        columns=["PVS-100-TL-OUTD SN 115179-3Q15-4020"]).values, 
        latest_day_energy=90000000, 
        web_dailyEnergy=539000
    )
    df_1 = inverter_1.create_CSV_files(
        asset="ABB-115179-3Q15-4020", 
        scope="b107e879-e80b-499d-9e12-2b8c0a6cb4bf"
    )

    inverter_2 = Inverter(dataframe=DataFrame(
        Inverter.read_file, 
        columns=["PVS-100-TL-OUTD SN 115190-3Q15-4020"]).values, 
        latest_day_energy=80000000, 
        web_dailyEnergy=486000
    )
    df_2 = inverter_2.create_CSV_files(
        asset="ABB-115190-3Q15-4020", 
        scope="b107e879-e80b-499d-9e12-2b8c0a6cb4bf"
    )

    inverter_3 = Inverter(dataframe=DataFrame(
        Inverter.read_file, 
        columns=["PVS-100-TL-OUTD SN 115228-3Q15-4020"]).values, 
        latest_day_energy=70000000, 
        web_dailyEnergy=538000
    )
    df_3 = inverter_3.create_CSV_files(
        asset="ABB-115228-3Q15-4020", 
        scope="b107e879-e80b-499d-9e12-2b8c0a6cb4bf"
    )


    check_value = inverter_1.check_value() + inverter_2.check_value() + inverter_3.check_value()
    if check_value == total_dailyEnergy_site:
        merge_dataFrame(df_1,df_2,df_3)
        print(f"Successfully! Total daily energy: {check_value}kWh.")
    else:
        print(f"Error! Total daily energy: {check_value}kWh does not equal total_dailyEnery_site: {total_dailyEnergy_site}kWh.")
