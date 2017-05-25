from django.conf.urls import url
from oscar.apps.catalogue.app import (
    BaseCatalogueApplication as DefaultCatApp,
    ReviewsApplication as DefaultReviewsApp
)

from shop.catalogue.views import product_or_category


class BaseCatalogueApplication(DefaultCatApp):
    def get_urls(self):
        urlpatterns = [
            url(r'^catalogue/$', self.catalogue_view.as_view(), name='index'),
            url(r'^(?P<slug>[\w-]+(/[\w-]+)*)/$', product_or_category,
                name='product_or_category'),
            url(r'^catalogue/ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range')
        ]
        return self.post_process_urls(urlpatterns)


class ReviewsApplication(DefaultReviewsApp):
    def get_urls(self):
        urlpatterns = [
            url(r'^(?P<product_slug>[\w-]*)_(?P<product_pk>\d+)/reviews/',
                self.reviews_app.urls)
        ]
        urlpatterns += super(ReviewsApplication, self).get_urls()
        return self.post_process_urls(urlpatterns)


class CatalogueApplication(ReviewsApplication, BaseCatalogueApplication):
    name = 'catalogue'


application = CatalogueApplication()
