from setuptools import setup, find_packages

setup(
    name='SimplexMethod',
    version='1.0',
    description='Implementation of the simplex method algorithm for solving linear programming problems',
    license='MIT',
    author='Demid Antipin',
    author_email='antipindemid@inbox.ru',
    url='https://github.com/DemidAntipin/SimplexMethod',
    packages=find_packages(),
    install_requires=['numpy'],
    tests_require=['pytest'],
    python_requires='>=3',
)
