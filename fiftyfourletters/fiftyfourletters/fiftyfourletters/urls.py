"""
URL configuration for fiftyfourletters project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, profile, signup
from core.views import login, logout, search, genres
from core.views import books_by_genre, book_details
# importExcel

urlpatterns = [
    # path('import/', importExcel, name='push_excel'),

    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('genres/', genres, name='genres'),
    path('genres/<str:genre_id>/', books_by_genre, name='books_by_genre'),
    path('book_details/<int:rec_id>/', book_details, name='book_details'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
                                 document_root=settings.MEDIA_ROOT)
