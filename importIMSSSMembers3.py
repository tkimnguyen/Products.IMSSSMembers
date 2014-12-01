fileName = "cleanedupdata201110021917.tsv"

def importCommitteeMembers(self):
    file = open(fileName, "r")
    mincols = 100
    keep_going = True
    while keep_going:
        row = file.readline()
        if not row:
            keep_going = False
            continue
        row = row.strip()
        cols = row.split("\t")
        numcols = len(cols)
#         if numcols < mincols:
#             mincols = numcols

        if numcols == 24:
            #import pdb;pdb.set_trace()
            LastName, FirstName, Address1, Address2, Address3, Address4, City, Zip, State, Country, NewMember, DatePaid, AmountPaid, DateOfPrevPayment, AmountOfPrevPayment, TypeOfMembership, FinalYearOfCurrentSubscription, EmailAddress, ResearchInterests, Comments, EmailAddress2, Currency, DatePaidDate, DateOfPrevPaymentDate = cols
        else:
            if numcols == 23:
                LastName, FirstName, Address1, Address2, Address3, Address4, City, Zip, State, Country, NewMember, DatePaid, AmountPaid, DateOfPrevPayment, AmountOfPrevPayment, TypeOfMembership, FinalYearOfCurrentSubscription, EmailAddress, ResearchInterests, Comments, EmailAddress2, Currency, DatePaidDate = cols
                DateOfPrevPaymentDate = ''
            else:
                if numcols == 22:
                    LastName, FirstName, Address1, Address2, Address3, Address4, City, Zip, State, Country, NewMember, DatePaid, AmountPaid, DateOfPrevPayment, AmountOfPrevPayment, TypeOfMembership, FinalYearOfCurrentSubscription, EmailAddress, ResearchInterests, Comments, EmailAddress2, Currency = cols
                    DateOfPrevPaymentDate = ''
                    DatePaidDate = ''
                else:
                    raise Exception
        if LastName <> 'Ferzoco' and LastName <> 'Stansbury' and LastName <> 'Rivers' and LastName <> 'Duclow':
            continue

        print ""
        print "----------------------------"
        print ""
        print numcols, ":", cols
        print ""
        print "numcols is %s" % numcols
        print ""
        print "LastName: %s" % LastName
        print "FirstName: %s" % FirstName
        print "Address1: %s" % Address1
        print "Address2: %s" % Address2
        print "Address3: %s" % Address3
        print "Address4: %s" % Address4
        print "City: %s" % City
        print "Zip: %s" % Zip
        print "State: %s" % State
        print "Country: %s" % Country
        print "NewMember: %s" % NewMember
        print "DatePaid: %s" % DatePaid
        print "AmountPaid: %s" % AmountPaid
        print "DateOfPrevPayment: %s" % DateOfPrevPayment
        print "AmountOfPrevPayment: %s" % AmountOfPrevPayment
        print "TypeOfMembership: %s" % TypeOfMembership
        print "FinalYearOfCurrentSubscription: %s" % FinalYearOfCurrentSubscription
        print "EmailAddress: %s" % EmailAddress
        print "ResearchInterests: %s" % ResearchInterests
        print "Comments: %s" % Comments
        print "EmailAddress2: %s" % EmailAddress2
        print "Currency: %s" % Currency
        print "DatePaidDate: %s" % DatePaidDate
        print "DateOfPrevPaymentDate: %s" % DateOfPrevPaymentDate

        id = "%s-%s" % (FirstName, LastName)
        id = id.replace(' ','-')
        id = id.replace('.','')
        id = id.lower()
        print "newpersonid = self.directory.invokeFactory('FSDPerson', id='%s')" % id
        print "newperson = self.directory[newpersonid]"
        print "schema = newperson.Schema()"
        print "newperson.setLastName('%s')" % LastName
        print "newperson.setFirstName('%s')" % FirstName

        print "address_field = schema.getField('address')"
        print "address_field.set(newperson, \"%s\\n%s\\n%s\\n%s\")" % (Address1, Address2, Address3, Address4)

        print "city_field = schema.getField('city')"
        print "city_field.set(newperson, '%s')" % City
        
        print "postalcode_field = schema.getField('postalCode')"
        print "postalcode_field.set(newperson, '%s')" % Zip
        
        print "state_field = schema.getField('state')"
        print "state_field.set(newperson, '%s')" % State
        
        print "country_field = schema.getField('country')"
        print "country_field.set(newperson, '%s')" % Country
        
        print "firstmembershipyear_field = schema.getField('firstMembershipYear')"
        print "firstmembershipyear_field.set(newperson, '%s')" % NewMember
        
        print "datepaid_field = schema.getField('datePaid')"
        print "datepaid_field.set(newperson, '%s')" % DatePaidDate
        
        print "amountpaid_field = schema.getField('amountPaid')"
        print "amountpaid_field.set(newperson, '%s')" % AmountPaid
        
        print "amountpaidcurrency_field = schema.getField('amountPaidCurrency')"
        print "amountpaidcurrency_field.set(newperson, '%s')" % Currency
        
        print "dateofpreviouspayment_field = schema.getField('dateOfPreviousPayment')"
        print "dateofpreviouspayment_field.set(newperson, '%s')" % DateOfPrevPaymentDate
        
        print "amountofpreviouspayment_field = schema.getField('amountOfPreviousPayment')"
        print "amountofpreviouspayment_field.set(newperson, '%s')" % AmountOfPrevPayment
        
        print "amountofpreviouspaymentcurrency_field = schema.getField('amountOfPreviousPaymentCurrency')"
        print "amountofpreviouspaymentcurrency_field.set(newperson, '%s')" % Currency
        
        print "membershiptype_field = schema.getField('membershipType')"
        print "membershiptype_field.set(newperson, '%s')" % TypeOfMembership
        
        print "finalyearofcurrentsubscription_field = schema.getField('finalYearOfCurrentSubscription')"
        print "finalyearofcurrentsubscription_field.set(newperson, '%s')" % FinalYearOfCurrentSubscription
        
        print "emailaddress2_field = schema.getField('emailAddress2')"
        print "emailaddress2_field.set(newperson, '%s')" % EmailAddress
        
        print "emailaddress3_field = schema.getField('emailAddress3')"
        print "emailaddress3_field.set(newperson, '%s')" % EmailAddress2
        
        print "researchinterests_field = schema.getField('researchInterests')"
        print "researchinterests_field.set(newperson, '%s')" % ResearchInterests
        
        print "comments_field = schema.getField('comments')"
        print "comments_field.set(newperson, '%s')" % Comments
        
        # we don't get an institution from the current MS Access database
        # print "newperson.setInstitution('%s')" % Institution

        print "newperson.setPassword('%s'[::-1])" % EmailAddress

        print "newperson.reindexObject()"

        print "return \"OK\""
        
#     print "mincols is ", mincols
            

if __name__ == "__main__":
    importCommitteeMembers(None)
