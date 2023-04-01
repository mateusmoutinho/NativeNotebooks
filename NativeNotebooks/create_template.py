from PyDoTheWorld import *
from cli_args_system import *
from os.path import abspath,dirname
from os.path import join 
def get_informations():

    main_lang = input('Inform Main language: ')
    loaded_languages = {
        'python':'py',
        'javascript':'js',
        'c':'c',
        'c++':'cpp',
    }
    try:
        extension = loaded_languages[main_lang]
    except KeyError:
        extension = input('Inform extension: ')
        extension = extension.replace('.','')
    out_dir = input('Inform out dir (type enter for current): ')
    
    code_dir = input('Inform code dir (type enter for current): ')

    if not out_dir:
        out_dir = '.'
        
    flag_start = input('Inform flag start (type enter for _): ')
    if not flag_start:
        flag_start = '_'
    return {
        '$code-dir$':code_dir,
        '$flag-start$':flag_start,
        '$mainLang$':main_lang,
        '$extension$':extension,
        '$out-dir$':out_dir
    }

def create_template():
    print('Creating new project')

    informations = get_informations()

    path = dirname(abspath(__file__))
    templates_path = join(path,'templates')

    tree = []
    config_path = join(templates_path,'config')
    config_tree = create_tree_from_hardware(config_path)

    code_dir = informations['$code-dir$']
    if not code_dir:
        code_dir =get_current_dir() 
    
    for c in config_tree:
  
        c_path = c.path.get_path()
        new_cdir_path = c_path.replace(config_path ,'')
        concated_path =  code_dir  + new_cdir_path
        c.path.set_path(concated_path)
        if c.in_memory():
            content = c.get_content()
            for key,value in informations.items():
                content  = content.replace(key,value)
            c.set_content(content)    

        c.hardware_write()
        tree.append(c)

    #ading notebooks
    notebooks_path = join(templates_path,'notebooks')
    
    lang_path = join(notebooks_path,informations['$mainLang$'])
    notebooks_tree = create_tree_from_hardware(lang_path)
    for c in notebooks_tree:
        c_path = c.path.get_path()
        new_cdir_path = c_path.replace(lang_path ,'')
        concated_path =  code_dir  + new_cdir_path
        c.path.set_path(concated_path)
        if c.in_memory():
            content = c.get_content()
            for key,value in informations.items():
                content  = content.replace(key,value)
            c.set_content(content)    

        c.hardware_write()
        tree.append(c)
    
    report = create_transaction_report(tree)
    print('The following files will be created')
    report.represent()
    write = input('Do you want to continue? (y/n): ')
    if write == 'y':
        hardware_commit_tree(tree)
        print('Done')
    else:
        print('Aborted')
    