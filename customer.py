import pymysql 

class customerList:
    def __init__(self): #self is an arguement that every class needs for all method definitions
        self.data = [] # a bunch of customers, using a list of dictionaries won't tie variable name to field name, allows for more than one customer to be stored as its own dictionary
        self.tempdata = {}
        self.tn = 'mailhotd_customers'
        self.fnl = ['fname','lname','email','password','subscribed'] #need a function to validate the differences in each fieldname
        self.errorlist = []
    def connect(self):
        import config
        return pymysql.connect(host=config.DB['host'], port=config.DB['port'], user=config.DB['user'], passwd=config.DB['passwd'], db=config.DB['db'], autocommit=True)
    def add(self): #Good to have class def without inputs so that it can be tested
        self.data.append(self.tempdata)
    def set(self,fn,val):
        if fn in self.fnl:
            self.tempdata[fn] = val #setting field name equal to value via setter method, controlling types where fn is a str and val is a str
        else:
            print('Invalid field: ' + str(fn))
            #Old Notes: Adding is doing two things setting each fn with a value, adding to overall data structure. Could be saved to a DB later. 
    
    def update(self,n,fn,val):
        if len(self.data) >= (n + 1) and fn in self.fnl:
            self.data[n][fn] = val # instead of modifying property directly in UT, it's done here and then put into the update method
        #data table is stored in data, as list of dictionaries, in class def
        else:
            print('Could not set value at row ' + str(n) + ' col ' + str(fn))
    def insert(self, n = 0): # make an insert based on the 0th row of the query
    
        cols = '`,`'.join(self,fnl) #used \ because we want the quote to be literal, thus using backslash as escape character is necessary when we want control chars to be literal chars.
        
        cols = '`'+cols+'`'
    
        vals = ('%s, ' * len(self.fnl))[:-1]
        
        tokens = []
        
        #order of dictionary and its composition (values) can change so we use fnl for inserting into DB
        for fieldname in self.fnl:
            tokens.append(self.data[n][fieldname])
        
        #cur.execute("DROP TABLE IF EXISTS `mailhotd_customers`")
        
        sql = 'INSERT INTO `' + self.tn + '` (' +cols+ ') VALUES (' +vals+ ');'
        
        conn = self.connect()

        cur = conn.cursor(pymysql.cursors.DictCursor)
   
        print(sql)
        print(tokens)
    
        cur.execute(sql,tokens)
        
    def verifyNew(self, n = 0):  # return true or false, keep track of all attempts in it's own data structure (list)
        self.errorlist = []

        if len(self.data[n]['fname']) == 0:
            self.errorlist.append("First name cannot be blank") #no fields can be blank
            
        if len(self.data[n]['lname']) == 0:
            self.errorlist.append("Last name cannot be blank") #no fields can be blank
            
        if len(self.data[n]['email']) == 0:
            self.errorlist.append("Email cannot be blank") #no fields can be blank
        if '@' and '.' in self.data[n]['email']: #email address must contain . and @
            pass
        else:
            self.errorlist.append("Email address invalid, make sure you include '.' and '@'")
            
        if len(self.data[n]['password']) == 0:
            self.errorlist.append("Password cannot be blank") #no fields can be blank
        if len(self.data[n]['password']) < 5:
            self.errorlist.append("Password must be longer than 4 characters") #password must be longer than 4 characters
        if len(self.data[n]['subscribed']) == 0:
            self.errorlist.append("Subscription cannot be blank") #no fields can be blank
        elif self.data[n]['subscribed'] != 'True':
            if self.data[n]['subscribed'] != 'False':
                self.errorlist.append("Subscription must be True or False") #subscribed must be 'True' or 'False'

        if len(self.errorlist) > 0:
            return False
        else:
            return True