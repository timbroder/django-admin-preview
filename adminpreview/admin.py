from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from django.views.generic.list_detail import object_detail

class PreviewAdmin(admin.ModelAdmin):
    class Media:
        js = ['js/jquery.adminpreview.js']
        css = dict(
            all = ['css/adminpreview.css']
        )
    
    def admin_slide_preview(self, obj):
        """
        Add this to your ModelAdmin:
        
        list_display = ('headline','created_date', 'state', 'admin_slide_preview')
        """
        return "<div class=\"previewslide\" id=\"%s/preview/\">+</div>" % obj.id
    admin_slide_preview.allow_tags = True
    admin_slide_preview.short_description = 'Preview'

    def get_preview(self, request, object_id):
        sub = self.queryset(request)[0]
        template = "preview/%s.html" % sub.__class__.__name__
        return object_detail(request, queryset=self.queryset(request), object_id=object_id, template_name=template.lower())

    def get_urls(self):
        my_urls = patterns('',
            url(r'^(?P<object_id>\d+)/preview/$', self.admin_site.admin_view(self.get_preview)),
        )
        return my_urls + super(PreviewAdmin, self).get_urls()
