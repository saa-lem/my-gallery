from django.shortcuts import render

# Create your views here.
def landing(request):
    posts = ImagePost.objects.all()
    post_list = []
    for post in posts:
        if post.recently_uploaded():
            post_list.append(post)
            return render(request,'general_templates/landing.html',{"post_list":post_list})
        else:
            return render(request, 'general_templates/index.html',{"posts":posts})


def index(request):
    posts = ImagePost.objects.all()

    context = {
        "posts":posts
    }
    return render(request, 'general_templates/index.html',context)


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imageposts = ImagePost.search_image(search_term)

        message = f"{search_term}"



        context = {
            "message":message,
            "posts":searched_imageposts
        }

        return render(request, 'general_templates/search.html', context)


    else:
        message = "You haven't searched for any term"

        return render(request,'general_templates/search.html',{"message":message})

     def aboretum_images(request):
    images=ImagePost.objects.filter(image_location__name="Aboretum")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)

def nature_images(request):
    images=ImagePost.objects.filter(image_location__name="Nature")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)



def park_images(request):
    images=ImagePost.objects.filter(image_location__name="National Park")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)

def beach_images(request):
    images=ImagePost.objects.filter(image_location__name="beach")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)

def cgi_images(request):
    images=ImagePost.objects.filter(image_location__name="CGI")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)


def unknown_images(request):
    images=ImagePost.objects.filter(image_location__name="Unknown")

    context = {
        "posts":images
    }
    return render(request, 'general_templates/display.html', context)   