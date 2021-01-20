# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, List
import os

# Local
from .utils import multi_replace

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def update(
    text: str,
    dependencies: Optional[List[str]] = None,
    version_bump_type: int = 0
) -> str:
    current_dependencies_str = '[{}]'.format(text.split('install_requires')[-1].split('=')[-1].lstrip().split('[')[-1].split(']')[0])
    current_version_str = text.split('version=')[-1].split('version =')[-1].split(',')[0].replace('"', '').replace("'", '')

    return text.replace(current_dependencies_str, __dependencies_str(dependencies)).replace(current_version_str, __bumped_version_number(current_version_str, bump_type=version_bump_type))

def generate(
    package_name: str,
    min_python_version: Optional[float] = None,
    max_python_version: Optional[float] = None,
    package_version: Optional[str] = None,
    git_user: Optional[str] = None,
    git_url: Optional[str] = None,
    dependencies: Optional[List[str]] = None,
    short_description: Optional[str] = None
) -> str:
    return multi_replace(__text, {
        '[PACKAGE_NAME]': package_name,
        '[GIT_USER]': git_user or '',
        '[GIT_URL]': git_url or '',
        '[PACKAGE_VERSION]': package_version or '0.0.0',
        '[DEPENDENCIES]': __dependencies_str(dependencies),
        '[SHORT_DESCRIPTION]': short_description or package_name,
        '[MIN_PYTHON_VERSION]': min_python_version or '3.3',
        # '[MAX_PYTHON_VERSION]': max_python_version or __get_var_value(setup_text, 'name', str) if setup_text else '',
    })


# ----------------------------------------------------------- Private methods ------------------------------------------------------------ #

def __dependencies_str(dependencies: List[str]) -> str:
    return '[\n{}{}\n{}]'.format(
        8*' ',
        ',\n{}'.format(8*' ').join(dependencies),
        4*' '
    ) if dependencies else '[]'

def __bumped_version_number(version_number: str, bump_type: int = 0) -> str:
    comps = version_number.split('.')
    bump_index = len(comps)-1-bump_type
    comps[bump_index] = str(int(comps[bump_index]) + 1)

    return '.'.join(comps)

def __get_var_value(s: str, var_name: str, val_type) -> any:
    if var_name not in s:
        return ''

    delimiters = ['"', "'"]
    _s = s.plit(var_name)[0]
    stream = ''
    start_char = None
    last_char = None
    started = False

    for c in _s:
        c = str(c)

        if started:
            if c == start_char and last_char != '\\':
                started = False

                break

            stream += c
        else:
            if c in delimiters:
                start_char = c
                started = True

        last_char = c

    return val_type(stream)

def _get_setup_str(setup_py: str) -> str:
    str = '(' + setup_py.split('setup(')[-1]

def get_str_between(s: str, start: List[str], end: List[str]) -> Optional[str]:
    if isinstance(start, str):
        start = [start]

    if isinstance(end, str):
        end = [end]

    str_delimiters = ['"', "'"]
    stream = ''
    level = -1
    is_in_string = False
    can_end = False

    @property
    def last_char() -> Optional[str]:
        return str(stream[-1]) if len(stream) > 0 else None

    for c in s:
        c = str(c)

        if last_char != '\\':
            if c in start:
                level += 1
            elif c in end:
                level -= 1
                can_end = True

            if c in str_delimiters:
                is_in_string = not is_in_string

        stream += c

        if can_end and level == 0:
            return stream

    return None





# ---------------------------------------------------------- Private properties ---------------------------------------------------------- #

__text = '''
import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = '[PACKAGE_NAME]'

setuptools.setup(
    name='[PACKAGE_NAME]',
    version='[PACKAGE_VERSION]',
    author='[GIT_USER]',
    description='[SHORT_DESCRIPTION]',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='[GIT_URL]',
    packages=setuptools.find_packages(),
    install_requires=[DEPENDENCIES],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=[MIN_PYTHON_VERSION]',
)
'''.strip()


# ---------------------------------------------------------------------------------------------------------------------------------------- #