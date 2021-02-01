from importlib import reload  

def reload_module(module):
    """It can be a pain to restart a notebook to update an imported
    module - use this to unload and reload a module that has changed"""
    # TODO needs testing to check this works ok inside a function
    reload(module)
    import(module)
