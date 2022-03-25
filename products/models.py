
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)

    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

  


AMOUNT = (
    ('SIZE' , 'SIZE'),
    ('MEDIUM', 'MEDIUM'),
    ('LARGE', 'LARGE'),
    ('X-LARGE', 'X-LARGE')
)

class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='product/')
    category = models.ForeignKey(Category, verbose_name=_("category"), related_name='product_category', on_delete=models.CASCADE)
    price = models.FloatField(_("price"))
    discount_price = models.FloatField(_("discount price"))
    discount_perc =  models.IntegerField(_("discount perc"))
    rating = models.IntegerField(_("rating"))
    rated_people_num = models.IntegerField(_("people rating number "))
    sold_num = models.IntegerField(_("sold quqntity number "))
    description = models.TextField(_("description"))
    quantity = models.IntegerField(_("quantity"))
    avail_check = models.BooleanField(_("avail  checking ") , default=True)
    avail_num = models.IntegerField(_("avail number"))
    slug = models.SlugField(_("slug") , blank=True, null=True)


    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product , self).save(*args, **kwargs)






class Team(models.Model):

    """Model definition for Team."""
    name =  models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='teams/')
    desc = models.TextField(_("description"))
    job  = models.CharField(_("job"), max_length=50)

    # TODO: Define fields here

    class Meta:
       

        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
       
        return self.name




class Newsletter(models.Model):
    email = models.EmailField(_("email"), max_length=254)
    created_at = models.DateTimeField(_("created at"), default=timezone.now())

    

    class Meta:
        verbose_name = _("Newsletter")
        verbose_name_plural = _("Newsletters")

    def __str__(self):
        return self.email

