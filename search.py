import random
import pandas as pd

class Document:
    def __init__(self, title, text):
        # можете здесь какие-нибудь свои поля подобавлять
        self.title = title
        self.text = text
    
    def format(self, query):
        # возвращает пару тайтл-текст, отформатированную под запрос
        #return [self.title, self.text + ' ...']
        return [self.title, self.text]

index = []


def build_index():
    # считывает сырые данные и строит индекс
    df = pd.read_csv("SPotifyFeatures.csv")
    libr = df[["artist_name"]].values
    songs = df[["track_name"]].values
    for i in range(len(libr)):
        #index.append(Document(libr[i][0] + ' - ' + songs[i][0], 'None'))
        #index.append(Document(libr[i][0],songs[i][0]))
        index.append(Document(songs[i][0], libr[i][0]))
    #index.append(Document('The Beatles — Come Together', 'Here come old flat top\nHe come groovin\' up slowly'))
    #index.append(Document('The Rolling Stones — Brown Sugar', 'Gold Coast slave ship bound for cotton fields\nSold in the market down in New Orleans'))
    #index.append(Document('МС Хованский — Батя в здании', 'Вхожу в игру аккуратно,\nОна еще не готова.'))
    #index.append(Document('Физтех — Я променял девичий смех', 'Я променял девичий смех\nНа голос лектора занудный,'))
    #index.append(Document('Timati - Борода', 'У тебя есть  борода\nзначит скажу да'))
    #index.append(Document('The Beatles', 'Come Together' ))
    #index.append(Document('The Rolling Stones', 'Brown Sugar'))
    #index.append(Document('МС Хованский', 'Батя в здании'))
    #index.append(Document('Физтех', ' Я променял девичий смех'))
    #index.append(Document('Timati','Борода'))

def score(query, document):
    # возвращает какой-то скор для пары запрос-документ
    # больше -- релевантнее
    return random.random()

def retrieve(query):
    # возвращает начальный список релевантных документов
    # (желательно, не бесконечный)
    candidates = []
    for doc in index:
        if query.lower() in doc.title.lower() or query in doc.text.lower():
            candidates.append(doc)
    return candidates[:50]
