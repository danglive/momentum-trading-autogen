# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="momentum-trading-autogen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "matplotlib>=3.5.0",
        "yfinance>=0.2.0",
        "ag2>=0.7.0",
        "streamlit>=1.22.0",
        "plotly>=5.13.0",
        "jupyter>=1.0.0",
        "seaborn>=0.12.0",
        "pandas-datareader>=0.10.0",
        "requests>=2.28.0",
        "diskcache>=5.6.0"  # Used by AutoGen
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        'console_scripts': [
            'momentum-analysis=examples.momentum_cli:main',
        ],
    },
    author="Van Tuan Dang",
    author_email="vantuandang1990@gmail.com",
    description="Momentum Trading Strategy Analysis with AutoGen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danglive/momentum-trading-autogen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    package_data={
        "": ["*.md", "*.yaml", "*.csv", "*.json", "*.png"],
        "templates": ["*.html"],
        "data": ["*.csv"],
    },
)