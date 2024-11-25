import email

from pkg_resources import require
from pygments.lexers import python
from spacy.cli import project

PyProject = "counsel_package_miraj"
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name=="miraj-raha", email=="septicshocklifebringer@gmail.com" },
]
description = "A small example package"
readme = "README.md"
require-python == "python3"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/Miraj995/counsel_package_miraj.git"
Issues = "https://github.com/pypa/sampleproject/issues"