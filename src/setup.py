from distutils.core import setup
import cpioarchive

setup(name='python-cpio',
  version=cpioarchive.version(),
  author="Ignacio Vazquez-Abrams",
  author_email="ivazquez@ivazquez.net",
  maintainer="Ignacio Vazquez-Abrams",
  maintainer_email="ivazquez@ivazquez.net",
  url="http://www.ivazquez.net",
  description="Access to cpio archives",
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: System :: Archiving'
  ],
  py_modules=['cpioarchive'],
  )
