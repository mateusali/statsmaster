from setuptools import setup, find_packages

setup(
    name="statsmaster",
    version="0.1.0",
    description="A powerful statistics library",
    author="Mateus Augusto da Silva Ali Fontes",
    author_email="mateusalifontes@gmail.com",
    url="https://github.com/mateusali/statsmaster",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
