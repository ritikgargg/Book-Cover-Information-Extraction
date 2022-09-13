def inputFileValidator(path):
    '''Validates the input against the allowed file formats'''

    # This function has the ability to extend/remove the validation support for input file formats.
    if(path.endswith(('.png', '.jpeg'))):
        return True
    return False
