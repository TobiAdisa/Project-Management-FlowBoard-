from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    # id = models.AutoField(primary_key=True)
    profile_image = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'users'
        managed = True

    def _str_(self):
        return self.username


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=False)

    lead = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects_led'
    )

    project_manager = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects_managed'
    )

    status = models.CharField(default="Pending", max_length=50)
    start_date = models.DateField(null=False)
    completed_on = models.DateField(null=True, blank=True)

    members = models.ManyToManyField(
        Users,
        related_name='projects',
        blank=True
    )

    class Meta:
        db_table = 'projects'
        managed = True

    def _str_(self):
        return self.title


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(default="Pending", max_length=50)
    priority = models.CharField(null=False, max_length=50)
    category = models.CharField(null=False, max_length=100)

    project = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        null=False,
        related_name='tasks'
    )

    assigned_users = models.ManyToManyField(
        Users,
        related_name='assigned_tasks',
        blank=True
    )

    start_date = models.DateField(null=False)
    due_date = models.DateField(null=False)
    completed_on = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'tasks'
        managed = True

    def _str_(self):
        return self.title
