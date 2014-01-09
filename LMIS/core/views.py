"""
    core/views.py holds the API end-point for core models. it is used to define the API views from which external
    clients can interact with the models to perform operations such as Create, Retrieve, Update, Delete etc via
    ModelViewSet functions such as list(), retrieve(), update(), partial_update(), destroy() and ad-hoc functions can
    be added too.
"""

#import from django core modules
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import viewsets, status
from rest_framework.response import Response

#import project modules
from .models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company, Rate, Contact,
                     Address, EmployeeCategory, Employee, FacilityType, Facility, Program, ProgramProduct,
                     FacilitySupportedProgram, ProgramProductAllocationInfo, FacilitySupportedProgramProduct,
                     SupervisoryNode, OrderGroup, ProductPresentation, ModeOfAdministration, WarehouseType, Warehouse,
                     ProductItem
                     )

from .api.serializers import (ProductSerializer, ProductCategorySerializer, UnitOfMeasurementSerializer,
                              UOMCategorySerializer, CompanyCategorySerializer, CompanySerializer, CurrencySerializer,
                              RateSerializer, ContactSerializer, AddressSerializer, EmployeeCategorySerializer,
                              EmployeeSerializer, UserSerializer, PermissionSerializer, FacilityTypeSerializer,
                              FacilitySerializer, ProgramSerializer, ProgramProductSerializer,
                              FacilitySupportedProgramSerializer, ProgramProductAllocationInfoSerializer,
                              FacilitySupportedProgramProductSerializer, SupervisoryNodeSerializer,
                              OrderGroupSerializer, ProductPresentationSerializer, ModeOfAdministrationSerializer,
                              WarehouseTypeSerializer, WarehouseSerializer, ProductItemSerializer
                              )


#TODO: add view function that returns only deleted models and make normal query set to return only models not yet
#TODO: deleted
#TODO: over-ride ModelViewSet.destroy() to just turn on model is_deleted flag on(soft delete)
class BaseModelViewSet(viewsets.ModelViewSet):
    """
        Base API end-point for other model view sets end-point.
    """
    def pre_save(self, obj):
        """
            This is over-ridden to attach user that created or modified an object to it before the object is saved.
        """
        if obj.uuid is None:
            obj.created_by = self.request.user
        obj.modified_by = self.request.user

    def pre_delete(self, obj):
        print("pre delete called")
        obj.is_deleted = True
        self.pre_save(obj)
        obj.save()

    def destroy(self, request, pk):
        """

        """
        return Response(data={'success': True})


class ProductViewSet(BaseModelViewSet):
    """
        API end-point that allows list of all products to be view
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

    def destroy(self, request, pk):
        """

        """
        try:
            uom_category = UOMCategory.objects.get(uuid=pk)
        except UOMCategory.DoesNotExist:
            uom_category = None
        if uom_category:
            uom_category.is_deleted = True
            serializer = UOMCategorySerializer(uom_category)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'Unknown': 'no matching object found'})
        # serializer = request.DATA
        # if serializer.is_valid():
        #
        # return Response(data={'success': True})


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
    queryset = Company.objects.all()
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


class FacilityTypeViewSet(BaseModelViewSet):
    """
        API end-point for FacilityType model.
    """
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class FacilityViewSet(BaseModelViewSet):
    """
        API end-point for Facility model
    """
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class ProgramViewSet(BaseModelViewSet):
    """
        API end-point for Program model
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramProductViewSet(BaseModelViewSet):
    """
        API end-point for ProgramProduct model
    """
    queryset = ProgramProduct.objects.all()
    serializer_class = ProgramProductSerializer


class FacilitySupportedProgramViewSet(BaseModelViewSet):
    """
        API end-point for FacilitySupportedProgram model
    """
    queryset = FacilitySupportedProgram.objects.all()
    serializer_class = FacilitySupportedProgramSerializer


class ProgramProductAllocationInfoViewSet(BaseModelViewSet):
    """
        API end-point for ProgramProductAllocationInfo model
    """
    queryset = ProgramProductAllocationInfo.objects.all()
    serializer_class = ProgramProductAllocationInfoSerializer


class FacilitySupportedProgramProductViewSet(BaseModelViewSet):
    """
        API end-point for FacilitySupportedProgramProduct model
    """
    queryset = FacilitySupportedProgramProduct.objects.all()
    serializer_class = FacilitySupportedProgramProductSerializer


class SupervisoryNodeViewSet(BaseModelViewSet):
    """
        API end-point for SupervisoryNode model
    """
    queryset = SupervisoryNode.objects.all()
    serializer_class = SupervisoryNodeSerializer


class OrderGroupViewSet(BaseModelViewSet):
    """
        API end-point for OrderGroup model
    """
    queryset = OrderGroup.objects.all()
    serializer_class = OrderGroupSerializer


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


class WarehouseTypeViewSet(BaseModelViewSet):
    """
        API end-point for WarehouseType model
    """
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer


class WarehouseViewSet(BaseModelViewSet):
    """
        API end-point for Warehouse model
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductItemViewSet(BaseModelViewSet):
    """
        API end-point for ProductItem model
    """
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
