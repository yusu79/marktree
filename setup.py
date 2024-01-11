from setuptools import setup
from setuptools import find_packages

with open("README.md", "r",encoding='utf-8') as f:
    readme = f.read()

setup(
    name='marktree',
    version='1.0.0',
    description='convert headings in a Markdown file (.md) into a tree-like structure and output.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/yusu79/marktree',
    author='yusu79',
    author_email='yusu79oss@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'marktree=marktree:main',
        ],
    },
)



