import os
import pandas as pd

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\ecl_master_collection")

df = pd.read_csv("master_ecl_csv_rev3.csv")
sep_agg_sc = df["∑FT"].str.split("-", n = 1, expand = True)
sep_agg_sc2 = sep_agg_sc[1].str.split("(", n = 1, expand = True)
df["Agg. Home"] = sep_agg_sc[0]
df["Agg. Away"] = sep_agg_sc2[0]

df.to_csv( "master_ecl_csv_rev4.csv", index=False, encoding='utf-8-sig')