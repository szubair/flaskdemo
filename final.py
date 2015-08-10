import customer
from flask import Flask,render_template
app = Flask(__name__)

check = {'name':'Disk Usage', 'id':'1'}
checks = [{'name':'Disk Usage', 'id':'1'},{'name':'Failed Logins', 'id':'2'}]

server = {'instance':'instance_id', 'private': 'private_ip'}
servers = [{'instance':'i-uuru', 'private': '192.168'},{'instance':'i-aa','private':'192.168'}]

@app.route('/noc/')
@app.route('/noc/Home')
def showCustomers():
   #return "This page will show all SS customers"
   #customers = customer.getCust_names()
   customers = customer.showCustomer()
   return render_template('home.html', customers = customers)
      
@app.route('/noc/<customer>', methods=['GET'])
def showServers(customer):
   #return "This page will show customer %s details" % customer
   #filename = customer.customerInfo(customer)
   filename = '/home/sabeerz/syscheck/info/isssdb.info'
   servers = customer.serverInfo(filename)
   return servers
   #return render_template('server.html', servers = servers)
   
@app.route('/noc/<customer>/<server_ip>')
def showChecks(server):
   #return "This page will show customer %s server %s health status" % (customer,server_ip)
   return render_template('checks.html', checks = checks)


if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=5000)
