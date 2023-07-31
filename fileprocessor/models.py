from django.db import models

class Upload(models.Model):
    STATUS_CHOICES = [
        ('UP', 'Uploaded'),
        ('PR', 'Processing'),
        ('CO', 'Complete'),
    ]

    PRODUCT_CHOICES = [
        ('EB', 'E-book'),
        ('BP', 'Blog Post'),
        # Adicione mais opções aqui conforme necessário
    ]

    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='UP')
    product = models.CharField(max_length=2, choices=PRODUCT_CHOICES, null=True)
    results = models.TextField(blank=True, null=True)
    ebook_title = models.CharField(max_length=200, blank=True, null=True)
    blog_post_title = models.CharField(max_length=200, blank=True, null=True)