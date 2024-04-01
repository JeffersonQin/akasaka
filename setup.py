from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("version", "r", encoding="utf-8") as fh:
    version = fh.read().strip()

def make_email(name, domain):
    return f"{name}@{domain}"


setup(
    name="akasaka",
    version=version,
    author="Haoyun Qin",
    author_email=make_email("qhy.cis", "gmail.com"),
    description="Dynamic mutiprocess preprocessing task loader and dispatcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffersonQin/akasaka",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'akasaka = akasaka.main:main'
        ]
    },
    install_requires=[
        'tqdm'
    ]
)
