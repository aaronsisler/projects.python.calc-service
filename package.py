import os

os.system("ls")
os.system("rm -rf dist")
os.system("rm -rf bundle.zip")
os.system("mkdir dist")
os.system("cp -r .venv/lib/python*/site-packages/ dist/")
os.system("rm -rf ./dist/__pycache__")
os.system("find ./dist -maxdepth 1 -type f -delete")
os.system("cp -r src/*.py dist/")
os.system("zip -r bundle.zip ./dist")
os.system("rm -rf ./dist")
