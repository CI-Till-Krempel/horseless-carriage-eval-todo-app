from setuptools import setup, find_packages

setup(
    name="todo_app",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==3.0.2",
        "Flask-SQLAlchemy==3.1.1",
        "pytest==8.0.0",
        "pytest-flask==1.3.0",
    ],
)
