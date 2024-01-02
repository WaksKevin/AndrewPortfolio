import json
from datetime import date
from pathlib import Path
from django.db import models
from django.urls import reverse
from django.http import request
from easy_thumbnails.fields import ThumbnailerImageField


class SiteInfo(models.Model):
    class Meta:
        verbose_name_plural = "Site Information"
        db_table = "site"

    logo = ThumbnailerImageField(upload_to="base/site/img", help_text="")
    site_title = models.CharField(max_length=255, help_text="")
    tagline = models.CharField(
        max_length=255,
        help_text="In a few words describe what this site about e.g. 'Just another portfolio site'",
        blank=True,
    )
    site_icon = ThumbnailerImageField(
        upload_to="base/site/img",
        help_text="Site Icons are what you see in browser tabs, bookmark bars, and within the PWA mobile apps. Site Icons should be square and at least 512 x 512 pixels.",
    )
    theme_color = models.CharField(max_length=255, help_text="")
    manifest = models.FileField(upload_to="base/site")

    def __str__(self):
        return self.site_title

    def get_logo_name(self):
        return self.logo.name.split("/")[-1]

    def save(self, *args, **kwargs):
        domain = request.get_host()
        home_url = reverse("home")
        data = {
            "scope": home_url,
            "start_url": domain + home_url,
            "display": "standalone",
            "icons": [
                {
                    "sizes": "512x512",
                    "type": "image/png",
                    "src": f"./img/{self.get_logo_name()}",
                }
            ],
            "name": self.site_title,
            "short_name": self.site_title,
            "theme_color": self.theme_color,
            "background_color": "#262626",
        }

        content = json.dumps(data)
        prefix = Path("media")
        file_path = Path("base", "site", "manifest.webmanifest")
        ispath = prefix / file_path

        ispath.parent.mkdir(parents=True, exist_ok=True)  # making sure directory exists

        with open((prefix / file_path).resolve(), "w") as file:
            file.write(content)

        self.manifest.name = str(file_path)
        super().save(*args, **kwargs)


class Author(models.Model):
    class Meta:
        verbose_name_plural = "Author"
        db_table = "author"

    first_name = models.CharField(max_length=255, help_text="")
    last_name = models.CharField(max_length=255, help_text="")
    dob = models.DateField(help_text="Date of birth")
    profile_img = models.ImageField(upload_to="base/author/img")

    email = models.EmailField(help_text="")
    primary_phone_number = models.CharField(max_length=255, help_text="")
    secondary_phone_number = models.CharField(max_length=255, help_text="")
    address = models.CharField(max_length=255)

    facebook = models.URLField(max_length=255, help_text="", blank=True)
    twitter_x = models.URLField(max_length=255, help_text="", blank=True)
    instagram = models.URLField(max_length=255, help_text="", blank=True)
    linkedin = models.URLField(max_length=255, help_text="", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        birthday = self.dob
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age
