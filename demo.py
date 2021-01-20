# from kcu import sh, kjson
# from selenium_facebook import facebook

# class Package:
#     def __init__(
#         self,
#         name: str,
#         version: str
#     ):
#         self.name = name
#         self.version = version

#     def get_install_name(self, include_version: bool = False) -> str:
#         return '{}{}'.format(self.name, '=={}'.format(self.version) if include_version else '')

#     @property
#     def versioned_name(self) -> str:
#         return '{}=={}'.format(self.name, self.version)

# class GitPackage(Package):
#     def __init__(
#         self,
#         name: str,
#         version: str,
#         git_url: str
#     ):
#         self.name = name
#         self.version = version
#         self.git_url = git_url

#     @property
#     def get_install_name(self, include_version: bool = False):
#         return '{} @ git+{}'.format(super().get_install_name(include_version=include_version), self.git_url)

# from pipreqs import pipreqs
# # class Dependencies:

# all_imports = pipreqs.get_all_imports('.')
# pkg_names = pipreqs.get_pkg_names(all_imports)
# imports_info = pipreqs.get_imports_info(pkg_names)

# print('all_imports ', all_imports)
# print('pkg_names   ', pkg_names)
# print('imports_info', imports_info)
# # kjson.save
# # print(pipreqs.get_imports_info(pipreqs.get_pkg_names()))
# # print(sh.sh('pipreqs --force'))








# s='''
# import setuptools, os

# readme_path = 'README.md'

# if os.path.exists(readme_path):
#     with open(readme_path, "r") as f:
#         long_description = f.read()
# else:
#     long_description = 'pypi_utils'

s='''
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

            'clean_python_package=pypi_utils.__main__:clean_lines',
            'cpp=pypi_utils.__main__:clean_lines',


            'new_python_class=pypi_utils.__main__:new_class',
            'npc=pypi_utils.__main__:new_class',

            'new_python_enum=pypi_utils.__main__:new_enum',
            'npe=pypi_utils.__main__:new_enum',

            'new_python_file=pypi_utils.__main__:new_file',
            'npf=pypi_utils.__main__:new_file',

            'new_python_flow=pypi_utils.__main__:new_flow',
            'npfl=pypi_utils.__main__:new_flow',
        ]
    },
    python_requires='>=3.5',
)
'''.strip()



from typing import Optional, List

# def get_setup_str(setup_py: str) -> str:
#     s = '(' + setup_py.split('setup(')[-1]

# def get_str_between(s: str, start: List[str], end: List[str]) -> Optional[str]:
#     if isinstance(start, str):
#         start = [start]

#     if isinstance(end, str):
#         end = [end]

#     str_delimiters = ['"', "'"]
#     stream = ''
#     level = -1
#     is_in_string = False
#     can_end = False

#     @property
#     def last_char() -> Optional[str]:
#         return str(stream[-1]) if len(stream) > 0 else None

#     for c in s:
#         c = str(c)

#         if last_char != '\\':
#             if c in start:
#                 level += 1
#             elif c in end:
#                 level -= 1
#                 can_end = True

#             if c in str_delimiters:
#                 is_in_string = not is_in_string

#         stream += c

#         if can_end and level == 0:
#             return stream

#     return None


# import tokenize
# import io

# # s = s.split('setup(')[-1]


# for token in tokenize.generate_tokens(io.StringIO(s).readline):
#     if token.type == 1:
#         print(token)



def setup(**kwargs):
	#code to insert the dictionary into your database
	print(kwargs)

def parse_setup(text):
	'''unmatched parenthesis, even inside string literals, will break this'''
	start = text.find('setup(')
	text = text[start:] #cut off anything before
	stack = 0
	for idx, char in enumerate(text[6:], 7):
		if char == ")":
			if stack:
				stack -= 1
			else:
				break
		elif char == "(":
			stack += 1

	return text[:idx] #cut off anything behind

#open the unknown setup.py, parse it, execute it. 
with open('setup.py') as f:
	eval(parse_setup(f.read()))