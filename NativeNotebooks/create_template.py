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

    code_dir = input('Inform code dir (type enter for current): ')

    flag_start = input('Inform flag start (type enter for _): ')
    if not flag_start:
        flag_start = '_'
    return {
        '$code-dir$':code_dir,
        '$flag-start$':flag_start,
        '$mainLang$':main_lang,
        '$extension$':extension
    }

def create_template():
    print('Creating new project')

    informations = get_informations()

    path = dirname(abspath(__file__))

    hole_tree = load_json_tree(join(path,'templates.json'))

    
    out_tree = []

    code_dir = informations['$code-dir$']
    if not code_dir:
        code_dir =get_current_dir() 
    
    
    for c in hole_tree:
    
        c_path = c.path.get_path()
        if 'config/'not in c_path:
            continue 
        concated_path = c_path.replace('config/',code_dir + '/')
        c.path.set_path(concated_path)
        content = c.get_content()
        for key,value in informations.items():
            content  = content.replace(key,value)
        c.set_content(content)    
        c.hardware_write()
        out_tree.append(c)
        
    
    for c in hole_tree:
        c_path = c.path.get_path()
        if f'notebooks/{informations["$mainLang$"]}' not in c_path:
            continue

        concated_path = c_path.replace(
            f'notebooks/{informations["$mainLang$"]}',
            code_dir + '/'
        )
        c.path.set_path(concated_path)
        if c.in_memory():
            content = c.get_content()
            for key,value in informations.items():
                content  = content.replace(key,value)
            c.set_content(content)    

        c.hardware_write()
        out_tree.append(c)

    
    report = create_transaction_report(out_tree)
    print('The following files will be created')
    report.represent()
    write = input('Do you want to continue? (y/n): ')
    if write == 'y':
        hardware_commit_tree(out_tree)
        print('Done')
    else:
        print('Aborted')
    