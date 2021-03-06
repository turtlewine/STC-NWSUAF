from django.contrib import admin
from .models import *

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']
    #添加链接
    list_display_links = ['name']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['name']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['name']
    #详细页面顺序
    #fields = ('email', 'name', 'age')
    #详细页面 属性分组
    #fieldsets = (
    #    ('基本设置',{
    #       'fields':('country', 'website')
    #    }),
    #    ('高级设置',{
    #        'fields':('name', 'address','city'),
    #        'classes':('collapse',)
    #    }),
    #)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['create_time', 'status']
    #添加链接
    list_display_links = ['create_time']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['create_time']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['status']
    #详细页面顺序
    #fields = ('email', 'name', 'age')
    #详细页面 属性分组
    #fieldsets = (
    #    ('基本设置',{
    #       'fields':('country', 'website')
    #    }),
    #    ('高级设置',{
    #        'fields':('name', 'address','city'),
    #        'classes':('collapse',)
    #    }),
    #)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['create_time', 'is_ongoing']
    #添加链接
    list_display_links = ['create_time']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['create_time']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['is_ongoing']
    #详细页面顺序
    #fields = ('email', 'name', 'age')
    #详细页面 属性分组
    #fieldsets = (
    #    ('基本设置',{
    #       'fields':('country', 'website')
    #    }),
    #    ('高级设置',{
    #        'fields':('name', 'address','city'),
    #        'classes':('collapse',)
    #    }),
    #)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ['create_time', 'feedback']
    #添加链接
    list_display_links = ['create_time']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['create_time']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['feedback']
    #详细页面顺序
    #fields = ('email', 'name', 'age')
    #详细页面 属性分组
    #fieldsets = (
    #    ('基本设置',{
    #       'fields':('country', 'website')
    #    }),
    #    ('高级设置',{
    #        'fields':('name', 'address','city'),
    #        'classes':('collapse',)
    #    }),
    #)
admin.site.register(Order, OrderAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Feedback, FeedBackAdmin)
admin.site.register(Evidence, EvidenceAdmin)