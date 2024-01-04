# from django.db import models

# class PortfolioItem(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='portfolio_images/')
#     link = models.URLField(blank=True)

#     def __str__(self):
#         return self.title


from django.db import models
import os

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the associated image file from the filesystem
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        # Call the "real" delete method
        super(PortfolioItem, self).delete(*args, **kwargs)
