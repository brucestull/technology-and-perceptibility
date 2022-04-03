from django.db import models
from tap_project.settings import AUTH_USER_MODEL


class Tap(models.Model):
    """
    Python class for TAPs, the objects which will hold the url,
    url title, and url description.
    """
    # `default='http://localhost:8000/'`
    url = models.URLField(
        help_text='url of page which has content of interest for accessiblity',
        blank=True
        )
    title = models.CharField(
        max_length=200,
        help_text='short title for the url item'
        )
    url_label = models.CharField(
        max_length=200,
        help_text='text for displaying in link label'
        )
    description = models.CharField(
        'extended description',
        max_length=400,
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

    class Meta:
        ordering = ['-id']

    # created_date = models.DateTimeField('date created', auto_now_add=True, help_text='date the TAP was created')
    # deleted = models.BooleanField(default=False, help_text='designates whether the TAP should be shown in list view')

    def __str__(self):
        # return f'{self.id}: {self.title} - Deleted[{self.deleted}]'
        return f'{self.id}: {self.title}'
    
    # def is_deleted(self):
    #     """
    #     Returns whether TAP is in deleted status or not.
    #     """
    #     return self.deleted

    # def delete(self):
    #     """
    #     Set the deleted status of a TAP to True.
    #     """
    #     self.deleted = True
