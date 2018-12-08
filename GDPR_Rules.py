from GDPR_object import *
from Reddit_policy import *
from compare import *
from facebook_policy import *
from twitter_Policy import *


text = read_directory_contents('GDPR_Articles')
GDPR_rules_objects = set()

print('Welcome!!')
print('This code will take some time so please be patient....')
print('Reading GDPR laws .....')
for Art in text:
    GDPR_rules_objects.add(GDPRobject(Art))


for art in GDPR_rules_objects:
    print(art.section_NC)


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

