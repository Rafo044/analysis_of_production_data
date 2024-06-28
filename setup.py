from setuptools import setup, find_packages

# requirements.txt read
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='analysis_of_production_data',
    version='0.1',
    author='Rafael Alikhanli',
    author_email='rafo044@protonmail.com',
    description='Data analysis project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rafo044/analysis_of_production_data',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),  
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.9',
    ],
)

