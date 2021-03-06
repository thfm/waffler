from setuptools import setup

setup(
    name="waffler",
    version="0.1",
    description="A small program to help make your writing more sophisticated.",
    long_description=open("README.md").read(),
    py_modules=["waffler"],
    install_requires=["click", "nltk"],
    entry_points="""
        [console_scripts]
        waffle=waffler:waffle
    """
)
