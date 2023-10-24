import os 

def saveData(refreshKey):
    appdata_path = os.getenv("appdata")
    data_directory = os.path.join(appdata_path, 'TestingData')
    try:
        os.makedirs(data_directory, exist_ok=True)
        with open(os.path.join(data_directory, 'data.txt'), 'w') as file:
            file.write(refreshKey)
            print(f'Data directory created at: {data_directory}')
    except Exception as e:
        print(f'Error creating data directory: {str(e)}')

def loadData():
    appdata_path = os.getenv("appdata")
    data_file_path = os.path.join(appdata_path, 'TestingData', 'data.txt')
    try:
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                data = file.read()
                print(f'Data loaded from file: {data}')
                return data
        else:
            print(f'Data file not found at: {data_file_path}')
            return None
    except Exception as e:
        print(f'Error loading data: {str(e)}')
        return None
def removeData():
    appdata_path = os.getenv("appdata")
    data_directory = os.path.join(appdata_path, 'TestingData')
    file_path = os.path.join(data_directory, 'data.txt')
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f'File {file_path} removed successfully')
        except Exception as e:
            print(f'Error removing file: {str(e)}')
    else:
        print(f'File {file_path} does not exist.')