import os
import pandas as pd

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\ecl_master_collection")

df = pd.read_csv("master_ecl_csv_rev3.csv")
# is_leg1 = df["Leg"] == " Leg 1"
# df_leg1 = df[is_leg1]
#
# df_leg1.to_csv( "master_ecl_csv_leg1.csv", index=False, encoding='utf-8-sig')

is_leg2 = df["Leg"] == " Leg 2"
df_leg2 = df[is_leg2]

df_leg2.to_csv( "master_ecl_csv_leg2.csv", index=False, encoding='utf-8-sig')