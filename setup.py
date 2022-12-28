import setuptools

with open("README.txt", 'r') as fh:
	long_description = fh.read()

classifiers = []

setuptools.setup(
	name = "LePotatoPi.GPIO",
	version = "0.0.2",
	author = "solrobson",
	description = "Le Potato Port of RPi.GPIO to help allow Le Potato Developers to follow coding tutorials",
	long_description = "Gives Libre Le Potato the same interface mapping as RPi.GPIO and the same pin numbers",
	url = "https://github.com/solrobson/le-potato-pi",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"Development Status :: 2 - Pre-Alpha",
		"Intended Audience :: Developers",
		"Topic :: System :: Hardware"
	],
)
