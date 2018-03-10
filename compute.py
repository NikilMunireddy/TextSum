from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def compute_un(u,n):
    LANGUAGE = "english"
    k=''
    SENTENCES_COUNT = n
    try:
        if k=='':
            url=u
        else:
            url='https://en.wikipedia.org/wiki/'+k
    except Exception:
        sent='you havent enterd url or key word'
        quit()
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    sent=[]
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sent.append(sentence)
    return sent


def compute_kn(k,n):
    LANGUAGE = "english"
    k=''
    SENTENCES_COUNT = n
    try:
        if k=='':
            pass
        else:
            url='https://en.wikipedia.org/wiki/'+k
    except Exception:
        sent='you havent enterd url or key word'
        quit()
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    sent=[]
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sent.append(sentence)
    return sent
