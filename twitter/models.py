from django.db import models


class twitt(models.Model):
    auther = models.ForeignKey(
        "Account.CustomUser", on_delete=models.CASCADE, default=None, related_name='twittes')
    
    text = models.CharField(max_length=500, verbose_name='متن')
    
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد', null=True)

    class Meta:
        ordering = ['-created',]
