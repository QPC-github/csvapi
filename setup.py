from setuptools import setup, find_packages

TESTS_REQUIRE = [
    'requests-mock==1.4.0',
    'pytest==3.5.0',
    'aiohttp==3.1.3',
    'pytest-asyncio==0.8.0',
]

setup(
    name='csvapi',
    description='An instant JSON API for your CSV',
    author='Alexandre Bulté',
    version='0.0.1.dev',
    license='MIT',
    url='https://github.com/abulte/csvapi',
    packages=find_packages(),
    package_data={'csvapi': []},
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'click_default_group==1.2',
        'requests==2.18.4',
        'agate==1.6.1',
        'agate-sql==0.5.3',
        'validators==0.12.1',
        'agate-excel==0.2.2',
        'Quart==0.6.6',
        'cchardet==2.1.1',
    ],
    entry_points='''
        [console_scripts]
        csvapi=csvapi.cli:cli
    ''',
    tests_require=TESTS_REQUIRE,
    extras_require={
        'test':  TESTS_REQUIRE,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
