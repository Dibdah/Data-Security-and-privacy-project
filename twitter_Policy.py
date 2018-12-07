from general import *
from text_Processing import *
from section_object import *

TWITTER_POLICY = read_file('twitter_policy_text.txt')
TWITTER_POLICY_SECTIONS = divide_to_section(TWITTER_POLICY, ':')
Twitter_Section_Object_set = set()


def create_object_twitter():
    for sect in TWITTER_POLICY_SECTIONS:
        Twitter_Section_Object_set.add(WebSiteObject(sect))




# TWITTER_POLICY_PARA = divide_to_paragraph(TWITTER_POLICY)


# def twitter_vs_write_of_access():
