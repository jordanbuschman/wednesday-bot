from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='wednesday-bot',
    version='1.0',
    author='Jordan Buschman',
    url='https://github.com/jordanbuschman/wednesday-bot',
    description='Lambda function to wish you a custom Wednesday message (my dudes)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    data_files=['.env'],
    install_requires=['discord.py', 'python-dotenv'],
    setup_requires=['lambda_setuptools'],
    python_requires='>=3.6',
    lambda_function='wednesday.wednesday:lambda_wednesday',
    lambda_module='wednesday',
)
