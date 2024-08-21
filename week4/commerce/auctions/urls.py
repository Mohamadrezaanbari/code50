from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("<int:listing_id>", views.display_listing, name="display_listing"),
    path("<int:listing_id>/addWatchlist", views.addWatchlist, name="addWatchlist"),
    path("<int:listing_id>/removeWatchlist", views.removeWatchlist, name="removeWatchlist"),
    path("<int:listing_id>/addBid", views.addBid, name="addBid"),
    path("<int:listing_id>/comment", views.comment, name="comment"),
    path("<int:listing_id>/AddNewComment", views.AddNewComment, name="AddNewComment"),
    path("<int:listing_id>/closeAuction", views.closeAuction, name="closeAuction"),
    path("displayWatchlist", views.displayWatchlist, name="displayWatchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("create", views.create, name="create")
]
