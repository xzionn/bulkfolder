import os

query = []

print('''
      
                                                                     
,-----.          ,--.,--.    ,------.      ,--.   ,--.               
|  |) /_ ,--.,--.|  ||  |,-. |  .---',---. |  | ,-|  | ,---. ,--.--. 
|  .-.  \|  ||  ||  ||     / |  `--,| .-. ||  |' .-. || .-. :|  .--' 
|  '--' /'  ''  '|  ||  \  \ |  |`  ' '-' '|  |\ `-' |\   --.|  |    
`------'  `----' `--'`--'`--'`--'    `---' `--' `---'  `----'`--'    
by xzionn                                      

      ''')
def get_path():
    try:
        res = input("Do you want to specify a path? (y/n): ").lower()
        if res == "n":
            return os.getcwd()
        else:
            path = input("Enter the path (full path): ")
            return os.path.abspath(path)
    except Exception as e:
        print(f"Error: {e}")
        return None

def dirlist():
    try:
        file_name = input("Enter the file name: ")
        with open(file_name, "r") as name:
            result = name.readlines()
            path_prefix = get_path()
            if path_prefix is None:
                return
            for line in result:
                folder = line.strip('\n')
                query.append(folder)

            for make in query:
                try:
                    not_already_folder_path = os.path.join(path_prefix, make)
                    os.makedirs(not_already_folder_path)
                    print(f"Success create folder {not_already_folder_path}")
                except FileExistsError:
                    folder_path = os.path.join(path_prefix, make + " Already")
                    os.makedirs(folder_path)
                    print(f"Folder {not_already_folder_path} already exists")
    except Exception as e:
        print(f"Error: {e}")

def countdir():
    try:
        count = int(input("Enter the count: "))
        path_prefix = get_path()
        if path_prefix is None:
            return
        for folder in range(count):
            folder_path = os.path.join(path_prefix, str(folder + 1))
            os.makedirs(folder_path)
            print(f"Success create folder {folder_path}")
    except Exception as e:
        print(f"Error: {e}")

try:
    method = input("Choose a method (dirlist/countdir): ").lower()
    if method == 'dirlist':
        dirlist()
    elif method == 'countdir':
        countdir()
    else:
        print("Invalid method chosen.")
except Exception as e:
    print(f"Error: {e}")
