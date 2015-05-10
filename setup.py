try:
    from setuptools import setup, find_packages

    def readme():
        with open('README.md') as f:
            return f.read()
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'long_description': readme(),
    'author': 'Martin Hjelmare',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'license': 'GPLv3',
    'author_email': 'marhje52@kth.se',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': find_packages(),
    'include_package_data': True,
    'scripts': ['scripts/path/to/script'],
    'name': 'projectname',
    'zip_safe': False
}

setup(**config)
