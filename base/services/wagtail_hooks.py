from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import ProductPage, ServicePage, ServiceWithFeePage


class ProductPageAdmin(ModelAdmin):
    model = ProductPage
    menu_label = 'Products'
    menu_icon = 'doc-empty-inverse'
    list_display = ('title', 'service')
    search_fields = ('title')


class ServicePageAbstractAdmin(ModelAdmin):
    model = ServicePage
    menu_label = 'Services'
    menu_icon = 'doc-empty'
    list_display = ('title', 'content')
    search_fields = ('title', 'content')


class ServicePageAdmin(ServicePageAbstractAdmin):
    pass


class ServiceWithFeePageAdmin(ServicePageAbstractAdmin):
    model = ServiceWithFeePage
    menu_label = 'Services With Fee'


class ServicesAndProductsGroup(ModelAdminGroup):
    menu_label = 'Services & Products'
    menu_icon = 'folder-open-1'
    menu_order = 200
    items = (ServicePageAdmin, ServiceWithFeePageAdmin, ProductPageAdmin)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(ServicesAndProductsGroup)