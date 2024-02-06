import subprocess

with open('requirements.txt') as f:
    requirements = f.readlines()

for package in requirements:
    package = package.strip()
    subprocess.call(['pip', 'install', package])
