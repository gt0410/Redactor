import argparse
import urllib
import re
import tempfile
import nltk
from commonregex import CommonRegex
from nltk.corpus import wordnet as wn
import numpy

block = '\u2588'

def names(data):
    name = ""
    name_list = []
    words = nltk.word_tokenize(data)
    taggsets = nltk.pos_tag(words)
    namedEnt = nltk.ne_chunk(taggsets, binary = False)
    
    for subtree in namedEnt.subtrees():
        if subtree.label() == 'PERSON':
            l = []
            #print((subtree.leaves()))
            for leaf in subtree.leaves():
                l.append(leaf[0])
            name = ' '.join(l)
            if name not in name_list:
                name_list.append(name)

    for name in name_list:
        data = data.replace(name, block) #failing
    return(data, name_list)


def dates(data):
    parsed_text = CommonRegex(data)
    dates_list = parsed_text.dates

    for date in dates_list:
        data = data.replace(date, block)
    return(data, dates_list)

def addresses(data):
    st_address = []
    loc = ''
    loc_list = []
    parsed_text = CommonRegex(data)
    st_address = parsed_text.street_addresses
    words = nltk.word_tokenize(data)
    taggsets = nltk.pos_tag(words)
    namedEnt = nltk.ne_chunk(taggsets, binary = False)
    
    for subtree in namedEnt.subtrees():
        if subtree.label() == 'GPE':
            l = []
            # print((subtree.leaves()))
            for leaf in subtree.leaves():
                l.append(leaf[0])
            loc = ' '.join(l)
            if loc not in loc_list:
                loc_list.append(loc)
        
    loc_list.extend(st_address)
    
    for add in loc_list:
        data = data.replace(add, block)
    
    return(data, loc_list)

def phones(data):
    parsed_text = CommonRegex(data)
    phones_list = parsed_text.phones
    for phone in phones_list:
        data = data.replace(phone, block)
    return(data, phones_list)

def genders(data):
    genders_list=['he','she','him','her','his','hers','male','female','man','woman','men','women']

    for gender in genders_list:
        raw_text = r'\b' + gender + r'\b'
        data = re.sub(raw_text, block, data, flags = re.IGNORECASE)

    return(data)



def concept(data, concept):
    concept_list = []
    syns = wn.synsets(concept)
    for syn in syns:
        temp = syn.lemma_names()
        for elm in temp:
            if elm not in concept_list:
                concept_list.append(elm)

    sentences = nltk.sent_tokenize(data)
    for sentence in sentences:
        for c in concept_list:
            if c.lower() in sentence.lower():
                data = data.replace(sentence, block)

    return(data, concept_list)
