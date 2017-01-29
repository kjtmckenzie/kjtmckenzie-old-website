#!/usr/bin/env python

import os

image_row = \
'''
        <div class="row">
            <div class="col-md-12">
                <a href="#FILENAME#">
                    <img class="img-responsive" src="#FILENAME#" alt="">
                </a>
            </div>
        </div>
        <!-- /.row -->
        <hr>
'''

def loadList(file_name):
    """Loads text files as lists of lines. Used in evaluation."""
    with open(file_name) as f:
        l = [line.strip() for line in f]
    return l


def main():
    """Tests the model on the command line. This won't be called in
        scoring, so if you change anything here it should only be code 
        that you use in testing the behavior of the model."""

    template_file = "../index_template.html"

    album_title = raw_input("Album title: ")
    location = raw_input("Location: ")
    
    path="images/"
    filenames = next(os.walk(path))[2]
    images_html = ""
    
    for file in filenames:
        images_html += image_row.replace("#FILENAME#", path + file)
    
    with open(template_file) as rf:
        with open("index.html", "w") as wf:
            for line in rf:
                line = line.replace("#TITLE#", album_title)
                line = line.replace("#LOCATION#", location)
                line = line.replace("#IMAGES#", images_html)
                wf.write(line)
                #print line
                
    
    # copy file
    # find and replace
    

if __name__ == '__main__':
    main()
