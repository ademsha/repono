from distutils.core import setup

setup(
    name='repono',
    version='0.1',
    packages=['data', 'data.api', 'data.api.tinydb', 'config',
              'export', 'providers', 'providers.api', 'providers.data',
              'providers.extraction', 'providers.extraction.twitter'],
    url='https://github.com/ademsha',
    license='APACHE 2.0',
    author='ademsha',
    author_email='',
    description='Extract useful insights/datasets from Twitter data stream',
    requires=['tweepy', 'tinydb']
)
