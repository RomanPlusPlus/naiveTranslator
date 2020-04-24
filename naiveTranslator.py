"""
Translates text from Russian to English, and the other way around. Also detects the input language.

The translation is done word-by-word, using a very limited dictionary of 12 tsd entries.
The dictionary was build by google-translating the 12 000 most common words of the spoken Russian.
The list of common words was obtained from wiktionary.org:
https://ru.wiktionary.org/wiki/Приложение:Список_частотности_по_НКРЯ:_Устная_речь_1—1000
The list is authored by Sobloku, Exuwon, Alone Coder, Vesailok, Al Silonov, and is available under the Creative
Commons Attribution-ShareAlike 3.0. license.
"""


def file_read_and_cleanup(filename):
    """Reads the file and returns a list of lines, stripped and converted into the lower case.

    Args:
        filename (str): e.g. "en_ru_dic/en.txt"
    """
    with open(filename) as f:
        lines = f.readlines()
    clean_lines = []
    for rc in range(len(lines)):
        clean_lines.append(lines[rc].strip().lower())
    return clean_lines


def build_dictionaries(english_lines, russian_lines):
    """Returns 2 bilingual dictionaries that look like this: {en_word: ru_word, ...} and  {ru_word: en_word, ...}

    Args:
        english_lines (list of strings): a list of English words, each being a translation a word from russian_lines
        russian_lines (list of strings): a list of Russian words.
    """
    en_as_input_dic = dict()
    ru_as_input_dic = dict()
    if len(english_lines) == len(russian_lines):

        for bd in range(len(english_lines)):
            en_as_input_dic[english_lines[bd]] = russian_lines[bd]
            ru_as_input_dic[russian_lines[bd]] = english_lines[bd]
    else:
        raise ValueError(
            "Can't build the dictionary. The English and the Russian parts of the dictionary have different lengths.")
    return en_as_input_dic, ru_as_input_dic


def replace_in_str(*args):
    """Returns a string where a given substr was replaced with another given substr.

    Args:
        *args (a bunch of arguments): it should contain 3 string arguments: source_str, oldsymb, newsymb
    """
    edited_str = ""
    source_str, oldsymb, newsymb = "", "", ""
    try:
        source_str, oldsymb, newsymb = args
        if isinstance(source_str, str):
            edited_str = source_str
    except Exception as e:
        print(e)
    try:
        edited_str = source_str.replace(oldsymb, newsymb)
    except Exception as e:
        print(e)
    return edited_str


def extract_words(*args):
    """Splits a string into words.

    Args:
        *args (a bunch of arguments): it should contain 1 string argument: the input string
    """
    symbols_to_remove = [":", ".", ",", ";", "?", "!", "\"", "\'", "’", "“", "”", "\\", "/", "(", ")", "[", "]", "0",
                         "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "-", "–", "https", "http", "html", "htm",
                         "www", ">", "<", "+", "=", "%", "&", "$", "€", "#", "@", "~", "…", "→", "^", "*", "°c", "¼",
                         "„", "№", "—", "‘", "⁸", "−", "{", "|", "}", "°", "×", "[", "]"]

    common_abbreviation_artefacts = [
        "t",  # from can't and don't
        "re",  # from you're
        "ve",  # from we've etc
        "m",  # from i'm
        "s",  # from multiples, she's etc
        "ll",  # from we'll etc
        "don",
        "doesn",
        "haven",
        "g",
        "e"
    ]

    try:
        i_str = args[0]

        i_str = i_str.lower()
        for i in range(len(symbols_to_remove)):
            i_str = replace_in_str(i_str, symbols_to_remove[i], " ")

        wordis = i_str.split()

        for i in range(len(wordis)):
            stripped = wordis[i].strip()
            wordis[i] = stripped

        clean_words = []
        for w in wordis:
            if w not in common_abbreviation_artefacts:
                clean_words.append(w)
    except Exception as e:
        print(e)
        clean_words = []
    return clean_words


def get_common_letters(str1, str2):
    """Returns a set of letters common for the both input strings.

    Args:
        str1 (str): any string
        str2 (str): any string
    """
    letters1 = set(str1)
    letters2 = set(str2)
    common_letters = letters1.intersection(letters2)
    return common_letters


def detect_lang(text):
    """Detects the language of the input text and returns "Russian" or "English" accordingly

    Args:
        text (str): a Russian- or a English-language text
    """
    russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    common_letters = get_common_letters(text, russian_alphabet)
    if len(common_letters) > 0:
        language = "Russian"
    else:
        language = "English"
    return language


def similarity_score(word1, word2):
    """Calculates how similar are the two input strings, using a naive metric based on the count of common letters.

    Args:
        word1, word2 (str): any string
    """
    common_letters = get_common_letters(word1, word2)
    sim_score = 2 * len(common_letters) / (len(word1) + len(word2))
    return sim_score


def find_most_similar_word(words_list, test_word):
    """Returns a word from words_list that is the most similar to the test_word.

    Args:
        words_list (a list of strings): a list of words to compare with test_word
        test_word (str): a word, for which a similar world must be found
    """
    best_word = None

    if len(test_word) > 4:
        for w in words_list:
            if len(w) > 4:
                if (test_word in w) or (w in test_word):
                    best_word = w
                    break

    if best_word is None:
        best_score = 0
        for w in words_list:
            score = similarity_score(w, test_word)
            if score > best_score:
                best_score = score
                best_word = w
    return best_word


def translate_word(word, dictionary):
    """Translates the given word according to the provided dictionary.

    Args:
        word (str): any word of the same language as the dictionary keys
        dictionary (dict): looks like this: {en_word: ru_word, ...}, or like this: {ru_word: en_word, ...}
    """
    if word in dictionary.keys():
        word_to_use = dictionary[word]
        similar = ""
    else:
        similar = find_most_similar_word(list(dictionary.keys()), word)
        if similar is not None:
            word_to_use = dictionary[similar]
        else:
            word_to_use = word
    return word_to_use, similar


def translate_text(text, bilingual_dictionary):
    """Translates the text according to the provided dictionary. It's a word-by-word translation.

    Args:
        text (str): any text of the same language as the dictionary keys
        bilingual_dictionary (dict): looks like this: {en_word: ru_word, ...}, or like this: {ru_word: en_word, ...}
    """
    words = extract_words(text)
    print("\nExtracted the following words:\n" + str(words))
    print("\nCommencing a word-by-word translation.\n")

    text_translation = ""
    for t in range(len(words)):
        word_to_use, similar = translate_word(words[t], bilingual_dictionary)
        print(words[t] + " --> " + similar + " --> " + word_to_use)
        text_translation += word_to_use + " "
    return text_translation


en_lines = file_read_and_cleanup("en_ru_dic/en.txt")
ru_lines = file_read_and_cleanup("en_ru_dic/ru.txt")
en_as_input, ru_as_input = build_dictionaries(en_lines, ru_lines)

user_request = ""
while user_request != "exit":
    user_request = input("Please enter a text to translate, or type 'exit' to exit\n")
    clean_request = user_request.strip().lower()

    lang = detect_lang(clean_request)
    if lang == "Russian":
        trans_dict = ru_as_input
    else:
        trans_dict = en_as_input
    print("\n" + lang + " language detected.\n")

    translation = translate_text(clean_request, trans_dict)

    print("\nTranslation:\n" + translation + "\n")
