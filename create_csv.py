import pandas as pd

df = pd.DataFrame(
    {
        "Time":["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Asset":["ABB-8051","ABB-8051","ABB-8051","ABB-8051","ABB-8051","ABB-8051","ABB-8051"],
        "Scope":["CSVfile08082021","CSVfile08082021","CSVfile08082021","CSVfile08082021","CSVfile08082021","CSVfile08082021","CSVfile08082021"],
        "ActivePower":[200, 350, 450, 515, 532, 670, 890],
    }
)
df.to_csv("new_info.csv", index=False)
# df = pd.read_csv(input("Nhap vao CSV_file: "), header=0, index_col=False)
# print(df)
# df.to_csv("new_info.csv", index=False)
# print(df.columns)