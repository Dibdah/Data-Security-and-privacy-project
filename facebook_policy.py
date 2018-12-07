from general import *
from text_Processing import *
from section_object import *

FaceBook_POLICY = read_file('facebook_policy.txt')
FaceBook_POLICY_SECTIONS = divide_to_section(FaceBook_POLICY, '?')
FaceBook_Section_Object_set = set()


def create_object_facebook():
    for sect in FaceBook_POLICY_SECTIONS:
        FaceBook_Section_Object_set.add(WebSiteObject(sect))
