import os

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\europe-champions-league-master")

file_folder_list = os.listdir()[:-4]

for i in file_folder_list:
    os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\europe-champions-league-master" + "\\" + i)
    os.rename(r"champs.csv",r"champs" + i + ".csv")
    print(os.listdir())
