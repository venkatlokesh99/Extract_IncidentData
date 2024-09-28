setup(
	name='project0',
	version='1.0',
	author='Venkat Lokesh Vejendla',
	author_email='vvejendla@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs', 'resources')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
