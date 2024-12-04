from django.shortcuts import render
from rest_framework.response import Response
from .models import Trip
from rest_framework.decorators import api_view
from .Serializer import TripSerializer


# Create your views here.
@api_view(['POST'])
def newtrip(request):
    data = request.data
    trip =Trip.objects.create(title = data['title'])
    return Response({'message': 'Trip created successfully',"id":trip.id})


@api_view(['POST'])
def home(request):
    data = request.data
    tripids = data.get('tripidlist')
    trips = TripSerializer(Trip.objects.filter(id__in=tripids), many=True) 
    return Response({'message': 'Trip created successfully', 'trips': trips.data})

@api_view(['POST'])
def trip(request):
    id = request.data["tripid"]
    trip = TripSerializer(Trip.objects.get(id=id))
    return Response(trip.data)
@api_view(['POST'])
def trip(request):
    id = request.data["tripid"]
    trip = TripSerializer(Trip.objects.get(id=id))
    return Response(trip.data)
@api_view(['POST'])
def newmember(request):
    id = request.data["tripid"]
    name = request.data["name"]
    trip = Trip.objects.get(id=id)
    if name.lower() in [x.lower() for x in trip.members]:
        return Response({'status': 'Member already exists in the trip'})
    trip.newmember(name)
    return Response({'status': 'success'})
@api_view(['POST'])
def newpayment(request):
    id = request.data["tripid"]
    shop = request.data["shop"]
    member = request.data["member"]
    amount = request.data["amount"]
    trip = Trip.objects.get(id=id)
    trip.newpayment(member,amount,shop)
    tripserial = TripSerializer(trip)
    return Response(tripserial.data)
@api_view(['POST'])
def removemember(request):
    id = request.data["tripid"]
    name = request.data["name"]
    trip = Trip.objects.get(id=id)
    trip.members.remove(name)
    trip.save()
    tripserial = TripSerializer(trip)
    return Response(tripserial.data)
@api_view(['POST'])
def removepayment(request):
    id = request.data["tripid"]
    payment = request.data["payment"]
    trip = Trip.objects.get(id=id)
    trip.payments.remove(payment)
    trip.save()
    tripserial = TripSerializer(trip)
    return Response(tripserial.data)
@api_view(['POST'])
def toggledue(request):
    id = request.data["tripid"]
    dueindex = request.data["dueindex"]
    toggle = request.data["toggle"]
    trip = Trip.objects.get(id=id)
    trip.dues[dueindex][3] = toggle
    trip.save()
    tripserial = TripSerializer(trip)
    return Response(tripserial.data)

@api_view(['POST'])
def deletetrip(request):
    id = request.data["tripid"]
    trip = Trip.objects.get(id=id)
    trip.delete()
    return Response({'status': 'success'})