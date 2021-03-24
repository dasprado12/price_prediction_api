from setuptools import setup


setup(
    name='price_prediction_api',
    description="Exposes prection data",
    author="Daniel Prado, Mateus Leite, Pedro Negrão",
    author_email="danielsprado12@gmail.com, pedron_1997@hotmail.com, ---",
    install_requires=['flask', 'requests', 'uwsgi'],
    python_requires='>=3.6',
)