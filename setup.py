from setuptools import setup, find_packages

with open('version.txt') as vtxt:
    version = vtxt.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='leetcodeDriverPY',
    version=version,
    description='A simple library to help people run Leetcode testcases without the Leetcode online IDE.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    project_urls={
        'Github': 'https://github.com/Duve3/leetcodeDriverPY',
        'Issue Tracker': 'https://github.com/Duve3/leetcodeDriverPY/issues',
    },
    author='Duve3',
    author_email='Duv3tabest@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='leetcode',
    packages=find_packages(),
    install_requires=['']
)
