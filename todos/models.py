from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo",
                             max_length=100, blank=False, null=False)
    create_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(
        verbose_name="Data de entreg", null=False, blank=False)
    finished_at = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
