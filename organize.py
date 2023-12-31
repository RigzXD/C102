import shutil
import os

to_dir = "/Users/rigz/Downloads/C102_assets-main"
from_dir = "/Users/rigz/Downloads/Image_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention == '':
        continue
    if extention in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Image_files'
        path3 = to_dir + '/' + "Image_files" + '/' + file_name
        print("path1",path1)
        print(path2)
        if os.path.exists(path2):
            print("moving " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving " + file_name + "...")
            shutil.move(path1, path3)