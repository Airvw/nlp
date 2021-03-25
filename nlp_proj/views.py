from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from .models import Hotel
from .models import UploadFile
from .forms import UplaodFileForm

def index(request):
    review_all = Hotel.objects.all()  # .get(), .filter(), ...
    # request가 POST -> Form을 완성.
    # Form이 유효하면 저장.\
    # if request.method == "POST":
    #     form = CoffeeForm(request.POST)  # 완성된 Form
    #     if form.is_valid():  # 채워진 Form이 유효하다면
    #         form.save()  # Form을 Model에 저장

    # form = CoffeeForm()
    return render(request, 'index.html', {"review_list": review_all})

def upload_view(request):
    file_all = UploadFile.objects.all()
    if request.method == "POST":
        form = UplaodFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(upload_view)
    else:
        form = UplaodFileForm()
    return render(request, 'upload.html', {"file_list" : file_all, "uploadform" : form})


