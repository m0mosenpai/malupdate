from setuptools import setup, find_packages

setup(
    name="malupdate",
    version="0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3"],

    # metadata to display on PyPI
    author="Sarthak Khattar",
    author_email="sarthakoct@gmail.com",
    description="Package to interact with MyAnimeList using the Official API",
    keywords="hello world example examples",
    url="https://github.com/m0mosenpai/malupdate",   # project home page, if any

    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    # could also include long_description, download_url, etc.
)