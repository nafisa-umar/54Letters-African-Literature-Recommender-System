from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Book, Genre
from django.db.models import Q
from .recommend import recommend

# from tablib import Dataset
# from .resources import BookResource

# Create your views here.
# uploading data


# def importExcel(request):
#     if request.method == "POST":
#         book_resource = BookResource()
#         dataset = Dataset()
#         new_books = request.FILES['my_file']
#         imported_data = dataset.load(new_books.read(), format="xlsx")
#         for data in imported_data:
#             value = Book(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3],
#                 data[4],
#                 data[5],
#                 data[6],
#                 data[7],
#                 data[8],
#                 data[9],
#                 data[10],
#                 data[11],
#                 data[12],
#                 data[13],
#                 data[14],
#                 data[15],
#             )
#             value.save()

#     return render(request, 'core/dashboard/form.html')


@login_required(login_url='login')
def index(request):
    return render(request, 'core/index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, 'An account already exists with this email')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
            # log user in and redirect to profile

            # creatie UserProfile for new user
            user_model = User.objects.get(username=username)
            new_profile = UserProfile.objects.create(
                user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('signup')

    else:
        return render(request, 'core/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'core/login.html')


@login_required(login_url='login')
def profile(request):
    genres = Genre.objects.all()

    if request.method == "POST":
        usergenre = request.POST.getlist('usergenres[]')
        print(usergenre)

    else:
        return render(request, 'core/profile.html', {
            'genres': genres
        })


@login_required(login_url='login')
def genres(request):
    genres = Genre.objects.order_by('?')[:20]

    return render(request, 'core/genres.html', {
        'genres': genres
    })

# show books by genre


def books_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, genre_id=genre_id)
    books = genre.book.all()

    return render(request,
                  'core/shelf/index.html',
                  {'genre': genre, 'books': books})


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        keyword = request.POST["keyword"]
        results = []

        if keyword:
            results = Book.objects.filter(
                # Q(soup__icontains=keyword) |
                Q(title__icontains=F" {keyword} ") |
                Q(title__istartswith=keyword) |
                Q(title__iendswith=keyword) |
                Q(author__icontains=F" {keyword} ") |
                Q(author__istartswith=keyword) |
                Q(author__iendswith=keyword)
            )

        return render(request, 'core/search.html',
                      {'results': results})

    else:
        return render(request, 'core/search.html')


def book_details(request, rec_id):
    book = get_object_or_404(Book, rec_id=rec_id)

    # similar books
    similar_book_ids = recommend(rec_id)
    similar_book_ids = similar_book_ids.astype(int)
    similar_books = Book.objects.filter(rec_id__in=similar_book_ids)

    # if not similar_books:
    #     similar_books = None

    return render(request, 'core/shelf/book_details.html',
                  {'book': book,
                   'similar_books': similar_books}
                  )


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
