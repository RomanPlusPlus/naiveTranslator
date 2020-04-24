Translates text from Russian to English, and the other way around. Also detects the input language.

The translation is done word-by-word, using a very limited dictionary of 12 tsd entries.

NaiveTranslator could be useful as a baseline, as it's *very* hard to get a worse translation quality:) 
If your fancy ML translator is even worse, then there is something terribly wrong with it. 

### Features

- Translates between Russian and English
- Detects the input language
- Command-line interface
- Pure Python. We don't even import any build-in libs, not to mention NLTK etc. 
- fewer than 300 LOC

### Dictionary

The dictionary was build by google-translating the 12 000 most common words of the spoken Russian.

The list of common words was obtained from [wiktionary.org](https://ru.wiktionary.org/wiki/Приложение:Список_частотности_по_НКРЯ:_Устная_речь_1—1000
). The list is authored by Sobloku, Exuwon, Alone Coder, Vesailok, Al Silonov, and is available under the Creative
Commons Attribution-ShareAlike 3.0. license.
