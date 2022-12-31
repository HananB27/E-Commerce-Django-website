from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed_listings", views.closedListings, name="closed_listings"),
    path("<int:listing_id>", views.displayListing, name="display_listing"),
    path("<int:listing_id>/add_watchlist", views.addWatchlist, name="add_watchlist"),
    path("<int:listing_id>/remove_watchlist", views.removeWatchlist, name="remove_watchlist"),
    path("<int:listing_id>/new_bid", views.newBid, name="new_bid"),
    path("<int:listing_id>/comment", views.comments, name="comment"),
    path("<int:listing_id>/close_auction", views.closeAuction, name="close_auction"),
    path("display_watchlist", views.displayWatchlist, name="display_watchlist"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("display_category", views.displayCategory, name="display_category"),
    path("create_listing", views.createListing, name="create_listing"),
    

]