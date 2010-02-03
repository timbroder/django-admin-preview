class PreviewAdmin(admin.ModelAdmin):
    #add to your ModelAdmin
    #list_display = ('headline','created_date', 'state', 'admin_slide_preview')
    def admin_slide_preview(self, obj):
        return "<div class=\"previewslide\" id=\"%s/preview/\">+</div>" % obj.id
    admin_slide_preview.allow_tags = True
    admin_slide_preview.short_description = 'Preview'
    
    def get_preview(self, request, object_id):
        sub = self.queryset(request)[0]
        template = "preview/%s.html" % sub.__class__.__name__
        return object_detail(request, queryset=self.queryset(request), object_id=object_id, template_name=template.lower())
        
    def get_urls(self):
        urls = super(PreviewAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^(?P<object_id>\d+)/preview/$', self.get_preview),
        )
        return my_urls + urls
    
    class Media:
        js = js = ('js/jquery.js',
                   'js/jquery.adminpreview.js'
