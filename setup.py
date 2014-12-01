from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Products', 'IMSSSMembers', 'version.txt')).read().strip()
if version.endswith('dev'):
    version = version[:-3]

setup(name='Products.IMSSSMembers',
      version=version,
      description="Adds fields to FacultyStaffDirectory's Person objects for IMSSS members",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope facultystaffdirectory imsss',
      author='T. Kim Nguyen',
      author_email='tkn@alumni.uwaterloo.ca',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'Products.FacultyStaffDirectory'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
