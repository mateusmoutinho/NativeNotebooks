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
    

    all  = create_tree_from_hardware(
        current_dir,
        load_content=False,
        preserve_content=False
    )
    
    formated_tree = []

    if out_dir !='.':
        tree_to_remove = create_tree_from_hardware(
            out_dir,
            load_content=False,
            preserve_content=False
        )
        for file in tree_to_remove:
            file.hardware_remove()
            formated_tree.append(file)

    #print("current dir is",current_dir)
    for file in all:
        
        extension = file.path.get_extension()
        if extension == 'ipynb':
            file.load_content_from_hardware()
            result = copile_file(file.get_content(),lang)
            file.set_content(result)
            file.path.set_extension('py')
            name = file.path.get_name()
            file.path.set_name(start_flag+name)
            file.hardware_write()
           
                    
        if out_dir !='.':
            
            file.load_content_from_hardware()
            origina_path = file.path.get_path()
            


            path = origina_path.replace(current_dir,out_dir +'/')
            file.path.set_path(path)
      
            if out_dir in origina_path:
                continue    
            if 'notebook.yaml' in path:
                continue
            if '.vscode' in path:
                continue
            
            file.hardware_write()
        
        formated_tree.append(file)
    

    t = create_transaction_report(formated_tree)
    t.represent()
    procede = input("procede? (y/n)")
    if procede == 'y':
        hardware_commit_tree(all)
