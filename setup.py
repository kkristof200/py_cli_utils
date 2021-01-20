import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'pypi_utils'

setuptools.setup(
    name="pypi_utils",
    version="0.0.0",
    author="Kristof",
    description="pypi_utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/pypi_upgrade",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'new_python_package=pypi_utils.__main__:new_package',
            'npp=pypi_utils.__main__:new_package',

            'upgrade_python_package=pypi_utils.__main__:upgrade',
            'upp=pypi_utils.__main__:upgrade',

            'publish_python_package=pypi_utils.__main__:publish',
            'ppp=pypi_utils.__main__:publish',

            'new_python_subpackage=pypi_utils.__main__:new_subpackage',
            'npsp=pypi_utils.__main__:new_subpackage'

            'clean_python_package=pypi_utils.__main__:clean_lines',
            'cpp=pypi_utils.__main__:clean_lines',


            'new_python_class=pypi_utils.__main__:new_class',
            'npc=pypi_utils.__main__:new_class',

            'new_python_enum=pypi_utils.__main__:new_enum',
            'npe=pypi_utils.__main__:new_enum',

            'new_python_file=pypi_utils.__main__:new_file',
            'npf=pypi_utils.__main__:new_file',

            'new_python_flow=pypi_utils.__main__:new_flow',
            'npfl=pypi_utils.__main__:new_flow'
        ]
    },
    python_requires='>=3.5',
)