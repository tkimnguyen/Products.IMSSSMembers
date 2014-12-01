from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.Archetypes.atapi import *
from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter

from Products.FacultyStaffDirectory.interfaces.person import IPerson


# Any field you tack on must have ExtensionField as its first subclass:

class _StringExtensionField(ExtensionField, StringField):
    pass

class _FileExtensionField(ExtensionField, FileField):
    pass

class _TextExtensionField(ExtensionField, TextField):
    pass

class _DateTimeExtensionField(ExtensionField, DateTimeField):
    pass

class _LinesExtensionField(ExtensionField, LinesField):
    pass

class _IntegerExtensionField(ExtensionField, IntegerField):
    pass

class _FloatExtensionField(ExtensionField, FloatField):
    pass

class _FixedPointExtensionField(ExtensionField, FixedPointField):
    pass

class _ReferenceExtensionField(ExtensionField, ReferenceField):
    pass

class _ComputedExtensionField(ExtensionField, ComputedField):
    pass

class _BooleanExtensionField(ExtensionField, BooleanField):
    pass

class _ImageExtensionField(ExtensionField, ImageField):
    pass

class _PhotoExtensionField(ExtensionField, PhotoField):
    pass


class PersonExtender(object):
    """Adapter that adds IMSSS-relevant fields to Person.
    
    You could also change or delete existing fields (though you might violate assumptions made in other code). To do that, implement ISchemaModifier instead of ISchemaExtender.

    LastName	FirstName	Address1	Address2	Address3	Address4	City	Zip	State	Country	NewMember	DatePaid	AmountPaid	DateOfPrevPayment	AmountOfPrevPayment	TypeOfMembership	FinalYearOfCurrentSubscription	EmailAddress	ResearchInterests	Comments
    """
    adapts(IPerson)
    implements(ISchemaExtender)
    
    _fields = [
        _TextExtensionField('address',
                required=False,
                searchable=True,
                schemata="IMSSS",
                default_content_type = 'text/plain',
                default_output_type = 'text/plain',
                allowable_content_types=('text/plain', ),
                widget=TextAreaWidget(
                    label=u"Address",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _StringExtensionField('city',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"City",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _StringExtensionField('postalCode',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"Postal Code",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _StringExtensionField('state',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"State",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _StringExtensionField('country',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"Country",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _IntegerExtensionField('firstMembershipYear',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=IntegerWidget(
                    label=u"Year of initial membership",
                    description=u"",
                    size=4,
                ),
                read_permission="View",
                write_permission="IMSSS: modify secure membership details",
            ),

        _DateTimeExtensionField('datePaid',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=CalendarWidget(
                    label=u"Date paid",
                    description=u"",
                    show_hm = False,
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),

        _FloatExtensionField('amountPaid',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=DecimalWidget(
                    label=u"Amount paid",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),

        _StringExtensionField('amountPaidCurrency',
                required=False,
                searchable=True,
                schemata="IMSSS",
                vocabulary=('USD','Euro',),
                widget=SelectionWidget(
                    label=u"Amount paid currency",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),

        _DateTimeExtensionField('dateOfPreviousPayment',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=CalendarWidget(
                    label=u"Date of previous payment",
                    description=u"",
                    show_hm = False,
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),

        _FloatExtensionField('amountOfPreviousPayment',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=DecimalWidget(
                    label=u"Amount of previous payment",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),
    
        _StringExtensionField('amountOfPreviousPaymentCurrency',
                required=False,
                searchable=True,
                schemata="IMSSS",
                vocabulary=('USD','Euro',),
                widget=SelectionWidget(
                    label=u"Amount of previous payment currency",
                    description=u"",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify secure membership details",
            ),

        _StringExtensionField('membershipType',
                required=False,
                searchable=True,
                schemata="IMSSS",
                vocabulary=('regular','student',),
                widget=SelectionWidget(
                    label=u"Type of membership",
                    description=u"",
                ),
                read_permission="View",
                write_permission="IMSSS: modify secure membership details",
            ),
        
        _IntegerExtensionField('finalYearOfCurrentSubscription',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=IntegerWidget(
                    label=u"Final year of current subscription",
                    description=u"",
                    size=4,
                ),
                read_permission="View",
                write_permission="IMSSS: modify secure membership details",
            ),
        
        _StringExtensionField('emailAddress2',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"Additional email address 1",
                    description=u"optional",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),

        _StringExtensionField('emailAddress3',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"Additional email address 2",
                    description=u"optional",
                ),
                read_permission="IMSSS: view membership details",
                write_permission="IMSSS: modify membership details",
            ),
        
        _TextExtensionField('researchInterests',
                required=False,
                searchable=True,
                schemata="IMSSS",
                default_content_type = 'text/plain',
                default_output_type = 'text/plain',
                allowable_content_types=('text/plain', ),
                widget=TextAreaWidget(
                    label=u"Research interests",
                    description=u"",
                ),
                read_permission="View",
                write_permission="IMSSS: modify membership details",
            ),
        
        _StringExtensionField('institution',
                required=False,
                searchable=True,
                schemata="IMSSS",
                widget=StringWidget(
                    label=u"Institution",
                    description=u"",
                    size=50,
                ),
                read_permission="View",
                write_permission="IMSSS: modify membership details",
            ),
        
        _TextExtensionField('comments',
                required=False,
                searchable=True,
                schemata="IMSSS",
                default_content_type = 'text/plain',
                default_output_type = 'text/plain',
                allowable_content_types=('text/plain', ),
                widget=TextAreaWidget(
                    label=u"Comments",
                    description=u"viewable and editable only by IMSSS membership manager",
                ),
                read_permission="IMSSS: view secure membership details",
                write_permission="IMSSS: modify secure membership details",
            ),
        
        ]
    
    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self._fields


# # Optional stuff to tack on more methods to Person (after you adapt it to IYuppie, anyway):
# 
# class IYuppie(Interface):
#     """A Yuppie is any person who eats tofu and has a mobile phone."""
#     
#     def textMessage(self, spam):
#         """Text message some spam to the yuppie's mobile phone."""
# 
# 
# class YuppieAdapter(object):
#     """Adapt Persons to Yuppies."""
#     adapts(IPerson)
#     implements(IYuppie)
#     
#     def __init__(self, context):
#         self.context = context  # Phillip Weitershausen says this is canonical.
#     
#     def textMessage(self, spam):
#         print "I just texted %s to the yuppie's mobile phone at %s!" % (spam, self.context.getMobilePhone())
# 
# provideAdapter(YuppieAdapter)  # This should be in ZCML. Yuck.
