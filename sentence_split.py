from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)

def read_configfile(filepath: Path) -> dict:
    """
    Reads in the config file from root directory
    Returns:
        returns the json file storing configuration
    """
    import json
    CONFIG_FILEPATH = Path(filepath)

    with open(CONFIG_FILEPATH, 'r', encoding='utf-8') as fp:
        config_dict = json.load(fp)

    return config_dict

def load_spacy() -> None:
    """
    This loads spacy and language models 

    Returns:
        Spacy language models: [description]
    """
    import spacy
    import de_core_news_sm

    # Only import the elements you need to speed up
    nlp_model_de = de_core_news_sm.load(disable=['ner', 'tagger'])

    logging.info(nlp_model_de.pipe_names)

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
    configdict = read_configfile('config.json')
    df = import_data(filepath=configdict['DATA_INPUT_FILEPATH'])
    nlp_model_de = load_spacy()

    split_text_into_columns(nlp_model_de=nlp_model_de, df=df)

    return None

if __name__ == "__main__":
    main()

