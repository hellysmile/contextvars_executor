import io
import os
import re

from setuptools import setup


def get_version():
    regex = r"__version__\s=\s\'(?P<version>[\d\.ab]+?)\'"

    path = ('contextvars_executor.py',)

    return re.search(regex, read(*path)).group('version')


def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


setup(
    name='contextvars_executor',
    version=get_version(),
    author='Victor Kovtun',
    author_email='hellysmile@gmail.com',
    url='https://github.com/hellysmile/contextvars_executor',
    description='contextvars friendly ThreadPoolExecutor',
    long_description=read('README.rst'),
    py_modules=['contextvars_executor'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['asyncio', 'contextvars'],
)
