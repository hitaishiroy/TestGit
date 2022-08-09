
import json



from flask import Flask,jsonify

#import names
import random

app = Flask(__name__)

def generateNumber():
   # temp = [] #1234567890
   # for i in range(1,11):
   #    while len(temp)!=10:

   #       temp.append(str(random.randrange(1,11)))
   # phoneNumber = "".join(temp)
   #print(phoneNumber)
   t = random.randrange(1,12)
   r = random.randrange(1,5)
   total = t + r

   return total


@app.route('/', methods = ['GET'])

def generateData():
   # personName = names.get_full_name()
   # tb = generateNumber()
   # emailId = personName.replace(" ","").lower() + '@xyz.com'
   temp = str(generateNumber())
   

   #return jsonify(Name = personName, mobNumber = '+'+tb, Email = emailId)
   return temp
   


if __name__=='__main__':
    app.run('localhost', debug='True')

