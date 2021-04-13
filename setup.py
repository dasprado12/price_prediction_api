from setuptools import setup

setup(
    name='price_prediction_api',
    description="Exposes prection data",
    author="Daniel Prado, Pedro Negrão, Mateus Leite",
    author_email="danielsprado12@gmail.com, pedron_1997@hotmail.com, mateuspedrosa38@gmail.com",
    install_requires=['flask', 'requests', 'uwsgi', 'tensorflow-cpu', 'keras', 'pandas', 'numpy'],
    python_requires='>=3.6',
)