import lexnlp.nlp.en.segments.sentences
import lexnlp.nlp.en.segments.sections
import lexnlp.nlp.en.segments.paragraphs
import lexnlp.extract.en.urls
import spacy
import lexnlp.nlp.en.transforms.tokens
import re

nlpl = spacy.load('en')
nlp = spacy.load('en_core_web_sm')


def remove_urls(text):
    urls = lexnlp.extract.en.urls.get_urls(text)
    for url in urls:
        text = text.replace(url, 'URL')
    return text


def text_to_sentences(text):
    return lexnlp.nlp.en.segments.sentences.get_sentence_list(text)


def text_to_span_list(text):
    return lexnlp.nlp.en.segments.sentences.get_sentence_span_list(text)


def pre_process_document(text):
    return lexnlp.nlp.en.segments.sentences.pre_process_document(text)


def post_process_sentence(text, span_list):
    for item in span_list:
        print(lexnlp.nlp.en.segments.sentences.post_process_sentence(text, item))


def divide_to_section(text, ch):
    text = remove_urls(text)
    sections_temp = text.split(ch)
    temp = ''
    sections = set()
    for sec in sections_temp:
        sents = text_to_sentences(sec)
        result = ''
        result += temp
        for sent in sents[:-1]:
            result += '\n' + sent
        temp = sents[len(sents)-1] + '.'
        sections.add(result)
    return sections

def divide_to_paragraph(text):
    return lexnlp.nlp.en.segments.paragraphs.get_paragraphs(text)


def clean_text(text):
    result = ""
    for word in text:
        if word.is_stop == False and word.lemma_ != "-PRON-":  #:
            result += word.lemma_.lower().strip()
            result += " "
    resultt = result.replace("datum", "data").replace(",", "")
    result = resultt.replace("-PRON-", "")
    # result = nlp(result)
    return result


def extra_clean(text):
    text = text.lower()
    text = text.replace("the data subject", "you")
    text = text.replace("the controller", "we")
    text = text.replace("right", "")
    text = text.replace("data", "")
    text = text.replace("information", "")
    text = text.replace("article", "")
    text = re.sub("\d+", "", text)
    text = text.replace(')', '').replace('(', '')
    return clean_text(nlp(text))


def extract_nouns(text):
    text = extra_clean(text)
    text = nlp(text.strip())
    matchtext = []
    for word in text.noun_chunks:
        if word.lemma_ != "-PRON-":
            matchtext.append(word.text)
    if len(matchtext) is 0:
        for word in text:
            matchtext.append(word.text)
    return matchtext


def extract_root_NC(text):
    text = extra_clean(text)
    text = nlp(text)
    for word in text:
        if word.dep_ == "ROOT":
            print(word)
