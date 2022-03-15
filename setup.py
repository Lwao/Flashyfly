from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Flashyfly package to build and flash firmware in production environment'
LONG_DESCRIPTION = 'Flashyfly package to build and flash firmware in production environment working as a CLI wrapper for Platformio objecting ease of use and speed to deploy firmware in a hardware platform'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="flashyfly", 
        version=VERSION,
        author="Levy Gabriel",
        author_email="levygsg@hotmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['platformio','typer'], # add any additional packages that 
        
        keywords=['python', 'build', 'flash', 'firmware', 'hardware'],
        classifiers= [ # https://pypi.org/classifiers/
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
        ]
) 

# python setup.py sdist bdist_wheel
# twine upload dist/*
# twine upload --skip-existing dist/*