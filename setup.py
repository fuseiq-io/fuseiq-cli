from setuptools import setup, find_packages

setup(
    name="fuseiq-cli",
    version="0.1.0",
    description="FuseIQ CLI — deploy and manage your agents from the terminal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://fuseiq.io",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fuseiq=fuseiq_cli.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
