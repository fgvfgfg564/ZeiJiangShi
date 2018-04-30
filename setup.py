from cx_Freeze import setup, Executable

import sys

build_exe_options = {'packages': [], 'includes': []}
  
  
setup(name='test to exe',  
      version = '0.1',  
      description='test from py file to exe file',  
      executables = [Executable("main.py")]  
  
      )  
