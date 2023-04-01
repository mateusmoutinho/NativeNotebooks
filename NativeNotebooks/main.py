from PyDoTheWorld import * 
from cli_args_system import *
from os.path import abspath,dirname

def main():
    args = Args()
    
    new_project = args.flags_content('new')
    

    if new_project.exist():
        print('Creating new project')
        path = dirname(abspath(__file__))
        templates = f'{path}/template'
        current_dir = get_current_dir() + '/'
        tree = create_tree_from_hardware(templates)
        for file in tree:
            file.path.set_dir(current_dir)
            file.hardware_write()
        
        hardware_commit_tree(tree)
        return 
