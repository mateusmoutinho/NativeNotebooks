from PyDoTheWorld import * 
from cli_args_system import *
from os.path import abspath,dirname

def main():
    args = Args()
    
    new_project = args.flags_content('new')
    
    if new_project.exist_and_empty():
        print('no folder provided')
        return
    if new_project.exist():
        path = dirname(abspath(__file__))
        templates = f'{path}/template'
        name = new_project.flags()[0]
        tree = create_tree_from_hardware(templates)
        for file in tree:
            dir = file.path.get_dir()
            new_path = dir.replace('template', name)
            
            file.path.set_dir(new_path)
            file.hardware_write()
        hardware_commit_tree(tree)
        return 
main()
