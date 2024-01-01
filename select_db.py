from models import Author, Quote
from connect import *
from mongoengine import connect

# Підключення до MongoDB
connect(db='kolosok', host=uri, port=27017)


def get_all_authors():
    authors = Author.objects()
    for author in authors:
        print(author.to_mongo().to_dict())
    print(authors)    


def get_all_quotes():
    quotes = Quote.objects()
    for quote in quotes:
        print(quote.to_mongo().to_dict())
    print(quotes)


# Пошук цитат за тегом
def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    print("Цитати з тегом '{}':".format(tag))
    for quote in quotes:
        print("- {}".format(quote.quote))
    print()


# Пошук цитат за ім'ям автора
def search_by_author(author_fullname):
    auth = Author.objects(fullname=author_fullname).first()
    if author:
        quotes = Quote.objects(author=auth)
        print("Всі цитати автора '{}':".format(author_fullname))
        for quote in quotes:
            print("- {}".format(quote.quote))
    else:
        print("Автор '{}' не знайдений.".format(author_fullname))
    print()


#Пошук цитат за набором тегів
def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    # quotes = Quote.objects(tags__in=tag_list)
    print("Цитати з тегами '{}':".format(tags))
    for quote in quotes:
        print("- {}".format(quote.quote))
    print()


# # Основний цикл виконання скрипту
if __name__ == '__main__':
   
    while True:
        command = input("Введіть ім'я автора або тег: name:<author>, tag:<tag>, tags:<tag1,tag2>, або exit для виходу: ")
        parse_com = command.split(':')

        if parse_com[0] == 'name':
            author = parse_com[1].strip()
            search_by_author(author)
        elif parse_com[0] == 'tag':
            tag = parse_com[1].strip()
            search_by_tag(tag)
        elif parse_com[0] == 'tags':
            tags = parse_com[1].strip()
            search_by_tags(tags)
        elif parse_com[0] == 'exit':
            break
        else:
            print("Команда невідома, спробуйте ще раз, будь ласка!")





