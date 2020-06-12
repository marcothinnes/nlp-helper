from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)


def split_text_into_columns(nlp_models, df) -> None:
    """
    Takes Text Content of one DataFrame Cell and splits into multiple Columns

    Args:
        nlp_models (list): List of Spacy Language Models
        df (Pandas DataFrame): [description]

    Returns:
        Pandas Dataframe: concatenated Dataframe
    """
    import pandas as pd

    nlp_models = nlp_models

    df['sentences'] = 'default value'

    for nlp_model in nlp_models:

        for index, row in df.iterrows():

            list1 = []
            list1.clear()

            for sentence in nlp_model(row['content']).sents:
                #print(sentence)

                list1.append(sentence.text)

            #print(list1)
            row['sentences'] = list1
            #print(row['sentences'])
        
        logging.info(df['sentences'])

        dfcolumns = pd.DataFrame(df['sentences'].values.tolist()).add_prefix('column_')

        #print(dfcolumns)

        # Apply Version is slower:
        # expand df.sentences into its own dataframe
        # dfcolumns = df['sentences'].apply(pd.Series)
        # rename each variable
        #dfcolumns = dfcolumns.rename(columns = lambda x : 'columnname_' + str(x))


        # join the column dataframe back to the original dataframe
        dfconcat = pd.concat([df[:], dfcolumns[:]], axis=1)

        logging.info(dfconcat)

        return dfconcat