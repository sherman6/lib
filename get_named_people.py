# coding: utf-8

# Function to put words together in natural language.

def concatenate_names_naturally(list_of_names):
    
    """This function joins names from a list together in a natural language string."""
    
    listlength = len(list_of_names)
  
    if listlength ==0:
        output = "This list contains no names."

    elif listlength ==1:
        output = "This list contains 1 name: "+list_of_names[0]+"."

    elif listlength ==2: 
        output = "This list contains "+list_of_names[0]+" & "+list_of_names[1]+"."
        
    elif listlength > 2:
        output = "This list contains "
        names_except_last = list_of_names[0:-1]
        output = output + ", ".join(names_except_last)
        final_name = ", & "+ list_of_names[-1]+"."
        output = output + final_name
            
    return output

# This function joins words together in the way that sounds like an English-speaking person 
# is actually saying it.  If there are more than two names, separates each name by commas, 
# and adds an 'and' prior to the final name in the list. This language is very natural. 



# Function to extract named entities from text.

import nltk as nltk

def get_named_people(text="Simon and Nick are going to The Winchester Pub."):
    """Extract named entities which are people, using NLTK. Creates global variables."""
    
    global entities_w_labels_unique
    global named_people
    
    print("Warning: Creates global variables, 'entities_w_labels_unique', 'named_people'; Rewrites if already exist.")
    
    entities = []
    labels = []

    for sentence in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary = False):
            if hasattr(chunk, 'label'):
                entities.append(' '.join(c[0] for c in chunk)) #Add space as between multi-token entities
                labels.append(chunk.label()) 

    entities_w_labels = list(zip(entities, labels)) #match entities with their type label
    entities_w_labels_unique = list(set(zip(entities, labels))) #keep only unique (non-duplicate) entities

    named_people=[] 
    for i in range(len(entities_w_labels_unique)):
              if entities_w_labels_unique[i][1] in ['PERSON']:
                named_people.append(entities_w_labels_unique[i][0]) #Give only entities which are persons

    return named_people

# This extracts a list of unique people, named in a passage of text, using the NLTK package.  



# Putting it altogether:
concatenate_names_naturally(get_named_people(text))