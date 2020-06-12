import logging
logging.basicConfig(level=logging.DEBUG)

def load_spacy(language_models) -> None:
    """
    This loads spacy and language models 

    Returns:
        Spacy language models: [description]
    """
    import spacy
    import importlib

    nlp_models = []
    nlp_models.clear()

    for language_model_name in language_models:
        language_model = importlib.import_module(language_model_name)

        # Only import the elements you need to speed up
        nlp_model = language_model.load(disable=['ner', 'tagger'])
        logging.info(nlp_model)
        logging.info(nlp_model.pipe_names)

        nlp_models.append(nlp_model)

    logging.info(nlp_models)
    return nlp_models