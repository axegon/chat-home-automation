from codecs import open as fopen
from setuptools import setup, find_packages  # type: ignore
from setuptools import find_namespace_packages, setup  # type: ignore

setup(
    name="chat_home_automation",
    version="0.1.0",
    url="https://axegon.com",
    packages=find_namespace_packages(include=["chat_home_automation.*"]),
    python_requires=">=3.9.2",
    install_requires=fopen("requirements.txt").read().split("/n"),
    package_data={"": ["commitment.html", "py.typed", "*.md"]},
)
