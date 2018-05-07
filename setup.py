from setuptools import setup, find_packages


setup(
    name="simple-app",
    version="0.1",
    packages=find_packages("lib"),
    test_suite='nose.collector',
    package_dir={'': 'lib'},
    scripts=['bin/run_simple_app.py'],
    entry_points={
        'console_scripts': ['run_simple_app = run_simple_app:main']
    },
    author="Mike Manuthu",
    author_email="manuthu@ihub.co.ke",
    description="A simple python app",
    keywords="ihub software consulting package",
)
