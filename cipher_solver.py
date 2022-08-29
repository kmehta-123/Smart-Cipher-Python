import webster_api
import cipher

def likelihood_dict(text):

    to_return = dict()

    for i in range(len(cipher.alpha)):
        real_words = []
        words = cipher.decode(text, i).split()

        for word in words:
            if webster_api.is_word(word):
                real_words.append(word)
        
        words_str = ' '.join(words).lower()

        to_return[words_str] = len(real_words) / len(words)
    
    return to_return

def best_match(text):

    ld = likelihood_dict(text)

    max_proportion = 0.0
    closest_match = ''
    for key in ld:
        if ld[key] > max_proportion:
            max_proportion = ld[key]
            closest_match = key
    
    return closest_match