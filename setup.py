import setuptools

setuptools.setup(
    name="pinakinathc_py",
    version="0.0.1",
    author="Pinaki Nath Chowdhury",
    author_email="mail@pinakinathc.me",
    description="A utility library.",
    url="http://www.pinakinathc.me",
    project_urls={
        "Bug Tracker": "https://github.com/pinakinathc/pinakinathc_py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
)
