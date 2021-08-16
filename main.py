from create_csv import CreateCSVfile, activeEnergy, MyInverter
import create_csv
from pandas.core.frame import DataFrame
import pandas as pd

CreateCSVfile.Output(
    asset="ABB-111871-3Q15-3720", 
    scope="e5207ce3-5911-4ce3-877f-be4e245e9ddf",
    activeEnergy=activeEnergy.increase_activeEnergy(lastDay_totalEnergy=90000000, web_dailyEnergy=421000)
    )

# CreateCSVfile.Output(
#     asset="ABB-111871-3Q15-3720",
#     scope="e5207ce3-5911-4ce3-877f-be4e245e9ddf",
#     activeEnergy=activeEnergy.decrease_activeEnergy(thamchieu=90000000, web_dailyEnergy=420000)
# )
