"""oprosnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static

from oprosnik import settings
from questions.views import IndexView, QuestionView, AnswerView, TestsResults

urlpatterns = [
                  path('', IndexView.as_view(), name="IndexView"),
                  path('admin/', admin.site.urls),
                  path('test<int:test_id>/', QuestionView, name="QuestionView"),
                  path('test<int:test_id>/<int:pk>/', AnswerView.as_view(), name="AnswerView"),
                  path('statistic/<int:test_id>/', TestsResults, name="TestsResults"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
