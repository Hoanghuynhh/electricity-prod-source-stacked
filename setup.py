import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install','--upgrade','pip', 'setuptools'])

import pkg_resources

required  = {'customtkinter','numpy', 'matplotlib'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
