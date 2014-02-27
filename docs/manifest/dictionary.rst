==========
Dictionary
==========


Facilities
----------
Each facility is a networked entity, related to at least one other entity by its position in the distribution
network. Each facility has an inventory, cold chain units, geo-coordinates, affiliated users, an administrator,
inventory rules, a unique code, a calendar and log of reports, and the option to add fleet units and other
modules as necessary. A facility can be both a parent and, or a child facility. Relations among facilities are
only described in parent-child terms, even if the sending facility is on its same level of the network, and/or
two or more steps above it.

**# PARENT** | A facility supplying another facility in the network.

**# CHILD** | A facility receiving supplies from another facility in the network.

**# BACKUP** | A facility linked to a child facility’s primary parent to serve as it as a backup parent facility when
the parent facility is unable to fulfill orders.

**# KEEPER** | A facility linked to another facility to serve as its backup/off-site storage when the CCUs are
down or over capacity.


Cold Chain
----------
The cold chain refers to the temperature-controlled supply chain for vaccines and other temperature-
sensitive products, which can also include biologics, food, and speciality materials. Most vaccines must
maintain 2-8°C from the point of their manufacture to the point of delivery. All vaccines are sensitive to
prolonged heat exposure above 8°C. To address this the vaccine vial monitor (VVM) is a small patch attached
to most vaccine vials in developing countries that shows users how must exposure the vial has experienced.
Some vaccines may be frozen (e.g., oral polio vaccine and lyophilized measles vaccine) but others are
inactivated when frozen (e.g., tetanus toxoid and pentavalent). There is no indicator for freeze damage. The
cold chain consists of special-purpose refrigerators and freezers situated at cold stores and health facilities.
Insulated containers packed with coolant (e.g., ice) enable transport between facilities and various forms of
outreach into the community.

Each facility in the network is linked to specific cold chain units (CCU), i.e., freezers, refrigerators, and walk-in
cold rooms, with the option to add passive cold boxes and carriers. Each CCU is registered in the system
with its make and model, power source, year of install, and a unique code that associates it with the facility
code. The system facilitates the routine monitoring of volume capacity, temperature performance, and
maintenance and repair of each CCU.


Inventory
---------
Inventories refer to the goods at a particular facility or network of facilities. The inventory is organized by a
hierarchy.

**# STOCK** | The generic, individual components of a facility’s inventory. Items of stock have a particular
product category.

**# PRODUCT CATEGORY** | One of a series of broad categories of products, like Cold Store Vaccines, Cold
Store Diluents, Cold Store Medicines, Cold Store Other, Dry Store Syringes, Dry Store Safety Boxes, Dry
Store Medicines, Dry Store Other.

**# PRODUCT TYPE** | The specific products that comprise a category. For vaccines, generally organized by
antigen, i.e., BCG, OPV, Penta, etc. It is this level in the hierarchy that will present to the user for tasks like
stock counts and in the inventory dashboard.

**# PRODUCT PROFILE** | A stored collection of details about a specific product type, concerning its
manufacturer, country of origin, volume, doses, presentation, formulation and administration, safety, storage
and handling requirements, necessary affiliated products, and other general details about the product. When
a new product type is added manually by the stock manager.

**# BATCH** | The specific instances of a product profile, identified by a batch number either borrowed from the
manufacturer or generated when the batch first enters the system. The batch includes the date of expiration,
unit price, and other specific details not encompassed in the product profile.

**# STOCK LIST** | The product profiles defined as necessary/requisite for a specific facility to keep in stock.
The quantities are defined by the Inventory Rules.

**# STOCK REPORT** | The report required at a predetermined interval (i.e. daily, monthly, quarterly) at each
facility that logs a manual count of actual stock and wastage. Reports can enter the system either by direct
keying into a mobile device or laptop or transcribed from written records.


Transactions
------------
Transactions are of specific batches or bundles of batches between facilities in the network and are classified
as either incoming or outgoing.

**# INCOMING** | The user will enter the incoming order or batch numbers either manually or by QR scan. The
data encoded in this number will include the quantity and expiry of each distinct product profile, its origin and
shipment details. These incoming data are reflected in the receiving (child) facility’s inventory.

**# OUTGOING** | The outgoing shipment is given an Order Number that includes quantity of the batch
numbers for the items in the shipment, which link the shipment to the products expiry, origin, and product
profile information. The user selects the mode by which stock leaves the inventory [Shipped, Expired,
Exposed, Broken, Delivered, Returned] and for what purpose (RI, SIA). These outgoing data are reflected in
the fulfilling (parent) facility’s inventory.

**# SUPPLEMENTAL IMMUNIZATION ACTIVITY (SIA)** | Special-purpose, ad hoc vaccination events, like
Immunization Plus Days (house-to-house IPD) and outbreak responses (e.g., measles). Often antigen-
specific, or of limited scope.

**# ROUTINE IMMUNIZATION (RI)** | The ongoing availability, promotion, and administration of vaccines to
children (and pregnant women). It may include routine outreach from a facility into a community, but not
special-purpose SIAs.

**# ORDER FORM** | The official manifest specifying which child facility is requesting which stock items in
which quantities from which parent facility, along with the date/time of order placement. The contents of the
Order Form is coupled with an Order Number.

**# ORDER NUMBER** | Each Order Form has an Order Number, a standardized, unique code referencing
the state, LGA, year, facility code, and sequential number.

**# ORDER REQUEST FORM** | An Order Form originating from a parent facility on behalf of a child facility,
submitted to a child facility for review and authorization.

**# BUNDLE** | The collection of whole or partial batches that together constitute the contents of a discrete
transfer between two distinct facilities per the authorized terms of an Order Form. Bundles can flow up and
down through the network (down, parent shipping stock to a child; up, child returning stock to a parent). It
serves as the tracking and transport manifest that is recorded (scanned or manually entered) in the system
upon arrival at a child (receiving) facility or upon pick-up from a parent facility. It is the entering of the Bundle
Number at arrival that initiates the Bundle Receipt.

**# BUNDLE NUMBER** | The unique numbers assigned to each bundle, encoded in a standardized
format linking the bundle to the facility of origin and the specific contents (by batch) of the bundle. It
enters the system by either scan of a pre-printed QR code or manual entry.

**# BUNDLE RECEIPT** | The form the authorized user at the child (receiving) facility reviews and executes
to verify the bundle delivered matches the bundle manifest. Entering the Bundle Number into the system
(via SMS, type, QR scan) initializes the Bundle Receipt. The Receipt is populated with the quantity of
stock items packed at the parent facility. The user verifies the accuracy, or adjusts the quantities
accordingly, assigns each line-item to a CCU, and submits the form. Submitting the form updates the
child (receiving) facility inventory and closes the transaction in the log.

**# QUICK-RESPONSE CODE (QR)** | A type of two-dimensional barcode selected for use with this system for
its fast readability with a wide-range of devices and high storage capacity.

**# TRACK-COUNT DISCREPANCY** | The difference between the stock levels the system reports by virtually
tracking a facility’s incoming and outgoing transactions and the results of the user-submitted, manually
counted Stock Reports.


Inventory Rules
---------------
The inefficiencies of having too much stock at any one facility can mean inadequate supplies in another
(opportunity cost), or if expired before consumption, can be highly costly. Too-low of inventories at a given
facilities can have compound effects downstream, driving missed opportunities for vaccination.
The system helps automate the management and optimization of inventory levels, which is essential for
ensuring inventories are balanced according to need across the network. The system monitors fluctuations in
inventory levels, a product of facility consumption (demand plus wastage) and incoming schedules, and uses
them as inputs in calculations to determine the rules governing that inventory and the workflows initiating
from changes in inventory. In the absence of such data, or appropriate forecast modeling, the rules can be
manually set and adjusted. The system provides the option for administrators to adjust these values and
assumptions (e.g., Service Level) and generate, incorporate additional modeling variables, e.g., Order Cycle,
Forecast-to-Mean Variance.

**# LEAD-TIME (LT)** | The duration between the time an order is authorized and the time the bundle arrives at
the facility, measured in days. The system calculates and updates average and variance in Lead-Time per
receiving facility with each bundle arrival. (Arrival Date/time - Order Date/time).

**# CONSUMPTION** | The amount of its inventory a facility consumes per the forecasting interval. This
includes fulfilling demand (shipment to child facilities and/or delivery + wastage), measured daily. The system
calculates and updates average and variance in consumption per program (RI, SIA) per facility.

**# LEAD-TIME CONSUMPTION (LTC)** | The average consumption during the lead-time period.
LTC = (Average Consumption * Average Lead Time)

**# SERVICE FACTOR (SF)** | The desired level (availability) of facility service expressed as a percentage.
Taking the inverse of the cumulative standard normal distribution of the desired service level, provides the
service factor. SF = (NORMSINV(Service_Level))
**# BUFFER STOCK** | The minimum level of each product profile a facility must maintain on site at all times
given its supply access, consumption patterns, and desired service level.
BUFFER = (SF)*SQRT(Average_LT*STDEVPA(Consumption)^2+Average_Consumption^2*STDEVPA(LT)^2)

**# REORDER POINT** | The inventory level for each item in a facility stock list at which a refill of supplies must
be ordered. ROP = BUFFER + STC

**# FULL** | The level at which a facility is at capacity for a particular item in its stock list. Organized by product
profile. Based on a facility’s available cold chain capacity and average consumption rate.


User Profiles
-------------

{Context for capabilities and expectations per level of the network}