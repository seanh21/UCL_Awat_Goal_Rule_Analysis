import pandas as pd
import os

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\europe-champions-league-master")

file_folder_list = os.listdir()[:-4]

for i in file_folder_list:
    os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\europe-champions-league-master" + "\\" + i)
    f=pd.read_csv("champs" + i + ".csv")
    keep_col = ['Round', 'Date', 'Team 1', 'FT', 'HT', 'Team 2', '∑FT', 'ET', 'P']
    new_f = f[keep_col]
    new_f.to_csv("new_champs" + i + ".csv", index=False)