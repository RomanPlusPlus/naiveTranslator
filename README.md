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

### Translation quality

Sample input: 
> Питательные вещества попадают в живой организм, где усваиваются клетками с целью выработки и накопления энергии, поддержания жизнедеятельности, а также обеспечения ростовых процессов и созревания. Обычно пища делится по происхождению на растительную и животную. 

Output of the NaiveTranslator:
> to fasten sveta from here in alive organ where get along mainland with chain production and repentance energy imitation connect a also security rostov process and ugly usually food see by origin on the grow and stomach

For comparison, the output of the Google Translate:
> Nutrients enter a living organism, where they are absorbed by cells in order to generate and store energy, support vital functions, and also ensure growth processes and maturation. Usually food is divided by origin into plant and animal.

As one can see, the translation quality of the NaiveTranslator is terrible. 

### How to use

1. dowload this repo. 
2. cd to the dir where naiveTranslator.py is located
3. launch it
4. enter a text to translate and press Enter

### Dictionary

The dictionary was build by google-translating the 12 000 most common words of the spoken Russian.

The list of common words was obtained from [wiktionary.org](https://ru.wiktionary.org/wiki/Приложение:Список_частотности_по_НКРЯ:_Устная_речь_1—1000
). The list is authored by Sobloku, Exuwon, Alone Coder, Vesailok, Al Silonov, and is available under the Creative
Commons Attribution-ShareAlike 3.0. license.
