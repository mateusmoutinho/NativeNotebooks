from PyDoTheWorld import *

tree = create_tree_from_hardware('templates')
for t in tree:
    path = t.path.get_path()
    formatado = path.replace('templates/','').replace('templates\\','')
    t.path.set_path(formatado)
    if t.in_memory() == False:
        t.ignore()
    
dump_json_tree(
    tree,
    'NativeNotebooks/templates.json',
    preserve_hadware_data=False,
    consider_igonore=False,
    preserve_path_atributes=False
)