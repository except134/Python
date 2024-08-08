import io

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for l in file:
                    l = l.lower()
                    symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for s in symbols:
                        l = l.replace(s, '' if s != ' - ' else ' ')
                    words.extend(l.split())
                all_words[file_name] = words
        return all_words
   
    def find(self, word):
        ret = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                ret[name] = words.index(word) + 1
        return ret

    def count(self, word):
        ret = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            ret[name] = words.count(word)
        return ret
    
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

