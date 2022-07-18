"""li=[12,45,23,16,25,9,4]
su_li=sorted(li,reverse=True)
print("sorted value:",su_li)
print("orginal value:", li)"""

class employee():
    def __init__(self, name, age, pincode):
        self.name = name,
        self.age = age,
        self.pincode = pincode

        def __repr__(self):
            return '({},{},${})'.format(self.name,self.age,self.pincode)

e1=employee("vicky",22,624619)
e2=employee("arun",26,234678)

employes=[e1,e2]
def e_sort(emp):
    return emp.age
s_employee = sorted(employes, key=e_sort)
print(s_employee)
print(e1.name,e1.pincode,e1.age)



