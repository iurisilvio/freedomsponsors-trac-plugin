from setuptools import setup

PACKAGE = 'freedomsponsors-trac-plugin'
VERSION = '0.1'

try:
    long_description = open("README.md").read()
except:
    long_description = ''

setup(name=PACKAGE,
      version=VERSION,
      packages=['freedomsponsors'],
      entry_points={'trac.plugins': '%s = freedomsponsors' % PACKAGE},
      description="FreedomSponsors Trac plugin",
      long_description=long_description,
      author='Iuri de Silvio',
      author_email='iurisilvio@gmail.com',
      url='http://github.com/iurisilvio/%s' % PACKAGE,
      keywords='trac plugin',
      license='MIT',
      zip_safe=False,
)

