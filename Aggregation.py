import os
import pandas as pd

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\ecl_master_collection")

file_list = os.listdir()

master_ecl_csv = pd.concat([pd.read_csv(i) for i in file_list])

master_ecl_csv.to_csv( "master_ecl_csv.csv", index=False, encoding='utf-8-sig')
