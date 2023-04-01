from PyDoTheWorld import * 
from cli_args_system import *
from NativeNotebooks.create_template import *
import  PySchemaKey
import yaml

def main():
    args = Args()
    
    new_project = args.flags_content('new')
    

    if new_project.exist():
        create_template(new_project)
        return 

    copile = args.flags_content('copile')
    if copile.exist():
        notebook_content = load_any_content('notebook.yaml')
        if not notebook_content:
            print('No notebook.yaml file found')
            return
        notebook = yaml.load(notebook_content, Loader=yaml.FullLoader)
        try:
            lang = PySchemaKey.treat_and_get_str(notebook,'main-lang')
            start_flag = PySchemaKey.treat_and_get_str(notebook,'start-flag')
            out_dir = PySchemaKey.treat_and_get_str(notebook,'out-dir')
        except PySchemaKey.PySchemaException as e:
            print(e)
            return