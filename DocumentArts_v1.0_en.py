import os
#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件，用户选择插入类型编号还是重命名，若选择插入类型编号然后进行编号设置（起始值、依次增量值和位数）；若选择重命名后用户输入要改的名字，最后用户选择是否执行重命名操作
def insert_type_number(folder_path, start_value, increment, digits):
    files = os.listdir(folder_path)
    for index, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{start_value + index * increment:0{digits}}{file_extension}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

def rename_files(folder_path, new_name):
    files = os.listdir(folder_path)
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{new_name}{file_extension}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

def main():
    folder_path = input("Enter the folder path: ")
    choice = input("Enter '1' to insert type number or '2' to rename: ")
    
    if choice == '1':
        start_value = int(input("Enter the start value: "))
        increment = int(input("Enter the increment value: "))
        digits = int(input("Enter the number of digits: "))
        insert_type_number(folder_path, start_value, increment, digits)
    elif choice == '2':
        new_name = input("Enter the new name: ")
        rename_files(folder_path, new_name)
    else:
        print("Invalid choice.")
    
    execute_rename = input("Do you want to execute the renaming operation? (y/n): ")
    if execute_rename.lower() == 'y':
        print("Renaming operation executed successfully.")
    else:
        print("Renaming operation cancelled.")

if __name__ == "__main__":
    main()