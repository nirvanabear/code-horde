x, y =  "avocadotoast", "toast"


def isAnagramSimple(str_a,str_b):
   if(len(str_b) > len(str_a)):
      return False
   else:
      for i in range(len(str_b)):
         print(i)
         if i + len(str_b) <= len(str_a):
            print(str(i + len(str_b)) + ", " + str(len(str_a)))
            print(str_a[i: i+len(str_b)] + ", " + str_b)
            if str_a[i: i+len(str_b)] == str_b:
               return True
         else:
            return False
     

print(isAnagramSimple(x,y))
