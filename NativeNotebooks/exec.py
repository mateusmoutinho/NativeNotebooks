from PyDoTheWorld import * 
from cli_args_system import *
from NativeNotebooks.create_template import *


def main():
    args = Args()
    
    new_project = args.flags_content('new')
    

    if new_project.exist():
        create_template(new_project)
        return 

    copile = args.flags_content('copile')
    if copile.exist():
        
        pass
    