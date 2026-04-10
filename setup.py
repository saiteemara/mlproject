## setup.py is a build script used by Python packaging tools (setuptools)
## "Make my project behave like a pip-installable library"

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:         # Why remove -e . in setup.py?
            requirements.remove("-e .")    # -e . is not a library It’s an installation instruction.

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Sai",
    author_email='teemarasai49@gmail.com',
    packages=find_packages(),  # Automatically finds all folders with __init__.py
    install_requires=get_requirements('requirements.txt')
)