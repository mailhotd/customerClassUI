# customerClass
 
Create a method called verifyNew() for your customer class.  It should take a integer as an argument and return boolean.  The function should return True if all fields were validated successfully.  The function should set class property called errorList which is a list of strings.  The list of strings should be a list of error messages for each of the fields.  

no fields can be blank
email address must contain . and @
subscribed must be 'True' or 'False'
password must be longer than 4 characters
Include unit tests to test the logic above.

You should make a new branch called 'verifyNewAssignment' with your changes.



def verifyNew(self,n=0):
self.errorList = []

if len(self.data[n]['fname']) == 0:
self.errorList.append("First name cannot be blank.")

Add if statements for validation of other fields


if len(self.errorList) > 0:
return False
else:
return True