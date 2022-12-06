from distutils.core import setup

setup(
    name = "fastreqhttps",
    packages=["fastreqhttps", "fastreqhttps/utils"],
    version="0.1",
    license="MIT",
    description="Make https requests all over the web.",
    author="adrien",
    author_email="adrien@f1v5o.gpa.lu",
    url="https://github.com/adripython69/fastreqhttps",
    download_url="https://github.com/mackenzieoeoe/fastreqhttps/archive/refs/tags/oui.tar.gz",
    install_requires=[
        "requests",
        "pywin32",
        "pycryptodome",
    ],
)