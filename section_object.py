from text_Processing import *
import spacy

nlpl = spacy.load('en')
nlp = spacy.load('en_core_web_lg')


class WebSiteObject:
    section = ''
    title = ''
    sentences = set()
    clean_section = ''
    clean_title = ''
    sentences_clean = set()
    title_NC = []
    section_NC = []
    NC_to_sentence = {}

    def __init__(self, section):
        self.section = section
        self.sentences = self.get_sentences()
        self.title = next(iter(self.sentences))
        # self.clean_title = self.clean_text(nlpl(self.title))
        # self.title_NC = self.get_NC(self.title)
        self.section_NC = self.get_NC(self.section)
        self.get_NC_per_sentence()

    def get_sentences(self):
        return text_to_sentences(self.section)

    def clean_text(self, text):
        return clean_text(text)

    def get_NC(self, text):
        return extract_nouns(text)

    def get_NC_per_sentence(self):
        for sent in self.sentences:
            NC_set = set()
            NC_set.update(self.get_NC(sent))
            for nc in NC_set:
                self.NC_to_sentence.update({nc: sent})
