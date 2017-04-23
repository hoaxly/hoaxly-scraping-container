# Automatically created by: slyd
"""configures portia project."""

from setuptools import setup, find_packages

setup(
    name='hoaxlyPortia',
    version='1.0',
    packages=find_packages(),
    package_data={
        'spiders': ['*.json', '*/*.json']
    },
    data_files=[('', ['project.json', 'items.json', 'extractors.json'])],
    entry_points={'scrapy': ['settings = spiders.settings']},
    zip_safe=True
)
