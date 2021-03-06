"""
    core/views.py holds the API end-point for core models. it is used to define the API views from which external
    clients can interact with the models to perform operations such as Create, Retrieve, Update, Delete etc via
    ModelViewSet functions such as list(), retrieve(), update(), partial_update(), destroy() and ad-hoc functions can
    be added too.
"""

#import from django core modules
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import viewsets, status, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company, Rate,
                         Contact, Address, EmployeeCategory, Employee, ProductPresentation, ModeOfAdministration,
                         ProductItem, Currency, ProductFormulation)

from .serializers import (ProductSerializer, ProductCategorySerializer, UnitOfMeasurementSerializer,
                          UOMCategorySerializer, CompanyCategorySerializer, CompanySerializer, CurrencySerializer,
                          RateSerializer, ContactSerializer, AddressSerializer, EmployeeCategorySerializer,
                          EmployeeSerializer, UserSerializer, PermissionSerializer, ProductPresentationSerializer,
                          ModeOfAdministrationSerializer, ProductItemSerializer, ProductFormulationSerializer)

from facilities.api.serializers import FacilitySerializer
from facilities.models import Facility


class BaseModelViewSet(viewsets.ModelViewSet):
    """
        Base API end-point for other model view sets end-point.

        permission_class:
            IsAuthenticated : ensures that only authenticated users can access the API
    """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('is_deleted',)
    #TODO: activate permission on APIView; permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'

    def pre_save(self, obj):
        """
            This is over-ridden to attach user that created or modified an object to it before the object is saved.

            i did this here cause the model doesn't have access to request object
        """
        if Employee.get_user_or_none(self.request.user.id):
            if obj.uuid is None:
                obj.created_by = self.request.user
            obj.modified_by = self.request.user

    def update_obj_is_deleted(self, is_deleted):
        """
            updates given object is_deleted field
        """
        obj = self.get_object(self.get_queryset())
        obj.is_deleted = is_deleted
        self.pre_save(obj)
        obj.save()

    def get_view_model_class(self):
        """
            return the class of the model attribute of the ViewSet Serializer class e.g for ProductViewSet, it returns
            Product which is the model specified on ProductSerializer model attribute
        """
        return self.serializer_class.Meta.model

    def destroy(self, request, uuid):
        """
            This over-rides ModelViewSet.destroy() so that objects are not deleted (hard deleted) but it just turns the
            "is_deleted" flag on models to
        """
        obj = self.get_object(self.get_queryset())
        if obj:
            self.update_obj_is_deleted(is_deleted=True)
            return Response(data={'success': True})
        return Response(data={'detail': 'not found'})

    @action(methods=['POST', 'DELETE'])
    def recover(self, request, uuid):
        """
            This ad-hoc functions turns off is_deleted flag of object it is called on. this redo soft delete on the
            object. it can only be accessed via POST and DELETE methods
        """
        obj = self.get_object(self.get_queryset())
        if obj:
            self.update_obj_is_deleted(is_deleted=False)
            return Response(data={'success': True})
        return Response(data={'detail': 'not found'})


class ProductViewSet(BaseModelViewSet):
    """
        API end-point for product model
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(BaseModelViewSet):
    """
        API end point for product category
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class UnitOfMeasurementViewSet(BaseModelViewSet):
    """
       API end point for Unit of Measurement
    """
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer


class UOMCategoryViewSet(BaseModelViewSet):
    """
        API end point for unit of measurement category
    """
    queryset = UOMCategory.objects.all()
    serializer_class = UOMCategorySerializer


class CompanyCategoryViewSet(BaseModelViewSet):
    """
        API end point for Company Category
    """
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyViewSet(BaseModelViewSet):
    """
        API end point for Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CurrencyViewSet(BaseModelViewSet):
    """
        API end point for Currency model
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class RateViewSet(BaseModelViewSet):
    """
        API end-point for Rate model
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class ContactViewSet(BaseModelViewSet):
    """
        API end-point for Contact model
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressViewSet(BaseModelViewSet):
    """
        API end point for Address Model
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EmployeeCategoryViewSet(BaseModelViewSet):
    """
        API end point for EmployeeCategory model
    """
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer


class EmployeeViewSet(BaseModelViewSet):
    """
        API end point for Employee model
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserFacilityView(views.APIView):
    """
        API end-point that returns logged in user facility if any
    """
    def get(self, request, format=None):
        serializer = FacilitySerializer(Employee.get_user_facility_or_none(request.user))
        return Response(serializer.data, status=status.HTTP_200_OK, template_name=None, headers=None, content_type=None)


class UserViewSet(viewsets.ModelViewSet):
    """
        API end point User model, required by EmployeeViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
        API end-point for Permission model required by UserViewSet since User model references Permission
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class ProductPresentationViewSet(BaseModelViewSet):
    """
        API end-point for ProductPresentation model
    """
    queryset = ProductPresentation.objects.all()
    serializer_class = ProductPresentationSerializer


class ModeOfAdministrationViewSet(BaseModelViewSet):
    """
        API end-point for ModeOfAdministration model
    """
    queryset = ModeOfAdministration.objects.all()
    serializer_class = ModeOfAdministrationSerializer


class ProductItemViewSet(BaseModelViewSet):
    """
        API end-point for ProductItem model
    """
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class ProductFormulationViewSet(BaseModelViewSet):
    """
        API end point for Product Formulation
    """
    queryset = ProductFormulation.objects.all()
    serializer_class = ProductFormulationSerializer
