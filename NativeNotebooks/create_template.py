from PyDoTheWorld import *
from cli_args_system import *
from os.path import abspath,dirname




def create_template(new_project:FlagsContent):
    print('Creating new project')
    path = dirname(abspath(__file__))
    templates = f'{path}/template'
    current_dir = get_current_dir() + '/'
        
    if new_project.filled():
        name = new_project._args[0]
        current_dir = name
        
        tree = create_tree_from_hardware(templates)
        for file in tree:
            file.path.set_dir(current_dir)
            file.hardware_write()
            
        hardware_commit_tree(tree)
