from setuptools import setup

PACKAGE = 'freedomsponsors-trac-plugin'
VERSION = '0.1'

setup(name=PACKAGE,
      version=VERSION,
      packages=['freedomsponsors'],
      entry_points={'trac.plugins': '%s = freedomsponsors' % PACKAGE},
)