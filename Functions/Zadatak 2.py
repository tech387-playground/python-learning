# 2.  Write a function that accepts 2 arguments, first one is any given data type, second one is user input value.
# Function should check if the input value satisfies the data type condition of the first argument.



def check_data_type(data_type, value):
    if(type(value)==data_type):
        print('yes')
    if(type(value)!=data_type):
        print('no')
    
var1 = 5.65
print('Da li je varijabla tipa int?')
check_data_type(type(int()),var1)

print('Da li je varijabla tipa float?')
check_data_type(type(float()),var1)

print('Da li je varijabla tipa string?')
check_data_type(type(str()),var1)