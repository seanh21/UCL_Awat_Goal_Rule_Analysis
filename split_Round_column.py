import os
import pandas as pd

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\ecl_master_collection")

df = pd.read_csv("master_ecl_csv_rev2.csv")
sep_leg_df = df["Round"].str.split("|", n = 1, expand = True)
df["Stage"] = sep_leg_df[0]
df["Leg"] = sep_leg_df[1]

df.to_csv( "master_ecl_csv_rev3.csv", index=False, encoding='utf-8-sig')