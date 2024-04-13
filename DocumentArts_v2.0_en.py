import os

#设计一个文件批量重命名工具程序，其功能是：用户输入文件夹路径，程序遍历文件夹下所有文件；
#用户选择插入类型编号还是插入文本，若选择插入类型编号然后进行编号设置（起始值、依次增量值和位数）；
#若选择插入文本后用户输入要插入的名字，最后用户选择是否执行重命名操作

def batch_rename_files(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)

    # User selects insert type (number or text)
    insert_type = input("Select insert type (1 for number, 2 for text): ")

    if insert_type == "1":
        # User selects number settings
        start_value = int(input("Enter start value: "))
        increment = int(input("Enter increment value: "))
        digits = int(input("Enter number of digits: "))

        # Rename files with number insertion
        for i, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{start_value + i * increment:0{digits}}{file_extension}"
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    elif insert_type == "2":
        # User enters text to insert
        insert_text = input("Enter text to insert: ")

        # Rename files with text insertion
        for file_name in files:
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{insert_text}{file_name}"
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    else:
        print("Invalid insert type selected.")

    # User selects whether to execute renaming operation
    execute_rename = input("Do you want to execute the renaming operation? (y/n): ")

    if execute_rename.lower() == "y":
        print("Renaming files...")
        # Perform renaming operation
        # ...

        print("Files renamed successfully.")
    else:
        print("Renaming operation cancelled.")

# User inputs folder path
folder_path = input("Enter folder path: ")

# Call the batch_rename_files function
batch_rename_files(folder_path)