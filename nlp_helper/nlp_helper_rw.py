from pathlib import Path
import pandas as pd

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


def import_json_data(filepath: Path) -> None:
    """
    Reads a JSON File and converts it into a Pandas DF

    Args:
        filepath (filepath): relative Path of Input File
    Returns:
        Pandas DataFrame: parsed Dataframe
    """
    import json
    

    with open(filepath) as json_file:
        data = json.load(json_file)

        df = pd.DataFrame.from_dict(data['user'], orient='columns')

        return df

def export_csv(input_df: pd.DataFrame, target_filepath: Path) -> None:
    input_df.to_csv(target_filepath, index=False)

    return None

def export_json(input_df: pd.DataFrame, target_filepath: Path) -> None:
    input_df.to_json(target_filepath, orient='records', lines=True)

    return None