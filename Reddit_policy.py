from general import *
from text_Processing import *
from section_object import *

Reddit_POLICY = read_file('reddit_privacy_policy.txt')
Reddit_POLICY_SECTIONS = divide_to_section(Reddit_POLICY, '!')
Reddit_Section_Object_set = set()


def create_object_Reddit():
    for sect in Reddit_POLICY_SECTIONS:
        Reddit_Section_Object_set.add(WebSiteObject(sect))
