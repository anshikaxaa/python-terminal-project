from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Python Command Terminal - A fully functional command-line terminal"

# Read requirements from requirements.txt
def read_requirements():
    requirements_path = os.path.join(this_directory, 'requirements.txt')
    try:
        with open(requirements_path) as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return ['psutil>=5.9.0']

setup(
    name="python-command-terminal",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A fully functional command-line terminal with AI capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshikaxaa/python-terminal-project",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "pct=terminal_final:main",
            "python-terminal=terminal_final:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
