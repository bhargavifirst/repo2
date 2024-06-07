class UpperLower:
     def case(self,a):
         upper =[]
         lower = []
         for i in a:
             if i.islower():
                 upper.append(i)
             else:
                 lower.append(i)
         print(upper)
         print(lower)

l=UpperLower()
l.case("BHargaviPAvaN")
