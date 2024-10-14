import polars as pl
import numpy as np
from xlsxwriter import Workbook
# import json

df1 = pl.read_excel(
    source="Interest.xlsx",
    sheet_name="Main Data",
)

df2 = pl.read_excel(
    source="data/2024-10-14.xlsx",
    # schema_overrides={"Période": pl.Utf8,
    #                   "Comptes": pl.Utf8,
    #                   "Catégorie": pl.Utf8,
    #                   "Sous-catégories": pl.Utf8,
    #                   "Note": pl.Utf8,
    #                   "Revenu/dépense": pl.Utf8,
    #                   "Description": pl.Utf8
    #                   },
    sheet_name="Sheet1",
)

# df2.write_excel(column_totals=True, autofit=True)

with Workbook("Interest2.xlsx") as wb:
    # worksheet = wb.add_worksheet()
    df1.write_excel(
        workbook=wb,
        worksheet="Main Data",
        position=(0, 0),  # specify position as (row,col) coordinates
    )
    df2.write_excel(
        workbook=wb,
        worksheet="Tracking",
        position=(0, 0),
        table_style="Table Style Medium 26",
    )

arr = df2.to_numpy()
arr = np.where(arr is None, '', arr)

print(df2)
print(arr)
# arr_list = arr.tolist()

# json_data = json.dumps(arr_list)

# with open('data.json', 'w') as f:
#     f.write(json_data)

# print("Data has been written to 'data.json'.")
