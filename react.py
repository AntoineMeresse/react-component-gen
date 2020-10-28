import os

def check_if_component_direct_exist():
    if not os.path.exists('my_folder'):
        os.makedirs('my_folder')