from pathlib import Path
import pandas as pd

import logging
logging.basicConfig(level=logging.DEBUG)

from nlp_helper import *


def main() -> None:
    config_dict = read_configfile('config.json')
    df = import_json_data(filepath=config_dict['DATA_INPUT_FILEPATH_JSON'])

    nlp_models = load_spacy(language_models=[config_dict['LANGUAGE_MODELS']])

    df_text_into_columns = split_text_into_columns(nlp_models=nlp_models, df=df)
    export_csv(input_df=df_text_into_columns, target_filepath=config_dict['DATA_OUTPUT_FILEPATH_CSV'])
    export_json(input_df=df_text_into_columns, target_filepath=config_dict['DATA_OUTPUT_FILEPATH_JSON'])

if __name__ == "__main__":
    main()