sentence=input()

# clean snd normalize the sentence
cleaned=sentence.strip()
normalized=cleaned.lower()
new_norm=normalized.replace(".","")

# split the sentence and create the slug
words=new_norm.split()
joins="-".join(words)

# Produce the uppercase form and search result
uppercase=new_norm.upper()
position=new_norm.find("python")

# Display all processed values
print("Cleaned:",cleaned)
print("Normalized:",new_norm)
print("Word:",words)
print("Slug:",joins)
print("Uppercase:",uppercase)
print("Python Position:",position)