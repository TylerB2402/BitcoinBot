import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BitcoinBot",
    version="0.0.1",
    author="Tyler Beddow",
    author_email="tylerleebeddow@gmail.com",
    description="Bot for referencing bitcoin information on discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TylerB2402/BitcoinBot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)