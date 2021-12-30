import py_compile
from os import listdir

directory = '.'
files = listdir(directory)

for f in files:
    if f == __file__:
        continue
    elif ".py" in f:
        py_compile.compile(f,f"./socket_cam/{f[0:-3]}.pyc")
        print(f"Success compile the {f} to {f[0:-3]}.pyc")
 