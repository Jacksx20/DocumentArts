import os

#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件，用户选择插入，插入类型编号；然后进行编号设置（起始值、依次增量值和位数），最后用户选择是否执行重命名操作
folder_path = input("请输入文件夹路径：")
insert_type = input("请选择插入类型编号（1-前缀插入，2-后缀扩展名插入）：")
start_value = int(input("请输入起始数值："))
increment = int(input("请输入增量值："))
num_digits = int(input("请输入位数："))
rename_files = input("是否执行重命名操作？(Y/N): ")

if rename_files.upper() == "Y":
    file_list = os.listdir(folder_path)
    for i, file_name in enumerate(file_list):
        file_ext = os.path.splitext(file_name)[1]
        if insert_type == "1":
            new_file_name = f"{str(start_value + i * increment).zfill(num_digits)}{file_name}"
        elif insert_type == "2":
            new_file_name = f"{file_name}{str(start_value + i * increment).zfill(num_digits)}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
print("Renaming successful！")
