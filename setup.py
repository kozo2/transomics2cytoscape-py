import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transomics2cytoscape", # Replace with your own username
    version="0.0.1",
    author="Kozo Nishida",
    author_email="knishida@riken.jp",
    description="A tool set for 3D Trans-Omic network visualization with Cytoscape",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ecell/transomics2cytoscape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.1',
)