import spacy


def extractAuthors(imgText):
    '''Extracts authors from the OCR output.
    Employs Named Entity Recognition using spaCy for the purpose'''

    nlp = spacy.load("en_core_web_md")
    doc = nlp(imgText)

    # Obtaining named entities with label PERSON
    authors = {ent.text for ent in doc.ents if ent.label_ == 'PERSON'}
    return authors
