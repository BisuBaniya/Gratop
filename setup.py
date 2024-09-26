from setuptools import setup, find_packages # type: ignore

setup(
    name='gratop',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # 'psutil',  # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'gratop = gratop.gratop:main',  # Maps 'gratop' command to gratop.py
        ],
    },
    description='Graphical Table of Processes for Linux',
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/yourusername/gratop',  # Optional: Project URL
)
