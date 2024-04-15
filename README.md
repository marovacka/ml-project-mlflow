# ml-project-mlflow
#### Cookiecutter template for Machine Learning project supporting mlflow.

Please find all needed information about cookiecutter [here](https://github.com/cookiecutter/cookiecutter).

Install cookiecutter using pip package manager

`python -m pip install --user cookiecutter`

and create project from template directly from Github repository

`python.exe -m cookiecutter -o <destination_path> gh:marovacka/ml-project-mlflow`

Or you can clone repository first

`git clone https://github.com/marovacka/ml-project-mlflow.git`

and create template from directory `{{cookiecutter.project_dir}}` of the local clone using following command

`python.exe -m cookiecutter -o <destination_path> ../`
