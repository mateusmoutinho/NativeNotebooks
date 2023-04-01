from PyDoTheWorld import * 

def copile_project(lang:str,start_flag:str,out_dir:str):
    all  = create_tree_from_hardware(get_current_dir(),load_content=False,preserve_content=False)
    formated_tree = []
    for file in all:
        dir = file.path.get_dir()
        extension = file.path.get_extension()
        print(file)


