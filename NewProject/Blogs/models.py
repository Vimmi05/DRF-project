from django.db import models

class BlogModel(models.Model):
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3965221937.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2181143252.
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name