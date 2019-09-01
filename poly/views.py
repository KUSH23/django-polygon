from django.contrib.gis.geos import LinearRing, Point, Polygon
from django.shortcuts import render, redirect
from django.contrib.gis.geos import GEOSGeometry
from polygen.models import PolyPoints
from .forms import PostForm

def home_page(request):
    form = PostForm()
    points = PolyPoints.objects.all()
    return render(request, "index.html", {'form': form})

def my_view(request):

    if request.method == 'POST':
        # print(request.POST.get('_lat'))

        form = PostForm(request.POST)
        qq = False
        print(qq)
        print(form['_lat'].value())
        print(type(form.data['_long']))
        p1 = Point(float(form['_lat'].value()),float(form['_long'].value()))
        lr = Polygon(((25.774,-81.190), ( 18.466, -66.118), (32.321, -64.757), (25.774, -81.190)))
        qq = p1.within(lr)
        print(qq)
    return render(request, "result.html",{'qq':qq})