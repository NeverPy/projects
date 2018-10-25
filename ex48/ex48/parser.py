class ParserError(Exception):
    pass

class Sentence:
    
    def __init__(self,subject,verb,obj):
            self.subject = subject[1]
            self.verb = verb[1]
            self.object = obj[1]
            
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list,expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list,word_type):
    while peek(word_list) == word_type:
        match(word_list,word_type)

class Parse:
    def __init__(self,word_list):
        self.word_list = word_list
        
    def parse_verb(self,word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_object(self,word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(self,word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb or a noun next .")

    def parse_sentence(self,word_list):
        subj = self.parse_subject(word_list)
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)

        return Sentence(subj, verb, obj)
    def parse_addlist(self,word_list):
        self.word_list=word_list
word_list=[]
parse=Parse(word_list)
"""
class ParserError(Exception):
    pass

class Sentence:
    
    def __init__(self,subject,verb,obj):
            self.subject = subject[1]
            self.verb = verb[1]
            self.object = obj[1]
            
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list,expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list,word_type):
    while peek(word_list) == word_type:
        match(word_list,word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb or a noun next .")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
"""
