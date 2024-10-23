import setuptools

setuptools.setup(
    name='dataflow-template',
    version='0.1',
    install_requires=[
        'apache-beam[gcp]==2.46.0',
        'google-cloud-storage==2.10.0',
        'google-cloud-bigquery==3.11.0'
    ],
    packages=setuptools.find_packages(),
)