from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models

class Places(models.Model):
    place_name      =       models.CharField(primary_key=True, max_length=100)
    information     =       models.CharField(max_length=255)
    location        =       models.PointField(srid=4326)
    objects         =       models.GeoManager()

    def __unicode__(self):
        return self.place_name

    class Meta:
        verbose_name_plural     =       'Places'



