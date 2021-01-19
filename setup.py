import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'pypi_upgrade'

setuptools.setup(
    name="pypi_upgrade",
    version="0.0.6",
    author="Kristof",
    description="pypi_upgrade",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/pypi_upgrade",
    packages=setuptools.find_packages(),
    install_requires=["click"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'aloha = pypi_upgrade.pypi_upgrade:hello'
        ]
    },
    python_requires='>=3.5',
)