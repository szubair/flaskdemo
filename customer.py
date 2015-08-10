#!/usr/bin/python
import re
import os,commands

def showCustomer():
  cust_list = []
  fopen = open('./profile.txt','r')
  text = fopen.readlines()
  count = 0
  for each in text:
    c_dict = {}
    each = each.rstrip('\n').split(':')
    if count not in c_dict:
      count += 1
      c_dict['id'] = count
      c_dict['customer'] = each[0]
      c_dict['network'] = each[1]
    cust_list.append(c_dict)
  return cust_list
  
def customerInfo(customer):
  aws_profile = "aws ec2 describe-instances --profile %s" % customer
  #aws_filters = """ --filters "Name=instance-state-code,Values=16" --query "Reservations[*].Instances[*].{AInstanceId:InstanceId,BPrivateIp:PrivateIpAddress,DKeyPair:KeyName}" """
  aws_filters = """ --filters "Name=instance-state-code,Values=16" --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress,PrivateIpAddress,KeyName,Platform]" """
  aws_command = aws_profile + aws_filters
  #output = commands.getoutput(aws_command)
  dir = "/home/sabeerz/syscheck/info"
  file = ''.join([customer,'.info'])
  filename = os.path.join(dir, file)
  #if os.path.exists(dir):
  #   with open(filename,'w') as f2:
  #      f2.write(output)
  #   f2.close()
  return filename

def serverInfo(filename):
  server_list = []
  #filename = customerInfo(customer)
  fopen = open(filename, 'r')
  text = fopen.readlines()
  for each_line in text:
    each_line = each_line.split('\t')
    server_dict = {}
    server_dict['instance_id'] = each_line[0]
    server_dict['private_ip'] = each_line[2]
    server_dict['public_ip'] = each_line[1]
    server_dict['keypair'] = each_line[3]
    server_dict['os'] = each_line[4]
    server_list.append(server_dict)
  return server_list


#print customerInfo('isssdb')
print serverInfo('/home/sabeerz/syscheck/info/isssdb.info')    
#print showCustomer()
#print getCust_names()
#print getCust_ipaddr('Bastion')
