from django.shortcuts import render
from .forms import GoogleBookForm
from django.views import View
import urllib.request
from json import load
from .models import Book

apikey = 'AIzaSyAeWfJpdw7Jp6v9yD33EKB31Z3FEkTjg1E'


def index(request):
    return render(request, "index.html")


class AddGoogleBookView(View):
    def get(self, request):
        googleform = GoogleBookForm
        return render(request, 'googlebook.html', {'form': googleform})

    def post(self, request):
        googleform = GoogleBookForm(request.POST)
        msg = 'Done'
        if googleform.is_valid():
            search_term = googleform.cleaned_data['search_terms']
            url = 'https://www.googleapis.com/books/v1/volumes?q=' + search_term + '&key=' + apikey
            json_obj = urllib.request.urlopen(url)
            data = load(json_obj)
            for i in data['items']:
                try:
                    title = i['volumeInfo']['title']
                    authors = ''.join(str(j) for j in i['volumeInfo']['authors'])
                    publishedDate = int(i['volumeInfo']['publishedDate'])
                    try:
                        categories = ''.join(str(j) for j in i['volumeInfo']['categories'])
                        average_rating = i['volumeInfo']['averageRating']
                        ratings_count = i['volumeInfo']['ratingsCount']
                        thumbnail = i['volumeInfo']['imageLinks']['thumbnail']
                    except KeyError:
                        msg = 'GoogleAPI error'
                    except TypeError:
                        msg = 'GoogleAPI error'
                    except ValueError:
                        msg = 'GoogleAPI error'
                    categories = ''
                    average_rating = 0
                    ratings_count = 0
                    thumbnail = ''
                    book = Book.objects.create(title=title, authors=authors, published_date=publishedDate,
                                               categories=categories, average_rating=average_rating,
                                               ratings_count=ratings_count, thumbnail=thumbnail)
                except KeyError:
                    msg = "Author/Title/Date Error"
        return render(request, 'googlebook.html', {'msg': msg})
