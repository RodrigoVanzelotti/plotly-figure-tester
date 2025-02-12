from setuptools import find_packages, setup

setup(
    name='plotly_figure_tester',
    packages=find_packages(include=['plotly_figure_tester']),
    version='0.1.0',
    description='Plotly Wrapper for Figure Testing',
    author='Rodrigo Vanzelotti',
    install_requires=[
        "plotly>=6.0.0,<7.0.0",
        "plotly[express]>=6.0.0,<7.0.0",
        "dash>=2.18.2,<3.0.0",
    ],
    setup_requires=['pytest'],
    tests_require=['pytest>=8.3.4,<9.0.0'],
    test_suite='tests',
)