# I'm contanstantly neededing a model that has a title, excerpt, pub date, publish_status. So I have absctracted this to a common base type
from django.db import models
from django.conf import settings
import datetime

class PublishedGenericArticleManager(models.Manager):
    ''' manager to return only published stories '''
    def get_query_set(self):
        return super(PublishedGenericArticleManager, self).get_query_set().filter(status=self.model.PUBLISHED_STATUS)

# An Abstract Model for the base of story type models
class GenericArticle(models.Model):
    ''' An abstract model for common article model types '''
    
    title = models.CharField(max_length=250, help_text='Max 250 characters')
    slug = models.SlugField(unique_for_date='publish_date', db_index=True,help_text='Suggested value automatically generated from title. Must be unique for publish date.')
    excerpt = models.TextField(blank=True, help_text="A short summary or tag line. Optional")
    content = models.TextField()
    
    publish_date = models.DateTimeField(default=datetime.datetime.now, db_index=True)
    
    # Status Field
    PUBLISHED_STATUS, DRAFT_STATUS = xrange(2)
    STATUS_CHOICES = (
        (PUBLISHED_STATUS, 'Published'),
        (DRAFT_STATUS, 'Draft'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS, db_index=True,
                                 help_text="Only entries with 'Published' status are publicly displayed" )
    
    # Managers
    objects = models.Manager()
    published = PublishedGenericArticleManager()
    
    class Meta:
        abstract = True
