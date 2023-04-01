from PyDoTheWorld import * 
from cli_args_system import *
from NativeNotebooks.create_template import create_template
from NativeNotebooks.copile_project import copile_project
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
            default = {
                'main-lang':'python',
                'start-flag':'_',
                'out-dir':'$'
            }
            notebook_content = yaml.dump(default)
            write_any_content('notebook.yaml',notebook_content)
        
        
        notebook = yaml.load(notebook_content, Loader=yaml.FullLoader)
        try:
            lang = PySchemaKey.treat_and_get_str(notebook,'main-lang',default='python')
            start_flag = PySchemaKey.treat_and_get_str(notebook,'start-flag',default='_')
            out_dir = PySchemaKey.treat_and_get_str(notebook,'out-dir',default='$')
        except PySchemaKey.PySchemaException as e:
            print('Error in notebook.yaml file')
            print(e)
            return 
        copile_project(lang,start_flag,out_dir)