from django.contrib import admin
from django import forms
from generic_stories.models import GenericArticle

    
class GenericArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'mceEditor', 'size' : '40'}))

class GenericArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish_date',)
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ('title', 'content', 'excerpt',)
    list_filter = ('publish_date', 'status')
    date_hierarchy = 'publish_date'


    # Admin actions
    actions = ('make_published','make_draft',)
    
    # An Admin action to make a story published
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=GenericArticle.PUBLISHED_STATUS)
        if rows_updated == 1:
            message_bit = "1 object was"
        else:
            message_bit = "%s objects were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_published.short_description = "Mark selected as published"
    
    # An Admin action to make a story draft
    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status=GenericArticle.DRAFT_STATUS)
        if rows_updated == 1:
            message_bit = "1 object was"
        else:
            message_bit = "%s objects were" % rows_updated
        self.message_user(request, "%s successfully marked as draft." % message_bit)
    make_draft.short_description = "Mark selected as draft"
    
