from django.db import models
from tap_project.settings import AUTH_USER_MODEL


class Tap(models.Model):
    """
    Python class for TAPs, the objects which will hold the url,
    url label, and url description.
    """
    url = models.URLField(
        help_text='url of page which has content of interest for accessiblity',
        blank=True
        )
    url_label = models.CharField(
        max_length=200,
        help_text='text for displaying in link label'
        )
    description = models.TextField(
        'extended description',
        help_text='''
            extended description of what the link is about or,what kinds
            of information is found at url, or what is the importance of
            the link
        '''
        )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        # 'tap_project.settings.AUTH_USER_MODEL',   # This didn't work
        # 'users.CustomUser',                       # This didn't work
        related_name='taps',
        on_delete=models.CASCADE
        )
    created_date = models.DateTimeField(
        'date created',
        auto_now_add=True,
        help_text='date the Link was created'
        )
    public = models.BooleanField(
        'link is public',
        default=False
        )


    class Meta:
        ordering = ['-id']


    def __str__(self):
        return f'{self.id}: {self.url_label}'
    
