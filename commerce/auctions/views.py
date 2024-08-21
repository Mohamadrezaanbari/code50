from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Category, Listing, Comment , Bid

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    is_listing_in_watchlist = request.user in listing.watchlist.all()
    comments = listing.comments.all()
    is_owner = request.user.username == listing.owner.username
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "is_listing_in_watchlist": is_listing_in_watchlist,
        "is_owner": is_owner,
        "comments": comments
        })
def closed_listings(request):
    closed_listing = Listing.objects.filter(is_closed=True)
    return render(request, "auctions/closed_listing.html", {
         "listings": closed_listing
    })

def closeAuction(request,listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.is_closed = True
    listing.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))

def comment(request, listing_id):
    user = request.user
    text = request.POST["comment"]
    listing = listing = Listing.objects.get(pk=listing_id)
    new_comment = Comment(text=text, writer=user, listing=listing)
    new_comment.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))

def addBid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    current_bid = listing.bid.bid
    new_bid = bid = int(request.POST["bid"])
    if new_bid > current_bid:
           updated_bid = Bid(bid=new_bid, user=request.user)
           updated_bid.save()
           listing.bid = updated_bid
           listing.save()
           return render(request, "auctions/listing.html", {
               "listing": listing,
               "message": "Bid was updated successfully",
               "updated": True,
            })
    else:
           return render(request, "auctions/listing.html", {
               "listing": listing,
               "message": "Bid not high enough",
               "updated": False,
            })

def AddNewComment(request, listing_id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=listing_id)
    message = request.POST
    newComment = Comment(
        author = currentUser,
        listing = listingData,
        message=message
    )
    newComment.save()
    return HttpResponseRedirect(reverse("listing",args={listing_id, } ))
def displayWatchlist(request):
        user = request.user
        listings = user.watch_listings.all()
        return render(request, "auctions/watchlist.html", {
            "listings": listings
        })

def removeWatchlist(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing", args=(listing_id, )))

def addWatchlist(request,listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing", args=(listing_id, )))
def display_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    is_listing_in_watchlist = request.user in listing.watchlist.all()
    comments = listing.comments.all()
    is_owner = request.user.username == listing.owner.username
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "is_listing_in_watchlist": is_listing_in_watchlist,
        "is_owner": is_owner,
        "comments": comments
    })

def index(request):
        listings = Listing.objects.filter(is_closed=False)
        return render(request, "auctions/index.html", {
                 "listings": listings
            })

def displayCategory(request):
        category = request.POST["category"]
        listings= Listing.objects.filter(category=category)
        return render(request, "auctions/index.html", {
        "listings": listings,
        })
def create(request):
    if request.method == "POST":
        user = request.user
        title = request.POST["title"]
        description = request.POST["description"]
        image_url = request.POST.get("image_url")
        category = request.POST['category']

        #Create new bid
        bid = Bid(bid=int(request.POST["bid"]), user=user)
        bid.save()
        #Create new listing
        listing = Listing(title=title, category=category, owner=user, is_closed=False, description=description, bid=bid, url=image_url)
        listing.save()

        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/create.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
