from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.

# rooms=[
#     {'id':1,'name':'lets learn python!'},  
#     {'id':2,'name':'lets learn java!'},
#     {'id':3,'name':'lets learn c++!'},
# ]
def home(request):
    rooms=Room.objects.all()  # the above list will get ovveridded if we this thing
    context={'rooms':rooms}
    return render(request,'base/home.html',context)
    # return render(request,'home.html',{'rooms':rooms})
def room(request,pk):  #The id field is usually an automatically generated primary key field provided by Django.
    # for i in rooms:
    #     if i['id']==int(pk):
    #         room=i
    # context={'room':room}
    room=Room.objects.get(id=pk) #queryset
    context={'room':room}
    return render(request,'base/room.html',context)
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        # request.POST.get('name')
    

    context={'form':form}
    return render(request,'base/room_form.html',context)
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
