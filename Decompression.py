import os
import shutil
import zipfile

#用户输入文件夹路径，读取文件夹下面所有压缩包并把这些压缩包解压到一个新的指定的文件夹中
# 用户输入文件夹路径
folder_path = input("请输入文件夹路径：")

# 用户输入新的指定文件夹路径
output_folder_path = input("请输入新的指定文件夹路径：")

# 遍历文件夹下的所有文件
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # 判断是否为压缩包文件
    if zipfile.is_zipfile(file_path):
        # 解压缩文件到指定文件夹
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder_path)
            print(f"成功解压缩文件: {file_name}")