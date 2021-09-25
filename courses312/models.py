from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200)
    imgpath = models.ImageField(verbose_name="Фото категории походу", upload_to='media')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f'{self.name}'


class Branch(models.Model):
    latitude = models.TextField(verbose_name="Широта", max_length=200)
    longitude = models.TextField(verbose_name="Долгота", max_length=200)
    address = models.TextField(verbose_name="Адрес", max_length=200)

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return f'{self.address}'


class Contact(models.Model):
    TYPE = (
        ("1-phone", "Phone"),
        ("2-facebook", "Facebook"),
        ("3-email", "Email"),
    )
    type = models.CharField(choices=TYPE, max_length=20, verbose_name="Тип")
    value = models.TextField(verbose_name="Значение", max_length=200)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        # return f'{self.value}'
        return f"{self.type} , {self.value}"


class Course(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание", max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    logo = models.ImageField(verbose_name="Фото логотипа", upload_to='media')
    contacts = models.ForeignKey(Contact, verbose_name="Контакты", on_delete=models.CASCADE)
    branches = models.ForeignKey(Branch, verbose_name="походу филиал", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f'{self.name}'
