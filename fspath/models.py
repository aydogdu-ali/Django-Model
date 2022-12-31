from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True) #blank= True boş bırakılabilir null =True ise null verilebilir
    register = models.DateTimeField(auto_now_add=True) #saat ve tarihi alır. auto_now_add parametresi ilk kayıtta oluşturur.
    last_update_date= models.DateTimeField(auto_now=True)
    # auto_now parametresi ile son güncelleme tarihi ve saati oluşturulur. Herhangi bir değişiklikte.
    is_active = models.BooleanField()

    def __str__(self): # bu method ile objelerimizin görüntüsünü ayarlarız.
        return f"{self.number} {self.first_name}" 

    class Meta:
        ordering = ["number"] # tablonun numara sırasına göre sıralar
        verbose_name_plural = "Student_list" #tablonun adını değiştirir. Çoğul tarafını
        verbose_name = "Student_only" # tablonun tekil isimlerini gösterir.