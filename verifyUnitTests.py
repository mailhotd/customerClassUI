from customer import customerList
cl = customerList() #instance of a customerList class
#d = {'fname':'first','lname':'last','email':'email@email.com','password':'password','subscribed':'1',}
#cl.add(d)
#print(cl.data)
cl.set('fname','test')
cl.set('lname','test')
cl.set('email','email@email.com')
cl.set('password','12345')
cl.set('subscribed','True')

cl.add()
cl.verifyNew()
print(cl.errorlist)