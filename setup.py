from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="barcodeSpliter",
    version="1.9.3",
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
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # include_package_data=True,
    # package_data = {
    #     'data':["*.gz","*.tsv"]
    # },
    # data_files=[("./data/",["barcode.tsv","test_r1.fastq.gz","test_r2.fastq.gz"])],
    python_requires='>=3.6',
)
