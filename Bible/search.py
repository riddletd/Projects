#!/usr/bin/python

import os, sys, re, organize, textwrap

bible = organize.booksList()
count = 0
bookCount = 0
prevBookCount = 0
bookReference = ""



##
# Prints out the number of verses containing the search word(s).
# Currently NOT being used.
##
def verseNum():    
    if bookCount > 0:
        if " " not in search:
            print("\tThe word \"" 
                  + search 
                  + "\" is mentioned " 
                  + str(bookCount) 
                  + " times in the book of " + bookName + ".\n\n")
        else:
            print("\tThe expression \"" 
                  + search 
                  + "\" is mentioned " 
                  + str(bookCount) 
                  + " times in the book of " + bookName + ".\n\n")

### MAIN ###
#
# Takes the user input and iterates through the books of the bible
# in the BibleOrg directory and matches the verses containing the
# input.
#
##

search = raw_input("Search: ")

for book in bible:

    # Store the name of the book of the bible.
    
    bookName = book[:-5]

    # Open the file in the BibleOrg diretory using the names of the
    # bible found in the Books directory.
    
    file = open("BibleOrg/" + bookName)
    text = file.read()
    
    # Store the verses containing the input in a list.
    
    verse = re.findall(r'.*' + search + r'.*', text, re.I)
    
    # Pretty-print the verse to stdout and keep a count of both:
    #    * the number of verses that match the input 
    #    * and a count of the verses matching the input in a single
    #      book.

    for found in verse:
        dedented_text = textwrap.dedent(found).strip()
        print(textwrap.fill(dedented_text, width=80) + "\n\n")
        count += 1
        bookCount += 1

    # Store the reference of the book with the largest verse count.
    
    if bookCount > prevBookCount:
        bookReference = bookName
        prevBookCount = bookCount
    
    # Erase verse count for the next book.
        
    bookCount = 0

##
# Pretty-prints the stats for the search word(s) the user provides.
##

print("\n**************************************NOTE**************************************\n*")

if count != 0:
    if " " not in search:
        print("* The word \"" 
              + search 
              + "\" is mentioned " 
              + str(count) 
              + " times in the Bible.")
    else:
        print("* The expression \"" 
              + search 
              + "\" is mentioned " 
              + str(count) 
              + " times in the Bible.")
else:
    if " " not in search:    
        print("* The word \"" + search + "\" is not mentioned.")
    else:
        print("* The expression \"" + search + "\" is not mentioned.")

if prevBookCount != 0:
    print("* "
          + bookReference 
          + " has the most references to \"" 
          + search 
          + "\" with " 
          + str(prevBookCount) 
          + " references."
          
          + "\n* It would be wise to study " 
          + bookReference
          + " for more information about \""
          + search
          + "\".")

print("*\n********************************************************************************\n")
