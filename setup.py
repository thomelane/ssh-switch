from setuptools import setup


setup(name='ssh-switch',
      version='0.1',
      description='A command line tool to start and stop AWS EC2 instances using SSH aliases.',
      url='https://github.com/thomelane/ssh-switch',
      author='Thom Lane',
      author_email='thom.e.lane@gmail.com',
      packages=['ssh_switch'],
      entry_points={
          'console_scripts': ['ssh-switch=ssh_switch.script:main'],
      })
