from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Variation, Revisions


def update_price(modeladmin, request, queryset):
    price = 20.00
    queryset.update(price=price)
    update_revision = Revisions.objects.filter(product=queryset).last()
    if update_revision:
        update_revision.price = price
        update_revision.save()
    else:
        new_revision = Revisions.objects.create(product=queryset[0])
        new_revision.title = queryset[0].title
        new_revision.description = queryset[0].description
        new_revision.price = queryset[0].price
        new_revision.sale_price = queryset[0].sale_price
        new_revision.slug = queryset[0].slug
        new_revision.timestamp = queryset[0].timestamp
        new_revision.active = queryset[0].active
        new_revision.updated = queryset[0].updated
        new_revision.save()


update_price.short_description = 'update the product price'


def create_revision(obj):
    revisions = Revisions.objects.create(product=obj)
    revisions.title = obj.title
    revisions.description = obj.description
    revisions.price = obj.price
    revisions.sale_price = obj.sale_price
    revisions.slug = obj.slug
    revisions.timestamp = obj.timestamp
    revisions.active = obj.active
    revisions.updated = obj.updated
    revisions.save()


class ProductAdmin(admin.ModelAdmin):
    actions = [update_price]
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = ['__unicode__', 'title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        check_product = Product.objects.get(pk=obj.id)
        super(ProductAdmin, self).save_model(request, obj, form, change)
        if check_product:
            print "got 1"
            print check_product.id
            try:
                post_request = request.POST['title']
            except:
                post_request = None
            if check_product.title != post_request and post_request is not None:
                print "catch"
                print "#" * 10
                print check_product.title

                create_revision(check_product)
            # else:
            #     revisions = Revisions.objects.filter(product=check_product).last()
            #     if revisions:
            #         revisions.title = check_product[0].title
            #         revisions.description = obj.description
            #         revisions.price = obj.price
            #         revisions.sale_price = obj.sale_price
            #         revisions.slug = obj.slug
            #         revisions.timestamp = obj.timestamp
            #         revisions.active = obj.active
            #         revisions.updated = obj.updated
            #         revisions.save()
            #     else:
            #         create_revision(obj)

                    # get the last revision to the product

                    # revisions = Revisions.objects.filter(product=obj).last()
                    # if revisions:
                    #     if revisions.title != obj.title or revisions.description != obj.description:
                    #         create_revision(obj)
                    # else:
                    #     revisions.title = obj.title
                    #     revisions.description = obj.description
                    #     revisions.price = obj.price
                    #     revisions.sale_price = obj.sale_price
                    #     revisions.slug = obj.slug
                    #     revisions.timestamp = obj.timestamp
                    #     revisions.active = obj.active
                    #     revisions.updated = obj.updated
                    #     revisions.save()


class Meta:
    model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(Revisions)
