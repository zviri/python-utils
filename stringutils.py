import unicodedata
import re

def remove_accents(s):
    nkfd_form = unicodedata.normalize('NFKD', s)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii

def normalize_whitespace(s):
    return re.sub(r'\s+', ' ', s.strip())

def string_id(s):
    return re.sub('[\pL\pN]+', '', s).lower()
