{{cookiecutter.project_name}}
=============================
Machine Learning project generated using Cookiecutter.

Getting started
---------------

It is needed to create conda virtual environment for this project. It is  recommeded to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Use following command to create environment

`conda env create -f environment.yml`

#` conda create -y --name={{cookiecutter.project_dir}} python=3.10 `


and activate it by

`conda activate {{cookiecutter.project_dir}}`

Install your conda environment using ipykernel to be able to set correct kernel in jupyter notebook

`python -m ipykernel install --user --name={{cookiecutter.project_dir}}`

Install all packages of the project into environment.

`pip install .`

