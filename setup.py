from setuptools import setup, find_packages
setup(name             = 'SpiffWikiMarkup',
      version          = '0.4.0',
      description      = 'A library for converting between HTML and Wiki text',
      long_description = \
"""
Spiff WikiMarkup is a library that bidirectionally converts between HTML and
Wiki markup language.
""",
      author           = 'Samuel Abels',
      author_email     = 'cheeseshop.python.org@debain.org',
      license          = 'GPLv2',
      package_dir      = {'': 'src'},
      packages         = [p for p in find_packages('src')],
      install_requires = [],
      keywords         = 'spiff wikimarkup wiki markup html convert bidirectional',
      url              = 'http://code.google.com/p/spiff-wikimarkup/',
      classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ])
