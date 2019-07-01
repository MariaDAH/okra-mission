from setuptools import setup, find_packages

#installation file
setup(
    name='okra',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    url="https://localhost:5000",
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

