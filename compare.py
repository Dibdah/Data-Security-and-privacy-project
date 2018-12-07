from difflib import *
from spacy.matcher import Matcher, PhraseMatcher
from text_Processing import *
from general import *

nlp = spacy.load('en_core_web_sm')
nlpv = spacy.load('en_vectors_web_lg')
matcher = PhraseMatcher(nlp.vocab)


def find_key_word(policy_set, gdpr_NC):
    match_sections = set()
    patterns = [nlp(text) for text in gdpr_NC]
    for pattern in patterns:
        matcher.add('pattern', None, *patterns)
    for policy in policy_set:
        matches = matcher(policy.section)
        for match_id, start, end in matches:
            match_sections.add(policy)
    return match_sections


def compare_NC(policy_set, gdpr_NC):
    same_topic = set()
    for policy in policy_set:
        for nc_gdpr in gdpr_NC:
            nc_gdpr = nlpv(nc_gdpr)
            for nc in policy.section_NC:
                nc = nlpv(nc)
                sim1 = nc.similarity(nc_gdpr)
                if sim1 >= 0.8:
                    same_topic.add(policy)
                    continue
    if len(same_topic) is 0:
        same_topic = look_further(policy_set, gdpr_NC)
    return same_topic


def compare_NC_to_section(policy_set, art_NC):
    same_topic = set()
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(title_nc) for title_nc in art_NC]
    for pattern in patterns:
        matcher.add('titlepattern', None, *patterns)
    for policy in policy_set:
        matches = matcher(nlp(policy.section))
        if len(matches) is not 0:
            same_topic.add(policy)
    return same_topic


def look_further(policy_set, gdpr_NC):
    same_topic = set()
    for policy in policy_set:
        for nc_gdpr in gdpr_NC:
            word_list = str(nc_gdpr).split(' ')
            if len(word_list) is not 1:
                for word in word_list:
                    # for word in nc_gdpr:
                    sim_list = get_close_matches(word, policy.section.split(), cutoff=0.8)
                    if len(sim_list) is not 0:
                        same_topic.add(policy)
            else:
                # for word in nc_gdpr:
                sim_list = get_close_matches(nc_gdpr, policy.section.split(), cutoff=0.8)
                if len(sim_list) is not 0:
                    same_topic.add(policy)
    # print(same_topic)
    return same_topic


def get_similarity(policy_sents, gdpr_article, website):
    #gdpr_sent = set()
    #policy_sents = set()
    avg1, avg2 = find_NC_sentence_(policy_sents, gdpr_article)
    print('Values captured: ')
    print(gdpr_article.title, website, avg1, avg2)
    write_to_file(gdpr_article.title, website, avg1, avg2)


def compare_sentence_NC(policy_sents, gdpr_article):
    similar_sent = set()
    for policy in policy_sents:
        for (key, value) in gdpr_article.NC_to_sentence.items():
            print('---------------------')
            for (k, v) in policy.NC_to_sentence.items():
                key = nlpv(str(key))
                k = nlpv(str(k))
                sim = key.similarity(k)
                if sim > 0.8:
                    print('Value:', value, '\n')
                    print('policy value: ', v)
                    similar_sent.add(v)
            print('\n')


def find_NC_sentence_(policy_sents, gdpr_article):
    count = 0
    avg1 = 0
    avg2 = 0
    for policy in policy_sents:
        for (key, value) in gdpr_article.NC_to_sentence.items():
            for sent in policy.sentences:
                if contains_chunk(sent, key) is True:
                    value1 = extra_clean(value)
                    value1 = nlpv(str(value1))
                    sent1 = extra_clean(sent)
                    sent1 = nlpv(str(sent1))
                    sim1 = value1.similarity(sent1)
                    article = extra_clean(gdpr_article.section)
                    article = nlpv(str(article))
                    sim2 = article.similarity(sent1)
                    if sim1 > 0.75 and sim2 > 0.77:
                        avg1 += sim1
                        avg2 += sim2
                        count += 1
    if count is not 0:
        avg1 = avg1/count
        avg2 = avg2/count
    return avg1, avg2


def get_gdpr_sentence(gdpr_article, chunk):
    sents = get_sent(gdpr_article.sentences, chunk)
    return sents


def get_policy_sent(policy_set, chunk):
    sent = set()
    for policy in policy_set:
        sent.update(get_sent(policy.sentences, chunk))
    return sent


def get_sent(sent_set, chunk):
    match_sent = set()
    for sent in sent_set:
        if contains_chunk(sent, chunk) is not 0:
            match_sent.add(sent)
    return match_sent


def contains_chunk(sent, chunk):
    flag = False
    word_list = str(chunk).split(' ')
    for word in word_list:
        # for word in nc_gdpr:
        sim_list = get_close_matches(word, sent.split(), cutoff=0.8)
        if len(sim_list) is not 0:
            flag = True
    return flag
