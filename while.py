""" used controlled structure pdf and tutorial video
used chat gpt & github for reference """
total=0 # defining the variable to store the sum of numbers#
number_inputs=0 # defining the variable to store the number of inputs#
user=int(input("please enter number -1 to exit:"))
while user!=-1: # condition if not met the loop initiates#
    total+=user
    user=int(input("please enter number -1 to exit:"))
    number_inputs+=1 
    if user==-1: # condition if met then loop breaks#
        break
average=total/number_inputs # formulae to calculate average#
print ("Average is:{}" .format (average)) # format string used to concatenate float data type and print#