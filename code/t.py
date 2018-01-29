import pandas as pd
# The file has no headers naming the columns, so we pass header=None # and provide the column names explicitly in "names"
data = pd.read_csv(
        "/home/andy/datasets/adult.data", header=None, index_col=False,
        names=['age', 'workclass', 'fnlwgt', 'education',  'education-num',
               'marital-status', 'occupation', 'relationship', 'race', 'gender',
               'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
               'income'])
# For illustration purposes, we only select some of the columns
data = data[['age', 'workclass', 'education', 'gender', 'hours-per-week',
             'occupation', 'income']]
# IPython.display allows nice output formatting within the Jupyter notebook
display(data.head())
