from django.db import models


class MyModel(models.Model):
    field = models.JSONField("Хитрое JSON поле")

    class Meta:
        db_table = "mymodel"
