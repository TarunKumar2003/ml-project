from setuptools import setup, find_packages


HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Tarun',
)