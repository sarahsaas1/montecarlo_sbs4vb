from setuptools import setup, find_packages

setup(
    name='Montecarlo_sbs4vb',
    url= 'https://github.com/sarahsaas1/montecarlo_sbs4vb.git',
    author='Sarah Saas',
    author_email='sbs4vb@virginia.edu',
    description='Montecarlo Final Project Package',
    packages=find_packages(),    
    install_requires=['numpy',
    'pandas'],
)