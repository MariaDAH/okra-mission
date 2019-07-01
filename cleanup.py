import os
from path import Path

BASEDIR = os.path.abspath(os.path.dirname(__file__))

d = Path(BASEDIR) 

for i in d.walk():
    if i.isdir():
        if i.name == '__pycache__':
            if i.parent.name == 'okra':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'geoservice':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'okrabusiness':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'dashboards':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'fatsecret':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'okramission':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'users':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            elif i.parent.name == 'okra-mission':
                files = i.walkfiles("*.pyc")
                for file in files:
                    print(i.parent.name + i.name)
                    file.remove()
                    print("Removed {} file".format(file))
            else:
                pass
            

d1 = Path(BASEDIR+'/env/Lib') 

for i in d1.walk():
    if i.isdir():
        if i.name == '__pycache__':
            files = i.walkfiles("*.pyc")
            for file in files:
                print(i.parent.name + i.name)
                file.remove()
                print("Removed {} file".format(file))