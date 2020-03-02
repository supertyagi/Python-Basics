import re
import string
frequency={}
document_text=input("enter the string:")
text_string=document_text.read().lower()
match_pattern=input("enter the word or letter to be searched:")
for word in match_pattern:
 count=frequency.get(word,0)
 frequency[word]=count+1
frequency_list=frequency.keys()
for words in frequency_list:
 print words,frequency[words]