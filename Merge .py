import os
import shutil

#用户输入所要读取的文件夹，将文件夹中的各个子文件夹下的文件合并到一个新的文件夹中
# 用户输入要读取的文件夹路径
folder_path = input("请输入要读取的文件夹路径: ")

# 用户输入要合并到的新文件夹路径
new_folder_path = input("请输入要合并到的新文件夹路径: ")

# 遍历文件夹中的子文件夹
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 获取文件的绝对路径
        file_path = os.path.join(root, file)
        # 将文件复制到新文件夹中
        shutil.copy(file_path, new_folder_path)
print("文件合并成功！")