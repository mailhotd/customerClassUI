from customer import customerList

cl = customerList() #instance of a customerList class

cl.set('fname','Testguy')
cl.set('lname','Test')
cl.set('lastname','Test')
cl.set('email','a@a.com')
cl.set('password','12345')
cl.set('subscribed','True')
cl.add()

cl.update(0,'email','b@b.com')

print(cl.data[0])
#cl.delete()
print(cl.data)
#cl.deleteByID(cl.data[0]['id'])
cl.insert()

'''
# d = {'fname':'Testguy','lname':'test','email':'a@a.com','password':'123','subscribed':'1'}

# cl.add(d) #could call add on an integer even and add it to the list, check to make sure it's a dictionary and that item in customer.py has data in it with right structure (dict) make sure names of keys match in all files. 

cl.set('fname','Testguy')
cl.set('lname','Test')
cl.set('lastname','Test')
cl.set('email','a@a.com')
cl.set('password','12345')
cl.set('subscribed','True')
cl.add()
# cl.add()

print(cl.data) #.data contains all of the dictionaries (entire)
print(cl.data[0]) #.data contains all of the dictionaries (0)

cl.update(0,'email','b@b.com')
# cl.update(0,'e_mail','b@b.com')

print(cl.data) #.data contains all of the dictionaries (instance of email)

cl.insert()
'''