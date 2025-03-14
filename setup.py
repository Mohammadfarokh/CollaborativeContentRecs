from os import environ
from setuptools import setup, find_packages
import site
import sys
import time

# Enabling editable user pip installs
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

# Version
version = "1.2.0"

HASH = environ.get("HASH", None)
if HASH is not None:
    version += ".post" + str(int(time.time()))

install_requires = [
    "notebook>=6.5.5,<8",  # requires ipykernel
    "pandas>2.0.0,<3.0.0",  # Data manipulation
    "pyspark>=3.3.0,<=4",  # Spark for distributed processing
    "scipy>=1.5.0",  # For spatial distance calculations
]

# shared dependencies
extras_require = {
     "spark": [
        "pyarrow>=10.0.1",
        "pyspark>=3.3.0,<=4",
    ],
    "dev": [
        "pytest>=7.2.1",
        "pytest-mock>=3.10.0",  # for access to mock fixtures in pytest
    ]
}

setup(
    name="recommenders",
    version=version,
    extras_require=extras_require,
    install_requires=install_requires,
    python_requires=">=3.6",
    packages=find_packages(include=["myproject", "myproject.*"]),
    setup_requires=["numpy>=1.19"],
)
