from django.shortcuts import render

# Create your views here.

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