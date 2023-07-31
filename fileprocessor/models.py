from django.db import models

class Upload(models.Model):
    STATUS_CHOICES = [
        ('UP', 'Uploaded'),
        ('PR', 'Processing'),
        ('CO', 'Complete'),
    ]

    file = models.FileField(upload_to='uploads/')
    url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='UP')
    result = models.TextField(blank=True, null=True)
   
    PRODUCT_CHOICES = [
        ('EB', 'E-book'),
        ('BP', 'Blog Post'),
        # Adicione mais opções aqui conforme necessário
    ]

    product = models.CharField(max_length=2, choices=PRODUCT_CHOICES, null=True)

    class Upload(models.Model):
    # ...
    ebook_title = models.CharField(max_length=200, blank=True, null=True)
    # ...