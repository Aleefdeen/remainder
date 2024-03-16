import json
from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import RemainderDetails
from .serializers import RemainderDetailsSerializer

# Create your views here.
class RemainderDetailsViewSet(ModelViewSet):
    queryset = RemainderDetails.objects.all()
    serializer_class = RemainderDetailsSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = self.get_serializer(data=request.data, partial=True)
            if data.is_valid():
                data.save()
                return Response(
                    {"message": "Data successfully created"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"message": data.errors}, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)

    def list(self, request, *args, **kwargs):
       
        details = RemainderDetails.objects.all()
        serializer = self.get_serializer(details, many=True)
        return Response(
            {"message": "Details retrieved successfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
    def retrieve(self, request, *args, **kwargs):
        try:
            data = RemainderDetails.objects.get(id=self.kwargs["pk"])
            serializer = RemainderDetailsSerializer(data)
            return Response(
                {
                    "message": "Job details retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except RemainderDetails.DoesNotExist:
            return Response(
                {"message": "Details do not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        try:
            data = RemainderDetails.objects.get(id=self.kwargs["pk"])
            update_serializer = self.get_serializer(
                data, data=request.data, partial=True
            )
            if update_serializer.is_valid():
                update_serializer.save()
                return Response(
                    {"message": "Details updated successfully"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": update_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except RemainderDetails.DoesNotExist:
            return Response(
                {"message": "Details do not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
    
        try:
            RemainderDetails.objects.get(id=self.kwargs["pk"]).delete()
            return Response(
                {"message": "Details deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except RemainderDetails.DoesNotExist:
            return Response(
                {"message": "Details do not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )


