import distribute_setup
distribute_setup.use_setuptools()

# disables creation of .DS_Store files inside tarballs on Mac OS X
import os
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def setup():
	from setuptools import setup, find_packages
	return setup(
		name = "django-admin-preview",
		version = "0.1.2",
		
		packages = find_packages(),
		setup_requires = [ "setuptools_git >= 0.4.2", ],
		install_requires = open('requirements.txt'),
		entry_points = {
			'setuptools.file_finders'	: [
				'git = setuptools_git:gitlsfiles',
			]
		},
		
		include_package_data = True,
		zip_safe = False,
		
		# metadata for upload to PyPI
		description		= "Inline preview in the admin list view",
		url				= "https://github.com/broderboy/django-admin-preview",
	)

if(__name__ == '__main__'):
	setup()
