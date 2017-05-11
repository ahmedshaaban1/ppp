from setuptools import setup, find_packages

setup(name='fib',
      version='0.0.0',
      description='Fibonacci',
      long_description='Run Fibonacci calculations',
      author='Christopher Kotfila',
      author_email='kotfic@gmail.com',
      url='',
      py_modules=['fib'],
      packages=['celery_example'],
      install_requires=[],
      license='Apache 2.0',
      zip_safe=False,
      entry_points= {
          'console_scripts': ['fib=fib:main']
      },
      keywords='ansible')
