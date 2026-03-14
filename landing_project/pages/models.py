from django.db import models

class Landing(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)

    cta_title = models.CharField(max_length=200)
    cta_button = models.CharField(max_length=100)

    def __str__(self):
        return self.hero_title

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name

class Section(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero'),
        ('features', 'Features'),
        ('testimonials', 'Testimonials'),
        ('cta', 'CTA'),
    ]

    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.section_type} ({self.order})"

class Landing(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)

    cta_title = models.CharField(max_length=200)
    cta_button = models.CharField(max_length=100)

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"






