#def convertMetrotoKM(metre): 

    #"""
    

    #"""
    
    
    #return metre * 0.001 

#km = (convertMetrotoKM(metre=10000)) 
#print(km)

def bmi(weight, height):

    """
    - this function calcualtes bmi with weight and height
    - two parameters required: weight(in kg) and height in (m)
    
    """
    return weight / height ** 2

my_bmi =round(bmi(68, 1.78),2)

print(my_bmi)






