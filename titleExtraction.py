def isNotGarbageString(str):
    # A string with no alphabets is considered as a garbage string in our implementation
    for c in str:
        if(c.isalpha()):
            return True
    return False


def maxHeightOfWords(dict):
    maxHeight = 0
    for i in range(len(dict['level'])):
        # Height is checked for non-empty and non-garbage strings
        if(dict['text'][i].strip() != '' and isNotGarbageString(dict['text'][i])):
            maxHeight = max(maxHeight, dict['height'][i])
    return maxHeight


def getTitleUsingMaxHeight(dict, maxHeight):
    result = []
    for i in range(len(dict['level'])):
        # Height is checked for non-empty and non-garbage strings
        if(dict['text'][i].strip() != '' and isNotGarbageString(dict['text'][i])):
            # Tolerance for lower bound = maxHeight - 10
            if(dict['height'][i] >= maxHeight - 10):
                result.append(dict['text'][i])
    return " ".join(result)


def extractTitle(imgDict):
    '''Extracts  title from the OCR output.
    Uses the heuristic of finding text with maximum height in the OCR output'''
    maxHeight = maxHeightOfWords(imgDict)
    return getTitleUsingMaxHeight(imgDict, maxHeight)
