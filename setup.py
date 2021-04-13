from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="barcodeSpliter",
    version="1.6",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description = '"barcodeSpliter" can use barcode label to \
        separate different samples in mixed-sample sequencing.',
    author = "Haopeng Yu",
    author_email = "atlasbioin4@gmail.com",
    url = "https://github.com/atlasbioinfo/barcodeSpliter",
    license='Apache-2.0',
    entry_points = {
        'console_scripts' : [
            'barcodeSpliter = barcodeSpliter:main'
        ]
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data = {
        '':['*.gz','*.tsv']
    },
    python_requires='>=3.6',
)
