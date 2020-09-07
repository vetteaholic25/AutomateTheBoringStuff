import re
#Regular expression designed to show if a date is in correct format


#Regex that recognizes DD/MM/YYYY
dateFormatRegex=re.compile(r"\d{2}/\d{2}/\d{4}")
print(dateFormatRegex.findall(r"My birthday is 03/25/1991. Ginny's birthday is 06/10/1995."))
