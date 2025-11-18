from setuptools import setup, find_packages

setup(
    name="quantum-core-engine",
    version="2.0.1",
    include_package_data=True,  
    package_data={
        "quantum": ["pytransform/*"],  
    },
    install_requires=[  
        "requests==2.31.0",
        "psutil==6.0.0",
        "GPUtil==1.4.0",
        "boto3==1.34.4",
        "cryptography==43.0.1",
        "portalocker==2.7.0"
    ],
    description=(
        "Quantum CoreEngine is the backbone of QuantumDataLytica’s machine execution framework, "
        "providing essential functionalities for system monitoring, cloud integration, and secure computations."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Quantum Datalytia LLC",
    author_email="itsupport@quantumdatalytica.com",
    url="https://github.com/QuantumDatalytica-LLC/quantum-core-engine.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
)
