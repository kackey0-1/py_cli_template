from setuptools import setup

setup(
    name="py_cli_template",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clitool=src.main.cli:main
    ''',
)
