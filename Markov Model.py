import random 

#1 
def create_dictionary(filename): 
    '''takes a string representing the name of a text file, 
    and that returns a dictionary of key-value pairs in which:'''
    
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    words = text.split() 
    
    d = {} 
    current_word = '$' 
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word] 
        else: 
            d[current_word] += [next_word] 
            
        if next_word[-1] not in  '?.,!': 
            current_word = next_word
        else: 
            current_word = '$'
    return d
            
#2 
def generate_text(word_dict, num_words): 
    '''The function must use word_dict to generate and 
    print num_words words, with a space after each word.'''
    
    first_word = '$' 
    count = range(num_words)
    
    for x in count: 
        next_word = random.choice(word_dict[first_word])
        if next_word[-1] not in '.!?': 
            first_word = next_word 
        else: 
            first_word = '$'
        print(next_word, end = ' ')



# Create random text from lyrics from the song Brave by Sara Bareilles

word_dict = create_dictionary('sample_text.txt')

generate_text(word_dict, 20)