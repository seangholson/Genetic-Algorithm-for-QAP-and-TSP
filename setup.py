from os import path
from setuptools import setup


pwd = path.abspath(path.dirname(__file__))
with open(path.join(pwd, 'README.md'), 'r') as f:
    readme = f.read()


setup(
    name='Genetic-Algorithm-for-QAP-and-TSP',
    version='0.1.0',
    description='A genetic algorithm for QAP and TSP using a sorting network encoding',
    long_description=readme,
    long_description_content_type='test/markdown',
    url='git@github.com:seangholson/Genetic-Algorithm-for-QAP-and-TSP.git',
    author='Sean Gholson, Group W, Inc.',
    author_email='sgholson@groupw.com',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords='Genetic Algorithm',
    project_urls={
        'Documentation': 'git@github.com:seangholson/Genetic-Algorithm-for-QAP-and-TSP.git',
        'Source': 'git@github.com:seangholson/Genetic-Algorithm-for-QAP-and-TSP.git',
        'Bugs': 'https://github.com/seangholson/Genetic-Algorithm-for-QAP-and-TSP/issues',
        'Say hi!': 'mailto:sgholson@groupw.com',
    },
    packages=[
        'data',
        'examples',
        'genetic_algorithm',
        'utilities',
    ],
    python_requires='>=3.5, <4',
    install_requires=[
        'numpy',
        'pandas'
    ],
)
