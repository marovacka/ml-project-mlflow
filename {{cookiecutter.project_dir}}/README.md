{{cookiecutter.project_name}}
=============================
Machine Learning project generated using Cookiecutter.

Getting started
---------------

It is needed to create conda virtual environment for this project. It is  recommeded to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) package manager.

Use following command to create environment

`conda env create -f environment.yml`


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

Run cmd in administrator mode and install `make`

`choco install make`

After all instalation steps, you can run `src/{{cookiecutter.project_dir}}/main.py` script to see whether your package `{{cookiecutter.project_dir}}` is installed properly

`python src/{{cookiecutter.project_dir}}/main.py`

you should see the following message 

`hello {{cookiecutter.project_dir}}`

Run jupyter notebook `./notebooks/wine_classification_recipe.ipynb` to experiment with example recipe. The recipe contains all necesarry steps to train model for wine classification task.
Don't forget to set python kernel `{{cookiecutter.project_dir}}` in open notebook.

Feel free to create your own project recipe in a subdirectory inside `recipes/{{cookiecutter.project_dir}}`.
