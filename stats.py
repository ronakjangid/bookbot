def num_of_words(book_text):
    length_words = book_text.split()
    return len(length_words)


def count_characters(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts


def sort_on(items):
    return items['num']

def get_report(dictionary):
    temp_list = []
    for k, v in dictionary.items():
        temp_dic = {'char': k, 'num': v}
        temp_list.append(temp_dic)
    temp_list.sort(key=sort_on, reverse=True)
    return temp_list



