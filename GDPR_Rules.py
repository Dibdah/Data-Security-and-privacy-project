from GDPR_object import *
from Reddit_policy import *


text = read_directory_contents('GDPR_Articles')
GDPR_rules_objects = set()

print('Welcome!!')
print('This code will take some time so please be patient....')
print('Reading GDPR laws .....')
for Art in text:
    GDPR_rules_objects.add(GDPRobject(Art))

'''
for art in GDPR_rules_objects:
    print(art.section_NC)

'''
'''
print('Reading Twitter policy ....')
create_object_twitter()

print('Reading Facebook Policy ...')
create_object_facebook()
print('Reading Reddit policy .....')
create_object_Reddit()

same_topic = set()

print('Evaluation will start now:')
for Art in GDPR_rules_objects:
    print('Article title: ', Art.title, ' with Twitter')
    same_topic = compare_NC(Twitter_Section_Object_set, Art.title_NC)
    if len(same_topic) is 0:
        Art.check_article('Twitter', False)
        print('False')
    else:
        Art.check_article('Twitter', True)
        print('True')
        get_similarity(same_topic, Art, 'Twitter')
    print('Article title: ', Art.title, ' with Facebook')
    same_topic = compare_NC(FaceBook_Section_Object_set, Art.title_NC)
    if len(same_topic) is 0:
        Art.check_article('Facebook', False)
        print('False')
    else:
        Art.check_article('Facebook', True)
        print('True')
        get_similarity(same_topic, Art, 'Facebook')
    print('Article title: ', Art.title, ' with Reddit')
    same_topic = compare_NC(Reddit_Section_Object_set, Art.title_NC)
    if len(same_topic) is 0:
        Art.check_article('Reddit', False)
        print('False')
    else:
        Art.check_article('Reddit', True)
        print('True')
        get_similarity(same_topic, Art, 'Reddit')
'''
'''
for Art in GDPR_rules_objects:
    print(Art.title)
    same_topic = compare_NC(Twitter_Section_Object_set, Art.title_NC)
    Art.Article_Exists = {}
    if len(same_topic) is 0:
        Art.check_article('Twitter', False)
    else:
        Art.check_article('Twitter', True)
    same_topic = set()
    same_topic = compare_NC(FaceBook_Section_Object_set, Art.title_NC)
    if len(same_topic) is 0:
        Art.check_article('FaceBook', False)
    else:
        Art.check_article('FaceBook', True)

    same_topic = set()
    same_topic = compare_NC(Reddit_Section_Object_set, Art.title_NC)
    if len(same_topic) is 0:
        Art.check_article('Reddit', False)
    else:
        Art.check_article('Reddit', True)
    print(Art.Article_Exists)
    same_topic = set()
'''
'''
for Art in GDPR_rules_objects:
    print(Art.title)
    print(Art.Article_Exists)
    print('---------------------------')
'''

'''
'''
# for obj in GDPR_rules_objects:
#    print(obj.title)




#for reddit in FaceBook_Section_Object_set:
#    print(reddit.title)
# Right_of_Access = read_file('Data_Regulation.txt')
# Right_to_Object = read_file('Right_to_Object.txt')
# Right_of_Access_object = GDPRobject(Right_of_Access)
# Right_to_Object_object = GDPRobject(Right_to_Object)

# lexnlp_processing(Right_to_Object_object.section)
# print('***********************************')
# lexnlp_processing(Right_of_Access_object.clean_section)

'''
create_object_twitter()
create_object_facebook()
same_topic = compare_NC(Twitter_Section_Object_set, Right_of_Access_object.title_NC)
for policy in same_topic:
    print(policy.title)
print('111111111111')
same_topic = compare_NC(FaceBook_Section_Object_set, Right_of_Access_object.title_NC)
for policy in same_topic:
    print(policy.title)
print('2222222222222')
same_topic = compare_NC(Twitter_Section_Object_set, Right_to_Object_object.title_NC)
print(Right_to_Object_object.title_NC)
for policy in same_topic:
    print(policy.title)
print('3333333333333333')
same_topic = compare_NC(FaceBook_Section_Object_set, Right_to_Object_object.title_NC)
for policy in same_topic:
    print(policy.title)
'''
# policy_match = find_key_word(Section_Object_set, Right_of_Access_object)


#print(Right_of_Access_object.main_topic)

# print(Right_of_Access)

# pre_processed_text = pre_process_document(Right_of_Access)
# sentence_list = text_to_sentences(Right_of_Access)
# print(pre_process_document(Right_of_Access))
# post_process_sentence(Right_of_Access, text_to_span_list(Right_of_Access))
# print(toknize_text(Right_of_Access))
# chunck_patterns(Right_of_Access)

