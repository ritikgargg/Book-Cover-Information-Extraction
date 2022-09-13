import re


def returnMatches(regex, text):
    regexMatches = re.findall(regex, text)
    return {match[0].strip() for match in regexMatches}


def extractISBNs(imgText):
    '''Extracts ISBN numbers from the OCR output.
    Uses regex matching(with appropriate fallback cases) for the same.'''

    primaryISBNRegex = r'((ISBN[-]?(1[03])?[ ]*(:){0,1}[ ]*)(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10}))'

    # Fallback regex when some of the numbers in the ISBN are misread as alphabets by the OCR library.
    fallbackRegex = r'((ISBN[-]?(1[03])?[ ]*(:){0,1}[ ]*)(([0-9Xxa-zA-Z][- ]*){13}|([0-9Xxa-zA-Z][- ]*){10}))'

    isbns = returnMatches(primaryISBNRegex, imgText)

    if(len(isbns) == 0):
        isbns = returnMatches(fallbackRegex, imgText)

    return isbns
