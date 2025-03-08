from django.shortcuts import redirect, render
from .models import VisionBoard
from .forms import VisionForm


# Create your views here.
def CreatingVision(request):
    if request.method == 'POST':
        form = VisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('visions.html')
    else:
         form = VisionForm()  #create an empty form for GET request   
    return render (request, 'visionboard.html', {'form': form})


def Visions(request):
    visions = VisionBoard.objects.filter(is_in_trash= False)
    return render( request, 'visions.html', { 'visions': visions})

    
