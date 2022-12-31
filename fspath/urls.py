from django.urls import path
from .views import home # urls çalışacak olan fonksiyonu 
#views.py sayfasından çağırıyoruz

urlpatterns = [

path("",home)# urlde girilen path gelince home fonksiyonunu return eder.

]