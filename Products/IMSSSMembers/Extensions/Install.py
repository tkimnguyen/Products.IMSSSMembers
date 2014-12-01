from Products.CMFCore.utils import getToolByName
from Products.FacultyStaffDirectory.extenderInstallation import localAdaptersAreSupported, installExtender, uninstallExtender
from Products.IMSSSMembers.person import PersonExtender
from Products.CMFCore.permissions import setDefaultRoles

_adapterName = 'IMSSSMembers'

def _runProfile(profile, portal):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profile)

def install(portal):
    if localAdaptersAreSupported:
        installExtender(portal, PersonExtender, _adapterName)
    setDefaultRoles('IMSSS: view membership details', ())
    setDefaultRoles('IMSSS: modify membership details', ())
    setDefaultRoles('IMSSS: view secure membership details', ())
    setDefaultRoles('IMSSS: modify secure membership details', ())
    _runProfile('profile-Products.IMSSSMembers:default', portal)

def uninstall(portal):
    if localAdaptersAreSupported:
        uninstallExtender(portal, PersonExtender, _adapterName)
    _runProfile('profile-Products.IMSSSMembers:uninstall', portal)
