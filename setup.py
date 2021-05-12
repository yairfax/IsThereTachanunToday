from setuptools import setup, find_packages

setup(
    name='istheretachanuntoday',
    version='1.0.0',
    url='http://www.istheretachanuntoday.com/',
    license='MIT',
    author='Yair Fax',
    author_email='yairshop@gmail.com',
    description='A website to tell you whether or not there is tachanun on a given day.',
    long_description ='file: README.md',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pyluach',
        'njdate @ git+https://github.com/schorrm/njdate.git#egg=njdate',
        'requests'
    ],
    test=[
        'pytest'
    ],
    package_data={
        "": ["resources/*.json", "templates/*", "static/*"]
    }
)