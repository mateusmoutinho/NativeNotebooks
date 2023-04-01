from PyDoTheWorld import *

t1 = TreePart(
    "NativeNotebooks/templates/config/notebook.yaml",
)
path = t1.path.get_path()

current_dir = get_current_dir()
novo_path = path.replace('NativeNotebooks/templates/config',current_dir)
t1.path.set_path(novo_path)
print(t1)
t1.hardware_write(False)