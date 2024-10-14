import pandas as pd

def hello_{{cookiecutter.project_dir}}():
    print(f"hello {{cookiecutter.project_dir}}")

def get_wine_dataset():
    white_df = pd.read_csv("../data/winequality-white.csv", delimiter=';')
    white_df['is_red'] = 0
    red_df =  pd.read_csv("../data/winequality-red.csv", delimiter=';')
    red_df['is_red'] = 1
    wine_dataset_df = pd.concat((white_df, red_df))    

    return wine_dataset_df
    