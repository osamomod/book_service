from setuptools import setup, find_packages

setup(
    name="book_service_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Osamo",
    author_email="osamo@tut.by",
    description="Клиентская библиотека для работы с Book Service API",
)
