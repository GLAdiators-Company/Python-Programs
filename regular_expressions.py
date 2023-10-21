import re

pattern = r"(?!h)[a-z]ello"

text = '''RegExr was created by gskinner.com.hel
Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.comfgello
tello gello 
The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community relloand telloview patterns you create or favorite in My Patterns.

Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.

'''

# match = re.search(pattern,text) #It will return None if the pattern does not find in the text 
# print(match)

matches = re.finditer(pattern,text)

for match in matches:
    print(text[match.span()[0]:match.span()[1]],match.span(),sep=' -> ')