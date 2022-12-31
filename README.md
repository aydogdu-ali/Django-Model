# Django-Model
MODELS

Model, database de tutacağımız verileri şekillendireceğimiz yerdir.
ORM (Object Relational Mapping) database sorgulama işlemlerini python kodları ile yapıyoruz. ORM bu kodları  arka planda sorgu diline çevirir.
 
 

Django’da model oluşturma için öncelikle 
from django.db import models  import edilir. #default gelen Models yapısı kullanılır.
Class Student(models.Model): # Student Tablo ismi
first_name= models.CharField(maz_length=30)
last_name= models.CharField(maz_length=30)
number = models.IntegerField()

Model de işlem yaparsak python manage.py makemigrations komutu çalıştırılır ve arka planda tabloların yapılması için hazırlık süreci yapar.
python manage.py migrate komutu ile de tablolar oluşturulur. 
Model de her bir değişiklik yaptığımızda bu komutlar tekrar çalıştırılır. Ve Database de modelimizi tabloları oluşturmuş oluruz.

Database oluşturduğumuz tabloları görmek için admin panele giriş yapmalıyız.
Bunun için önce super kullanıcı olarak giriş yapmaktayız.
Bunu yapmak için terminale  python manage.py createsuperuser komutunu çalıştırırız.
Burada bize kullanıcı adı, email ve şifre sorar bunları doldurup superuser oluşturulur.
Sonra admin panele gideriz.

 
Buraya girdiğimizde oluşturduğumuz database tablosunu göremiyoruz. Bunu görmek için
Fspath app içinde bulunan “admin.py” dosyasının içerisine oluşturduğumuz modeli import ediyoruz.

 
Bu işlemden sonra tekrar “admi”n panele gittiğimizde öğrenci tablosunun geldiğini görürüz.
 




Admin panelden veri eklediğimizde oluşturulan veri obje olarak gözükür.
 
Biz bu objeleri database tablosunda istediğimiz gibi adlandırarak gösterebiliriz. Bunun için
Model içinde tanımlı olan  classın  def __str__ methodunu kullanırız.
Bu method bizim database tablomuzda herhangi bir değişiklik yapmaz.
  
 

Meta classı bize birtakım kolaylıklar sağlar örneğin sıralama
 Class Meta:
	Ordering = [“number”] dersek tabloları numara sırasına göre sıralar.
	verbose_name_plural = "Student_list" #tablonun adını değiştirir. Çoğul tarafını gösterir.
        verbose_name = "Student_only" # tablonun tekil isimlerini gösterir.


 

Shell/terminalde ORM komutlarını yazmak için
python manage.py shell  komutunu kullanırız.

Sonra sorgu yapacağımız modeli import ederiz.
from fspath.models import Student
s1 = Student.objects.all() dersek tablodaki tüm öğrencileri çekeriz. Görmek için
s1 yazıp enter tuşuna basarız.
S2 = Student.objects.get(number=123) dersek belirttiğimiz numaralı öğrenci gelir.
Shell’den çıkmak için exit() komutu kullanılır.
