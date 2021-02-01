import os
import glob

def get_latest_file(directory, extension='/*'):
    """Whats the most recent file in a directory
    args: 
        extension: str (extension e.g. '/*.xlsx' provide the file extension defaults to all)
        directory: str (path to the directory needs to end in '\\')
        
    return: str (path to the most recent file)
    """
    list_of_files = glob.glob(directory + extension) 
    latest_file = max(list_of_files, key=os.path.getctime)
    return os.path.join(latest_file)
