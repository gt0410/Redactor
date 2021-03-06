#
#
#
import argparse
import urllib
import re
import tempfile
import nltk
from commonregex import CommonRegex
from nltk.corpus import wordnet as wn
import numpy
import sys

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

#    for name in name_list:
#        data = data.replace(name, block) #failing
    return data, name_list


def dates(data):
    parsed_text = CommonRegex(data)
    dates_list = parsed_text.dates

#    for date in dates_list:
#        data = data.replace(date, block)
    return data, dates_list

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
    
#    for add in loc_list:
#        data = data.replace(add, block)
    
    return data, loc_list

def phones(data):
    parsed_text = CommonRegex(data)
    phones_list = parsed_text.phones
#    for phone in phones_list:
#        data = data.replace(phone, block)
    return data, phones_list

def genders(data):
    genders_list=['he','she','him','her','his','hers','male','female','man','woman','men','women']
#    c1 = data.count(block)
#    for gender in genders_list:
#        raw_text = r'\b' + gender + r'\b'
#        data = re.sub(raw_text, block, data, flags = re.IGNORECASE)
#    c2 = data.count(block)
#    gender_count = c2 - c1
    return data, genders_list



def concept(data, concept):
    concept_list = []
    concept_count = 0
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
                m = len(sentence)
                bl = m * block
                data = data.replace(sentence, bl)
                concept_count += 1
    return data, concept_list, concept_count

def redact(names_list, genders_list, dates, address_list, phones_list, concept_list, data):
    total = names_list + genders_list + dates + address_list + phones_list
    for elm in total:
        m = len(elm)
        elm = r'\b' + elm + r'\b'
        bl = m * block
        data = re.sub(elm, bl, data)

    return data

def stats(names_list, dates, address_list, phones_list, gen_list, gender_count, concept_list, concept_count, stats_list, f):
    status = ''
    total = len(names_list) + len(address_list) + len(phones_list) + concept_count + len(dates) + gender_count
    st = stats_list[0]
    status += ("Status for the file {}\n".format(f))
    status += ("The following number of names are redacted from the file {} \n".format(len(names_list)))
    status += ("The following number of dates are redacted from the file {} \n".format(len(dates)))
    status += ("The following number of addresses are redacted from the file {} \n".format(len(address_list)))
    status += ("The following number of phones are redacted from the file {} \n".format(len(phones_list)))
    status += ("The following number of genders are redacted from the file {} \n".format(gender_count))
    status += ("The following number of sentences are redacted from the file {} \n".format(concept_count))
    status += ("The total number of redactions in the file are {} \n".format(total))

    if st == 'stdout':
        print(status)

    elif st == 'stderr':
        err = ''
        if len(names_list) == 0:
            err += ("There are no names in the file to be redacted\n")
        if len(dates) == 0:
            err += ("There are no dates in the file to be redacted\n")
        if len(address_list) == 0:
            err += ("There are no addresses in the file to be redacted\n")
        if len(phones_list) == 0:
            err += ("There are no phones in the file to be redacted\n")
        if gender_count == 0:
            err += ("There are no genders in the file to be redacted\n")
        if concept_count == 0:
            err += ("There are no matches for concept in the file to be redacted\n")

        sys.stderr.write(err)

    else:
#        os.system("touch {}".format("stats.txt"))
        file_path = "stats.txt"
        with open(file_path, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()

    return status
