from pathlib import Path

def load_spacy() -> None:
    """
    This loads spacy and language models 

    Returns:
        Spacy language models: [description]
    """
    import spacy
    import de_core_news_sm

    nlp_model_de = de_core_news_sm.load()

    print(nlp_model_de.pipe_names)

    return nlp_model_de


def split_text_into_columns(nlp_model_de, df) -> None:
    """
    Takes Text Content of one DataFrame Cell and splits into multiple Columns

    Args:
        nlp_model_de (spacy model): [description]
        df (Pandas DataFrame): [description]

    Returns:
        Pandas Dataframe: concatenated Dataframe
    """
    import pandas as pd

    nlp_model_de = nlp_model_de

    df['sentences'] = 'default value'

    for nlp_model in [nlp_model_de]:
        

        for index, row in df.iterrows():

            list1 = []
            list1.clear()

            for sentence in nlp_model(row['content']).sents:
                #print(sentence)

                list1.append(sentence.text)

            #print(list1)
            row['sentences'] = list1
            print(row['sentences'])
        
        print('____')
        print(df['sentences'])

        dfcolumns = pd.DataFrame(df['sentences'].values.tolist()).add_prefix('column_')

        print(dfcolumns)

        # Apply Version is slower:
        # expand df.sentences into its own dataframe
        # dfcolumns = df['sentences'].apply(pd.Series)
        # rename each variable
        #dfcolumns = dfcolumns.rename(columns = lambda x : 'columnname_' + str(x))


        # join the column dataframe back to the original dataframe
        dfconcat = pd.concat([df[:], dfcolumns[:]], axis=1)

        print(dfconcat)
        print(dfconcat.info())

        return dfconcat

def import_data(filepath: Path) -> None:
    """
    Reads a CSV File and converts it into a Pandas DF

    Args:
        filepath (filepath): relative Path of Input File
    Returns:
        Pandas DataFrame: parsed Dataframe
    """
    import json
    import pandas as pd

    with open(filepath) as json_file:
        data = json.load(json_file)
        #print(data['user'])
        df = pd.DataFrame.from_dict(data['user'], orient='columns')

        #print(df)
        return df


def main() -> None:
    df = import_data(filepath='data/data.json')
    nlp_model_de = load_spacy()

    split_text_into_columns(nlp_model_de=nlp_model_de, df=df)

    return None

if __name__ == "__main__":
    main()

