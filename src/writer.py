"""
module for writing the clipping into their files
"""

import os

class Writer:
    """ the class for the writing functionality """

    def __init__(self, tags, data_folder, tagged):
        self.data_folder = data_folder
        self.tags = tags.split(',')
        self.tagged = tagged


    def manual(self, clippings):
        """ function to manually import clippings """

        d = {clipping:"x" for clipping in clippings}

        d_keys = list(d.keys())

        i = 0
        while i < len(d_keys):
            title = d_keys[i][0]
            metadata = d_keys[i][1].split("|")
            page = d_keys[i][0]
            date = d_keys[i][1]
            text = d_keys[i][3]
            print("Title: " + title)
            print("Page Number: " + page)
            print("Date: " + date)
            print("Text: " + text)

            print("Tags: ", end="")
            for tag in self.tags:
                print(tag + ", ", end="")
            print("\n")

            d_tag = input("Enter tag: ")

            if d_tag == "n":
                i += 1

            elif d_tag == "p":
                i -= 1

            else:
                d[d_keys[i]] = d_tag
                i += 1

        for clipping, d_tag in d.items():
            if d_tag != "x":

                if not os.path.exists(self.tagged + d_tag):
                    os.makedirs(self.tagged + d_tag)

                with open(self.tagged + '/' + d_tag + '/' + clipping[0], "a") as file:
                    file.write(clipping[3] + "\n")
                file.close()

    def auto(self, clippings):
        """ funtion for automatically writing out clippings """
        for clipping in clippings:
            title = clipping[0]
            text = clipping[3]

            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)

            with open(self.data_folder + '/' + str(title).rstrip() + '.md', "a") as file:
                file.write(text + "\n")
            file.close()
