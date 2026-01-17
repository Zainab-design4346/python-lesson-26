class element:
    def fun1(self, nums, val):
        dict1 = {}
        for i, num in enumerate(nums):
            if val - num in dict1:
                return (dict1[val - num], i)
            dict1[num] = i

sum = int(input("Enter sum : "))
print("index1=%d, index2=%d" % element().fun1((10,20,30,40,50),sum))
            
