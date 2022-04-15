from setuptools import setup

setup(
    name="py_cli_template",
    version='0.0.2',
    install_requires=[
        'Click',
    ],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'clitool1=main.cli:hello1',
            'clitool2=main.cli:hello2'
        ],
    },
)
