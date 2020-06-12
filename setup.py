 from setuptools import setup

 setup(
   name='nlp-helper',
   version='0.1.0',
   author='Marco Staschik',
   author_email='marco.staschik@gmail.com',
   packages=['nlp-helper', 'nlp-helper.test'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/nlp-helper/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   #long_description=open('README.txt').read(),
   install_requires=[
        "spacy = *"
        "pandas = *"
        "pathlib = *"
   ],
)