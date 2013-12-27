Vocabulary
------------

VVMStatus
    This is used to indicate Vaccine Vial Monitor for a vaccine. it has stages e.f Stage 1, Stage 2 etc

UOMCategory
    This is simply Unit of Measurement Category used to group units of measurement, it can be weight, volume, units etc.

UnitOfMeasurement
    This represents units of measuring items, it can be KiloGram, Celsius, Doses etc

Manufacturer
    Manufacturer refers to a product supplier, they are external firms, there is a list of products each manufacturer
    can supply.

Company
    Company is a concrete base class for entities such as Facility, it is used to model entities such as Partners.

CompanyCategory
    This is used to group company's that are related, it can be Facility, Partner, FacilityOperator

Party
    This is the abstract base class of Employee, Manufacturer and Company. A party is defined by: a name, a code,
    contact and address.

EmployeeCategory
    EmployeeCategory is used to model different categories of employees, it can be Driver, CCO, Store Manager.
    it is modelled hierarchically, it has properties such as:
        -name : name of the category, this is unique and required.
        -parent: parent category of this category. this is optional.

Employee
    Employee extends Party and an employee can also be an LMIS user if its linked to Django User object.
    Employee has the following attributes:
    - current company: The company field defines the current company of the user
    - main company: This defines which current company a user can choose: either the main company itself
            or one of the children companies.

FacilityType
    Facility Type is used to represent different types of facilities available in a country.
    it is modelled hierarchically. it can be a Health Facility or Store.

FacilityTypeApprovedProduct
    This is used to model products approved for each facility type.


Facility
    This is used to model stores, health facilities, Satellite store or any organisation that receives supplies and/or
    supplies other facilities.

WarehouseType
    This is used to represent different types of warehouse(storage locations), it can be 'Physical Warehouse' or
    'In-transit Warehouse'(used to model warehouse for items been transported from one facility to another e.g during
    delivery)

Warehouse
    Warehouse is used to define storage locations at a facility, a facility can have more than one warehouse.






