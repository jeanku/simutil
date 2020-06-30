import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simutil",
    version="1.0.6",
    author="jeanku, liubing",
    author_email="",
    description="A simple python libs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["simutil", "simutil/Scaffold", "Config"],
    package_data={
        'simutil': [
            'Scaffold/*.txt'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'configparser',
    ],
    keywords='util, libs',
    python_requires='>=3',
)
