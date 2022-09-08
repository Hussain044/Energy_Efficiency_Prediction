from setuptools import setup, find_packages
from typing import List, Dict


def get_requirements_list() -> List[str]:
    """
    This function is going to return a list of requirements from the requirements.txt file

    Returns: This function is hoing to return list which contains name of libraries 
    mentioned in requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


# Declaring variables for setup functions
# we cab also declare variables initially and later assign them in setup function
NAME = 'energy_efficiency_predictor'
REQUIREMENT_FILE_NAME = 'requirements.txt'

setup(
        name=NAME,
        version='0.0.1',
        author='Mohammed Ishtiaq',
        description='Energy efficiency predictor',
        packages=find_packages(),
        install_requires=get_requirements_list()
)
