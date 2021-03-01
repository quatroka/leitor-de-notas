from setuptools import setup

setup(
    name='leitor-de-notas',
    version='0.0.1',
    packages=['leitordenotas', 'leitordenotas.builder'],
    url='https://github.com/quatroka/leitor-de-notas',
    license='MIT',
    author='quatroka',
    author_email='monteiro.leonardosantos@gmail.com',
    description='Um simples leitor de notas de corretagem',
    requires=["PyMuPDF"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
