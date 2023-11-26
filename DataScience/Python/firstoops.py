class college:
    def __init__(self,name,roll_no,contact,addresh):
        self.name = name
        self.roll_no = roll_no
        self.contact = contact
        self.addresh = addresh
    def info(self):
        return f"My name is {self.name} and my roll no is {self.roll_no} and this is my contact number {self.contact} and i used to live near {self.addresh}"
a = college("sansat",101,999999999," new link raod ic colony borivali west")
print(a.info())
print()
b = college("alam",102,9876543210,"shubam nagar road malad west")
print(b.info())
