import setuptools
from typing import List


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "ML_SmartEngineMonitoringSystem"
AUTHOR_USER_NAME = "darshanadinushal"
SRC_REPO = "EngineHealthPredictor"
AUTHOR_EMAIL = "darshanadinushal@gmail.com"


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Reads the requirements.txt file and returns a list of dependencies.
    Removes '-e .' if present.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)

 