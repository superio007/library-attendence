import string
import cv2
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",database="student_data",passwd="123456")



cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    ret, img = cap.read()

# detect and decode
     
    data, bbox, _ = detector.detectAndDecode(img)
   # check if there is a QRCode in the image
    mytup=[]
    if data:
        a=data
        mytup=str(data[2:7])
        time_now = datetime.now()
        dStr = time_now.strftime("%y-%m-%d")
        tStr = time_now.strftime("%H:%M:%S")
        break
    cv2.imshow("QRCODEscanner", img)   
    if cv2.waitKey(1) == ord("q"):
        break

mycursor= mydb.cursor()
s="INSERT INTO data (Student_ID,Date,Students_Data,Time) VALUES(%s,%s,%s,%s) "
b1=(mytup,dStr ,data,tStr)
mycursor.execute(s,b1)
mydb.commit()

    
print(dStr)
print(data)
print(mytup)
print(tStr)
 
#b=open('1.csv','a')
#b.writelines(data)
#b.writelines(dStr)
#b.writelines(tStr)
#b.close()

cap.release()
cv2.destroyAllWindows()
