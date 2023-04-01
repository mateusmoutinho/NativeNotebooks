from PyDoTheWorld import *

tree = list_all_recursively('templates')
dump_json_tree(
    tree,
    'NativeNotebooks/templates.json'
)