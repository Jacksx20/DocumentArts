#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件；
#用户选择插入类型编号还是批量重命名，若选择插入类型编号然后进行编号设置（起始值、依次增量值和位数）；
#若选择批量重命名后用户输入要改的名字以及增量值，最后用户选择是否执行重命名操作

import os

def insert_type_number(folder_path, start_value, increment, digits):
    file_list = os.listdir(folder_path)
    for index, file_name in enumerate(file_list):
        new_name = f"{start_value + index * increment:0{digits}}_{file_name}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

def batch_rename(folder_path, new_name, increment):
    file_list = os.listdir(folder_path)
    for index, file_name in enumerate(file_list):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{new_name}_{index * increment}{file_extension}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

def main():
    folder_path = input("请输入文件夹路径：")
    operation = input("请选择操作类型（1-插入类型编号，2-批量重命名）：")
    
    if operation == "1":
        start_value = int(input("请输入起始值："))
        increment = int(input("请输入增量值："))
        digits = int(input("请输入位数："))
        insert_type_number(folder_path, start_value, increment, digits)
    elif operation == "2":
        new_name = input("请输入新的文件名：")
        increment = int(input("请输入增量值："))
        batch_rename(folder_path, new_name, increment)
    else:
        print("无效的操作类型！")
        return
    
    confirm = input("是否执行重命名操作？（Y/N）：")
    if confirm.upper() == "Y":
        print("正在执行重命名操作...")
    else:
        print("已取消重命名操作。")

if __name__ == "__main__":
    main()
    print("程序执行完毕！")