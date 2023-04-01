from PyDoTheWorld import * 
from cli_args_system import *

def main():
    args = Args()
    
    new_project = args.flags_content('new')
    
    if new_project.exist_and_empty():
        print('no folder provided')
        return
  
    name = new_project.flags()[0]
    print(name)

main()
