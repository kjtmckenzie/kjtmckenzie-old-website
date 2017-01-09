#!/usr/bin/env python

def loadList(file_name):
    """Loads text files as lists of lines. Used in evaluation."""
    with open(file_name) as f:
        l = [line.strip() for line in f]
    return l
    
def get_params(param_list):
    album_title = "default title"
    location = "default location"
    for str in param_list:
        val = str.split(": ")
        if (val[0] == "Album Title"):
            album_title = val[1]
        if (val[0] == "Location"):
            location = val[1]
            
    return album_title, location

def main():
    """Tests the model on the command line. This won't be called in
        scoring, so if you change anything here it should only be code 
        that you use in testing the behavior of the model."""

    template_file = "../index_template.html"
    parameters_file = "parameters.txt"

    param_list = loadList(parameters_file)
    album_title, location = get_params(param_list)
    
    # copy file
    # find and replace
    

if __name__ == '__main__':
    main()
