#!/usr/bin/env python3

######################################################################
#
# This application will use the books of the Bible stored in separate
# files in the 'Books' directory to list each verse on separate
# lines.
#
# Author: Trevor Riddle
# Creation Date: June 21, 2017
# Update: -
#
######################################################################

import os, sys, re, subprocess

##
# An array storing the books of the Bible.
##
process = subprocess.Popen('ls Books', shell=True, stdout=subprocess.PIPE)
booksString = process.stdout.read()
booksBytes = re.findall(b'.*\.txt\n', booksString)

##
# Convert booksBytes byte array into a Python string and append to the 
# bible list. The bible list will contain a list of all the files
# containing the books of the bible found in the 'Books' directory.
##
bible = []
for book in booksBytes:
    bible.append(book.decode("utf-8"))

##
# A function that returns the bible list
##
def booksList():
    return bible

##
# Stores a book of the bible into the text variable.
##
text = ""
def getBook(book):
    file = open(book, 'r')
    global text
    text = file.read()
    file.close()


##
# I NOW HAVE THE ORGANIZED BIBLE FILES. THIS CODE IS NO LONGER NEEDED. 
#
# A loop to iterate through each book of the Bible to manipulate
# using regular expressions. The primary goal is to create new files
# for the books of the bible where each book has this particular
# organization:
#     * Each verse is on a single line.
#     * Each chapter:verse pair will have the book at the front as
#       well. For example: Genesis 1:1. 
##
#for book in bible:
    # Variables
    


    # Store the book in the global text variable.
#    getBook("Books/" + book[:-1])

    # Put each verse on a separate line and store in update.
#    update = re.sub(r'\s(\d{1,3}:\d{1,3})\s', r'\n\1 ', text) 
#    update1 = re.sub(r'\n([^0-9].*)', r'\1 ', update)
#    update2 = re.sub(r'(\d{1,3}:\d{1,3})', book[:-5] + r' \1', update1)
    
#    file = open("BibleOrg/" + book[:-5], "a+")
#    file.write(update2)
