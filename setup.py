from setuptools import setup, Extension


with open("README.md", "r") as file:
    long_description = file.read()


dev_status = {
    "Alpha": "Development Status :: 3 - Alpha",
    "Beta": "Development Status :: 4 - Beta",
    "Pro": "Development Status :: 5 - Production/Stable",
    "Mature": "Development Status :: 6 - Mature",
}


setup(
    name="MedCab",
    packages=['app', 'pickles'],
    author="Robert Sharp",
    author_email="webmaster@sharpdesigndigital.com",
    version="0.0.1",
    description="MedCab | Cannabis Suggestion Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Free for non-commercial use",
    platforms=["Darwin", "Linux"],
    classifiers=[
        dev_status["Alpha"],
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)
