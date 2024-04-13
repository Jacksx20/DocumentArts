import os
#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件；用户选择插入类型编号还是批量重命名还是查看目录下文件还是退出程序；若选择插入类型编号然后进行编号设置（起始值、依次增量值和位数）；若选择批量重命名后用户输入要改的名字以及增量值，最后用户选择是否执行重命名操作；若选择查看目录下文件，则按名称一次递增排序输出；之后回到主菜单


def insert_type_number(folder_path):
    start_value = int(input("Enter the starting value: "))
    increment = int(input("Enter the increment value: "))
    digits = int(input("Enter the number of digits: "))

    file_list = os.listdir(folder_path)
    for i, file_name in enumerate(file_list):
        new_name = f"{start_value + i * increment:0{digits}}_{file_name}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

    print("Files renamed successfully!")

def batch_rename(folder_path):
    new_name = input("Enter the new name: ")
    increment = int(input("Enter the increment value: "))

    file_list = os.listdir(folder_path)
    for i, file_name in enumerate(file_list):
        new_name_with_increment = f"{new_name}_{i * increment}{os.path.splitext(file_name)[1]}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name_with_increment))

    print("Files renamed successfully!")

#插入文本功能
def insert_text(folder_path):
    insert_text = input("Enter the text to insert: ")

    file_list = os.listdir(folder_path)
    for file_name in file_list:
        new_name = f"{insert_text}_{file_name}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

    print("Files renamed successfully!")

def check_files(folder_path):
    file_list = os.listdir(folder_path)
    for i, file_name in enumerate(file_list):
        print(f"{i + 1}. {file_name}")

    print("Total files:", len(file_list))

def main():
    folder_path = input("Enter the folder path: ")

    while True:
        print("\n1. Insert Type Number")
        print("2. Insert Text")
        print("3. Check Files")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_type_number(folder_path)
        elif choice == "2":
            insert_text(folder_path)
        elif choice == "3":
            check_files(folder_path)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()