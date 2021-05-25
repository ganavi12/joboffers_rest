from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import JobOffer
from .serializers import JobOfferSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404 

# Create your views here.
class JobListCreateView(APIView):
    def get(self, request):
        joblists = JobOffer.objects.filter(available=True)
        serailizer = JobOfferSerializer(joblists, many=True)
        return Response(serailizer.data)
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class JobDetailView(APIView):
    def get_objects(self, pk):
        joblist = get_object_or_404(JobOffer, pk=pk)
        return joblist
    def get(self, request, pk):
        joblist = self.get_objects(pk)
        serializer = JobOfferSerializer(joblist)
        return Response(serializer.data)
    def put(self, request, pk):
        joblist = self.get_objects(pk)
        serializer = JobOfferSerializer(joblist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        joblist = self.get_objects(pk)
        joblist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)