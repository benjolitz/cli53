from setuptools import setup

__version__ = '0.3.1'
long_description = file('README','r').read()

setup(name='cli53',
      version=__version__,
      description='Command line script to administer the Amazon Route 53 DNS service',
      long_description=long_description,
      license='MIT',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://github.com/barnybug/cli53/',
      install_requires=['boto', 'argparse', 'dnspython'],
      scripts=['scripts/cli53'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
      )
