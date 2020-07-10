import setuptools

with open("README.md", 'r') as readme_file:
    readme = readme_file.read()

# For install_requires
with open("requirements.txt", 'r') as f:
    required = []
    for line in f:
        l = line.strip()
        required.append(l)

setuptools.setup(
    name='samplepkg-schahal',
    version="0.0.2-rc1",
    author="Foo Bar",
    author_email="foobar@example.com",
    description="A sample package to help supercharge a number",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/schahal/sample/",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=required,
    packages=setuptools.find_packages(exclude=['*test*', 'example*', '*sampleapp*']),
    license="License :: Other/Proprietary License",
)
