import os
from exam import most_common_frequent_word, get_links
filenames = os.listdir("diseases") # Obtain a list of the files in the folder
                                   # diseases
f = open("diseases/" + filenames[0]) # Open the first file in the folder diseases
text0 = f.read()
f.close()
# print(text0[:2000])  # Output the first 2000 characters in the file we opened
print(most_common_frequent_word(["diseases/" + filenames[i] for i in range(100)]))
print(get_links(text0))
