from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HotelReservationPrediction",
    version="0.1.0",
    author="Tejesh Boppana",
    author_email="tejesh.boppana@outlook.com",
    description="A machine learning project for predicting hotel reservations.",
    packages=find_packages(),
    install_requires = requirements,

)