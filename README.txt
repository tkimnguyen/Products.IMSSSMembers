IMSSSMembers extends FacultyStaffDirectory for use by the IMSSS
(http://imsss.net) to manage its membership database.

To fix the office phone field so it no longer enforces the North
American format, go to /facultystaffdirectory_tool/view and change the
phone number format to blank.

This product creates new permissions:

    'IMSSS: view membership details'
    'IMSSS: modify membership details'
    'IMSSS: view secure membership details'
    'IMSSS: modify secure membership details'

and assigns them variously to these roles:

    Personnel Manager
    Manager
    Owner

The view template prevents the public from seeing most IMSSS fields,
non-owners and non-managers from seeing most IMSSS fields, owners from
seeing the Comments field, and allows Manager and Personnel Manager
roles to see all IMSSS fields.


Development Notes:
------------------


http://plone.org/documentation/kb/adding-a-custom-permission-to-a-plone-2-5-product

http://plone.org/products/populator-tool (TAL condition checking for roles)

http://plone.org/documentation/kb/hide-content-from-anonymous

http://plone.org/documentation/kb/the-format-of-multiple-rich-text-fields


IMSSS Database Fields
---------------------

These are the fields the IMSSS keeps in its MS Access database.

Column Name                       Type       Size    Primary Key    Foreign Key    Nullable    Scale
LastName                          VARCHAR    100                                   YES              
FirstName                         VARCHAR    100                                   YES              
Address1                          VARCHAR    510                                   YES              
Address2                          VARCHAR    100                                   YES              
Address3                          VARCHAR    100                                   YES              
Address4                          VARCHAR    100                                   YES              
City                              VARCHAR    510                                   YES              
Zip                               VARCHAR    510                                   YES              
State                             VARCHAR    510                                   YES              
Country                           VARCHAR    100                                   YES              
NewMember                         VARCHAR    100                                   YES              
DatePaid                          VARCHAR    100                                   YES              
AmountPaid                        VARCHAR    100                                   YES              
DateOfPrevPayment                 VARCHAR    100                                   YES              
AmountOfPrevPayment               VARCHAR    100                                   YES              
TypeOfMembership                  VARCHAR    100                                   YES              
FinalYearOfCurrentSubscription    VARCHAR    100                                   YES              
EmailAddress                      VARCHAR    160                                   YES              
ResearchInterests                 VARCHAR                                          YES              
Comments                          VARCHAR                                          YES              


CREATE TABLE "Subscription Information" (
     LastName VARCHAR(100),
     FirstName VARCHAR(100),
     Address1 VARCHAR(510),
     Address2 VARCHAR(100),
     Address3 VARCHAR(100),
     Address4 VARCHAR(100),
     City VARCHAR(510),
     Zip VARCHAR(510),
     State VARCHAR(510),
     Country VARCHAR(100),
     NewMember VARCHAR(100),
     DatePaid VARCHAR(100),
     AmountPaid VARCHAR(100),
     DateOfPrevPayment VARCHAR(100),
     AmountOfPrevPayment VARCHAR(100),
     TypeOfMembership VARCHAR(100),
     FinalYearOfCurrentSubscription VARCHAR(100),
     EmailAddress VARCHAR(160),
     ResearchInterests VARCHAR,
     Comments VARCHAR
);


