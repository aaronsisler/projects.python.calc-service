import os

os.system("rm -rf dist")
os.system("rm -rf bundle.zip")
os.system("mkdir dist")
os.system("cp -r src/*.py dist/")
os.system("cd dist && zip -r ../bundle.zip .")
