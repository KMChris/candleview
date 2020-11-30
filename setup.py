import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CandleView",
    version="0.0.4",
    author="Krzysztof Mizgała",
    author_email="KMChris007@gmail.com",
    description="Candle chart and other stuff",
    url="https://github.com/KMChris",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
