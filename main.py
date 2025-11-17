from pyscript import display

Math = {'Sofie', 'Liam', 'Aaron', 'Jill'}
Science = {'Liam', 'Tessa', 'Aaron', 'Mila'}

display('The students involved in at least one club are: ' + str(Math | Science), target='output') #Union
display('The students who belong to both clubs are: ' + str(Math & Science), target='output') #Intersection
display('The students in the Math club are: ' + str(Math - Science), target='output') #Difference
display('The students in the Science club are: ' + str(Math - Science), target='output') #Difference
display('The students only in one club are: ' + str(Math ^ Science), target='output') #Symmetric Difference
