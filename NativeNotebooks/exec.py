from PyDoTheWorld import * 

from NativeNotebooks.create_template import create_template
from NativeNotebooks.copile_project import copile_project
import  PySchemaKey
import yaml
from sys import argv
def main():
    
    if 'new' in argv:
        create_template()
        return 
    
    
    elif 'copile' in argv:
        notebook_content = load_any_content('notebook.yaml')
        if not notebook_content:
            notebook_content = yaml.dump({
                'main-lang':'python',
                'start-flag':'_',
                'out-dir':'$'
            })
            write_any_content('notebook.yaml',notebook_content)
    
        notebook = yaml.load(notebook_content, Loader=yaml.FullLoader)
        try:
            lang = PySchemaKey.treat_and_get_str(notebook,'main-lang')
            start_flag = PySchemaKey.treat_and_get_str(notebook,'start-flag')
            out_dir = PySchemaKey.treat_and_get_str(notebook,'out-dir')
        except PySchemaKey.PySchemaException as e:
            print('Error in notebook.yaml file')
            print(e)
            return 
        copile_project(
            get_current_dir(),
            lang,
            start_flag,
            out_dir
        )
    else:
        print('Command not found')
        print('Commands: new, copile')