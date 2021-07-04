
from setuptools import setup, find_packages
from pathlib import Path

project_root = Path(__file__).resolve().parent

about = {}
version_path = project_root / 'adaptive' / '__version__.py'
with version_path.open() as f:
    exec(f.read(), about)

setup(
    name='adaptive',
    author=about['__author__'],
    license=about['__license__'],
    version=about['__version__'],
    url='https://github.com/scwolof/adaptive',
    packages=find_packages(exclude=['tests']),
    install_requires=['numpy>=1.7'],
    setup_requires=['numpy>=1.7'],
    tests_require=['pytest-runner', 'pytest', 'pytest-cov'],
)