try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Stefan Ristovski',
    'url': 'https://github.com/Ricky995/MyProject',
    'download_url': 'https://github.com/Ricky995/MyProject',
    'author_email': 'ristovskistefan95@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
