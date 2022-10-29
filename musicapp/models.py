from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=30, help_text = "enter your first name here(i.e your own name)")
    last_name = models.CharField(max_length=30,  help_text = "enter your surname here(i.e your father's name)")
    age = models.PositiveIntegerField(help_text = "Enter your age in whole number")
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.age}"

    class Meta:
        verbose_name = "Artiste"
        verbose_name_plural = "Artists"

    
        
class Song(models.Model):
    title = models.CharField(max_length=40, help_text = "Enter the name of the song here")
    date_released = models.DateField(null=True)
    likes = models.PositiveIntegerField()
    artiste = models.ForeignKey("Artiste", on_delete = models.CASCADE)
    # lyrics = models.ManyToManyField("Lyrics", help_text = "Enter Lyrics here")

    def __str__(self):
        return f"{self.id} {self.title}"
      

class Lyrics(models.Model):
    content = models.TextField(help_text="enter lyrics here")
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Lyric"
        verbose_name_plural = "Lyrics"
    
    def __str__(self):
        return f"{self.content}"
        # return f"{self.content}"