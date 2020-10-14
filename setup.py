from setuptools import setup, find_packages

setup(

	author='ihsan',
	version='0.0.1',
	name='ihsan-twitter',
	packages=find_packages(),
	author_email='ihsanl@pm.me',
	install_requires=['selenium', 'docopt'],
	description='Twitter scraping and stream.',
	url='https://github.com/ihsanturk/ihsan-twitter',
	entry_points={'console_scripts': ['twitter = twitter.cli:main']},

)
