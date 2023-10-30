class college:
    def __init__(self,name,roll_no,contact,addresh):
        self.name = name
        self.roll_no = roll_no
        self.contact = contact
        self.addresh = addresh
    def info(self):
        print(f"My name is {self.name} and my roll no is {self.roll_no} and this is my contact number {self.contact} and i used to live near {self.addresh}")
    
a = college("sansat",101,7232984880," new link raod ic colony borivali west")
a.info()
b = college("alam",102,)
b.name = 
b.roll_no = 102
b.contact = 7343984884
b.addresh = "new ghatkopar road andheri east "
b.info()