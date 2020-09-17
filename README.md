# Fake Tweets Generation.

Using Transformers (GPT-2) to create fake tweets based on 2016 US elections. This is a project for research purposes.

This project use a virtual environment, so you need to have Python 3.7 installed. And then in order to create the environment needed for this project (with all the dependencies) just run:
```
pipenv install
```

Everything you do, you need to do it inside and interactive shell provided by pipenv. To activate it, just run:

```
pipenv shell
```

Inside that shell you could run `jupyter notebook` to open a Jupyter Notebook (with all the dependencies installed) and execute all the notebooks inside the project.

In order to create the datasets needed to train the model, just open `preprocessing.ipynb` and execute every block, you should end up with three datasets: train, test and validation. Train and validation are the ones used in the training process.

All the work related with the model is done withing a Google Colab environment. Just open the notebook `tfm_transformer.ipynb` and click the button `Open in Colab`. The only thing you need to take into account is, to copy to a Google Drive (linked with Colab), the folder transformer and the dataset for train and validation. Then just follow the blocks inside the notebook.

At the end you will end up with tweets generated with the topic of the US_elections.
