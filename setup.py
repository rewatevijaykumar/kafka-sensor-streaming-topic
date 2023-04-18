from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Sensor Fault Detection'
VERSION = '0.0.1'
AUTHOR = 'Vijaykumar Rewate'
AUTHOR_EMAIL = 'rewatevijaykumar@gmail.com'
DESCRIPTION = 'Sensor Fault Detection using Machine Learning'
HYPEN_E_DOT = '-e .'
REQUIREMENTS_FILE = 'requirements.txt'

def get_requirements(file_path:str)->List[str]:
    '''
    Returns a list of requirement packages mentioned in the requirements.txt file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('/n','') for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements(REQUIREMENTS_FILE),
)