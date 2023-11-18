from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGallery


# Register your models here.

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class variationAdmin(admin.ModelAdmin):
    list_display=('product', 'variation_category','variation_value','is_active','created_date')
    list_editable=('is_active',)
    list_filter=( 'product', 'variation_category','variation_value')

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,variationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)