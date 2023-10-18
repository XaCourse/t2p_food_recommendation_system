from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def getRequirements(filepath: str)->List[str]:
    requirements=[]
    with open(filepath) as fileObj:
        requirements=fileObj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='xa kaler',
    author_email='course4xa@gmail.com',
    packages=find_packages(),
    install_requires=getRequirements("requirements.txt")
)