#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件；用户选择插入类型编号还是批量重命名，若选择插入类型编号然后进行编号设置（起始值、依次增量值和位数）；若选择批量重命名后用户输入要改的名字以及是否需要添加增量值，若要添加就设置增量值；最后用户选择是否执行重命名操作，显示实时进度及任务卧槽情况
import os

def insert_type_number(file_path, start_value, increment, digits):
    files = os.listdir(file_path)
    for i, file_name in enumerate(files):
        new_name = f"{start_value + i * increment:0{digits}}_{file_name}"
        os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_name))

def batch_rename(file_path, new_name, add_increment, increment_value):
    files = os.listdir(file_path)
    for i, file_name in enumerate(files):
        if add_increment:
            new_name_with_increment = f"{new_name}_{i * increment_value}{os.path.splitext(file_name)[1]}"
            os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_name_with_increment))
        else:
            new_file_name = f"{new_name}{os.path.splitext(file_name)[1]}"
            os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_file_name))

def main():
    folder_path = input("Enter the folder path: ")
    option = input("Choose an option:\n1-Insert type number\n2-Batch rename\nChoose an option:")
    
    if option == "1":
        start_value = int(input("Enter the start value: "))
        increment = int(input("Enter the increment value: "))
        digits = int(input("Enter the number of digits: "))
        insert_type_number(folder_path, start_value, increment, digits)
    elif option == "2":
        new_name = input("Enter the new name: ")
        # add_increment = input("Do you want to add an increment value? (y/n): ")
        # if add_increment.lower() == "y":
            # increment_value = int(input("Enter the increment value: "))
            # batch_rename(folder_path, new_name, True, increment_value)
        # else:
        #     batch_rename(folder_path, new_name, False, 0)
        increment_value = int(input("Enter the increment value: "))
        batch_rename(folder_path, new_name, True, increment_value)
        confirm = input("是否执行重命名操作？（Y/N）：")
        if confirm.upper() == "Y":
            print("正在执行重命名操作...")
        else:
            print("已取消重命名操作。")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
    print("Program executed successfully!")

