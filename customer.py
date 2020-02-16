import pymysql 

class customerList:
    def __init__(self): #self is an arguement that every class needs for all method definitions
        self.data = [] # a bunch of customers, using a list of dictionaries won't tie variable name to field name, allows for more than one customer to be stored as its own dictionary
        self.tempdata = {}
        self.tn = 'mailhotd_customers'
        self.fnl = ['fname','lname','email','password','subscribed'] #need a function to validate the differences in each fieldname
        self.errorlist = []
        self.conn = None
        self.pk = 'id'
    def connect(self):
        import config
        self.conn = pymysql.connect(host=config.DB['host'], port=config.DB['port'], user=config.DB['user'], passwd=config.DB['passwd'], db=config.DB['db'], autocommit=True)
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
    
        cols = '`,`'.join(self.fnl) #used \ because we want the quote to be literal, thus using backslash as escape character is necessary when we want control chars to be literal chars.
        
        cols = '`' + cols + '`'
    
        vals = ('%s,' * len(self.fnl))[:-1]
        
        tokens = []
      
        #order of dictionary and its composition (values) can change so we use fnl for inserting into DB
        for fieldname in self.fnl:
            tokens.append(self.data[n][fieldname])
        
        
        
        sql = 'INSERT INTO `' + self.tn + '` (' +cols+ ') VALUES (' +vals+ ');'
        
        
        
        self.connect()

        cur = self.conn.cursor(pymysql.cursors.DictCursor)
   
        print(sql)
        print(tokens)
    
        cur.execute(sql,tokens)
        
        self.data[n][self.pk] = cur.lastrowid
        

<<<<<<< Updated upstream
        
    def verifyNew(self, n = 0):  # return true or false, keep track of all attempts in it's own data structure (list)
        self.errorlist = []
=======
    def delete(self,n=0):
        item = self.data.pop(n)
        self.deleteByID(item[self.pk])

    def deleteByID(self, id):
        sql = 'DELETE FROM `' + self.tn + '` WHERE `' + self.pk + '` = %s;'
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql,tokens)
>>>>>>> Stashed changes

