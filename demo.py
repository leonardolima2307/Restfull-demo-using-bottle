from bottle import run, get , post, request ,delete
#create the data sctructure, employee have a name and a type 
employees = [{'name':'Marco','type' : 'Creative'},
             {'name':'Luv','type' : 'BI'},
             {'name':'Connor','type' : 'Support'}]
#This function returns all employees 
@get('/employee')
def getAll():
    return {'empoyee' :employees}
#This function returns a specifict employee that is in the array
@get('/employee/<name>')
def getOne(name):
    the_employee = [employee for employee in employees if employee['name'] == name]
    return{'employee' : the_employee[0]}
#This function creates a empoyee using a json in the body of the call
@post('/employee')
def addOne():
    new_employee = {'name' : request.json.get('name'), 'type' : request.json.get('type')}
    employees.append(new_employee)
    return {'empoyee' :employees}
#Similar to @getOne This function deletes a specifict employee 
@delete('/employee/<name>')
def removeOne(name):
    the_employee = [employee for employee in employees if employee['name'] == name]
    employees.remove(the_employee[0])
    return {'empoyee' :employees}
#starts the server instance
run(reloader=True, debug=True)