import json 
from PyDoTheWorld import * 

def copile_file(file_content:str,lang:str)->set:
    formated = ''
    file_loaded = json.loads(file_content)
    cels = file_loaded['cells']
    for cel in cels:
        if  cel['cell_type'] == 'code':
            code = ''.join(cel['source'])
            formated += "\n"+code
    return formated

def copile_project(current_dir:str, lang:str,start_flag:str,out_dir:str):
    all  = create_tree_from_hardware(current_dir,load_content=False,preserve_content=False)

    formated_tree = []
    for file in all:
        dir = file.path.get_dir()
        extension = file.path.get_extension()
        if extension == 'ipynb':
            file.load_content_from_hardware()
            result = copile_file(file.get_content(),lang)
            file.set_content(result)
            file.path.set_extension('py')
            

