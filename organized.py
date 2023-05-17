import os 
import shutil

from_dir = 'C:/Users/Office/Documents/File sorter'
to_dir = 'C:/Users/Office/Desktop/Class 102'

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    name, ext = os.path.splitext(file)

    if ext == '':
        continue
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif'] :
        path1 = from_dir+"/"+file
        path2 = to_dir+'/'+'image_files'
        path3 = to_dir+'/'+'image_files'+'/'+file

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            shutil.move(path1, path3)