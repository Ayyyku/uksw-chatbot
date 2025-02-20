import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import numpy as np
from typing import List

def tokenize(sentence: str) -> List[str]:
    '''
    Fungsi untuk memisahkan kalimat menjadi kumpulan kata
    '''
    return nltk.word_tokenize(sentence)
    

def stem(word: str) -> str:
    '''
    Fungsi untuk menghilangkan imbuhan pada kata
    '''
    stemmer = StemmerFactory().create_stemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence: List[str], all_words: List[str]) -> List[float]:
    '''
    Fungsi untuk membuat one-hot encoding list
    '''
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bow = np.zeros(len(all_words), dtype = np.float32)
    for idx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bow[idx] = 1.
    return bow