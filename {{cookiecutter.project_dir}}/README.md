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

Install all packages of this project into activated environment.

`pip install .`

MLFlow requires installed `make` utility. Please check whether you have`make` installed on your operating system (OS).
Run the following in your command line

`make --version`

Install `make` if it isn't installed on your OS, for example using Chocolatey package manager. You can download `.msi` installation file from
`https://github.com/chocolatey/choco/releases/`

Then run cmd in administrator mode and install `make`

`choco install make`

Run jupyter notebook `./notebooks/wine_classification_recipe.ipynb` to experiment with example recipe. The recipe contains all necesarry steps to train model for wine classification task.

Feel free to create your own project recipe in the directory `recipes/{{cookiecutter.project_name}}`.
Please notice that the directory `{{cookiecutter.project_name}}` is meant to be directory for the project package.
