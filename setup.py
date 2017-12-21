from setuptools import setup, find_packages
 
setup(
    name = "agite",
    version = "0.1",
    packages=find_packages(),
	entry_points={'scrapy': ['settings = agite_spider.settings']},
    )