import setuptools

setuptools.setup(
    name='python-kvproto',
    version='0.0.1',
    description='the python classes generated from the pingcap/kvproto',
    author='zyguan',
    author_email='zhongyangguan@gmail.com',
    url='https://github.com/zyguan/python-kvproto',
    packages=setuptools.find_packages(),
    keywords=['kvproto'],
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ),
    install_requires=[
        'grpcio-tools==1.27.1',
        'googleapis-common-protos==1.51.0',
    ],
)
