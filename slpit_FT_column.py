import os
import pandas as pd

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\ecl_master_collection")

# df = pd.read_csv("master_ecl_csv.csv")
# sep_scores_df = df["FT"].str.split("(", n = 1, expand = True)
# df["FT Home"] = sep_scores_df[0]
# df["FT Away"] = sep_scores_df[1]

df = pd.read_csv("master_ecl_csv_rev1.csv")
sep_scores_df = df["FT Away"].str.split("(", n = 1, expand = True)
df["FT Away"] = sep_scores_df[0]

df.to_csv( "master_ecl_csv_rev2.csv", index=False, encoding='utf-8-sig')