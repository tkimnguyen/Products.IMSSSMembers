from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.FacultyStaffDirectory.extenderInstallation import installExtenderGloballyIfLocallyIsNotSupported
from Products.GenericSetup import EXTENSION, profile_registry

from Products.IMSSSMembers.person import PersonExtender

installExtenderGloballyIfLocallyIsNotSupported(PersonExtender, 'Products.IMSSSMembers')  # Put the name of your product here.

registerDirectory('skins', globals())

def initialize(context):
    profile_registry.registerProfile(
        "default",
        "IMSSSMembers",
        "Adds IMSSS fields to Faculty/Staff Directory's Person type.",
        "profiles/default",
        product="Products.IMSSSMembers",
        profile_type=EXTENSION,
        for_=IPloneSiteRoot)
    profile_registry.registerProfile(
        "uninstall",
        "IMSSSMembers Uninstall",
        "Removes IMSSS fields from the Person type.",
        "profiles/uninstall",
        product="Products.IMSSSMembers",
        profile_type=EXTENSION,
        for_=IPloneSiteRoot)
