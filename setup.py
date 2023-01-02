from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='leetcodeDriverPY',
    version='1.0.0',
    description='A simple library to help people run Leetcode testcases without the Leetcode online IDE.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    github='https://github.com/Duve3/leetcodeDriverPY',
    issue_tracker='https://github.com/Duve3/leetcodeDriverPY/issues',
    author='Duve3',
    author_email='',
    license='MIT',
    classifiers=classifiers,
    keywords='leetcode',
    packages=find_packages(),
    install_requires=['']
)
