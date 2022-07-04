from setuptools import find_packages, setup

setup(
    name='pytorch-zoom-in-network',
    packages=find_packages(exclude=['data']),
    setup_requires=['wheel'],
    install_requires=[
        'opencv-python>=4.5,<4.6',
        'scikit-image==0.19.3',
        'onnx<1.9',
        'pytorch2keras==0.2.4',
        'torch==1.6.0',
        'torchvision==0.7.0'
    ],
    version='0.0.1',
    description="Efficient Classification of Very Large Images with Tiny Objects.",
    author='timqqt @ github',
    author_email='dkamotsky@gmail.com'
)
