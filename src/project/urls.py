"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from src.accounts import urls as accounts_urls
from src.book_review import urls as review_urls
from src.books.urls import booksurlpatterns
from src.root import urls as rooturls
from src.shopping import urls as shopping_urls
from src.store_admin import urls as admin_urls

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('shopping/', include(shopping_urls)),
    path('admin/', include(admin_urls)),
    path('books/', include(booksurlpatterns)),
    path('reviews/', include(review_urls)),
    path('', include(rooturls)),
]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
