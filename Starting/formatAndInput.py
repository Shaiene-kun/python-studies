a = int( input("Numero a: ") )
b = int( input("Numero b: ") )
sum = a + b
sub = a - b
mult =  a * b
div = a / b
remains = a % b
print ( "a = {num1} \nb = {num2}".format(num1=a, num2=b) )
print ("Sum: {}".format(sum))
print ("Sub: {}".format(sub))
print ("Mult: {}".format(mult))
print ("Div: {}".format(div))
print ("Whole Div: {}".format( int(div) ) )
print ("Remains: {}".format(remains) )

