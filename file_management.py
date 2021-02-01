import os

def get_latest_file(extension='/*'):
    """Whats the most recent file in a directory
    args: str (extension e.g. '/*.xlsx' provide the file extension defaults to all)
    return: str (path to the most recent file)
    """
    list_of_files = glob.glob(bob_moves_path + extension) 
    latest_file = max(list_of_files, key=os.path.getctime)
    return os.path.join(latest_file)
