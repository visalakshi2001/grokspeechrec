from setuptools import setup, find_packages


setup(
    name='tmlc-testapp',
    version='0.0.1',
    license='MIT',
    author="TMLC",
    author_email='visalakshi2001@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/visalakshi2001/tmlc-pypi',
    keywords='example project',
    setup_requires=['vosk', 'pyaudio'],
    install_requires=['vosk', 'pyaudio'],

)