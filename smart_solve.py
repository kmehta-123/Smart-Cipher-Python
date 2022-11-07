import webster_api
import cipher

def smart_solve(text):

    pm = _probability_map(text)

    max_proportion = 0.0
    closest_match = ''
    for key in pm:
        if pm[key] > max_proportion:
            max_proportion = pm[key]
            closest_match = key
    
    return closest_match

def _probability_map(text):

    to_return = dict()

    for i in range(len(cipher.alpha)):
        real_words = []
        words = cipher.decode(text, i).split()

        for word in words:

            # print(word)

            if webster_api.is_word(word):
                real_words.append(word)
        
        words_str = ' '.join(words).lower()

        to_return[words_str] = len(real_words) / len(words)
    
    return to_return