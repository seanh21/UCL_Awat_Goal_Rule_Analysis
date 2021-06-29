import os
import shutil

os.chdir("\\Users\\Sean\\Desktop\\Google Data Analytics Certificate\\Course 8\\europe-champions-league-master")

file_folder_list = os.listdir()[:-4]

for i in file_folder_list:
    original = r"\Users\Sean\Desktop\Google Data Analytics Certificate\Course 8\europe-champions-league-master" + "\\" + i + "\\" + "new_champs" + i + ".csv"
    target = r"C:\Users\Sean\Desktop\Google Data Analytics Certificate\Course 8\ecl_master_collection" + "\\" + "new_champs" + i + ".csv"
    shutil.move(original,target)