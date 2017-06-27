
import time
import MySQLdb
import serial
dates = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
         'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
hours = {'08':'eight', '09':'nine', '10':'ten', '11':'eleven', '12':'twelve',
         '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen',
         '17':'seventeen', '18':'eighteen','19':'eighteen','20':'eighteen',
         '21':'eighteen', '22':'eighteen', '23':'eighteen','00':'eighteen',
         '01':'eight', '02':'eight', '03':'eight', '04':'eight', '05':'eight',
         '06':'eight', '07':'eight'}
db = MySQLdb.connect("localhost","root","eight88","myDb")

cursor = db.cursor()
ser = serial.Serial('/dev/ttyACM0')


while True:
    t = time.localtime()
    x = time.asctime(t)
    month = x[4:7]
    day = x[8:10]
    if day[0] == ' ':
        d = day
        day = '0'+d[1]
    year = x[20:24]
    date = year+'-'+dates[month]+'-'+day
    hour = hours[x[11:13]]
    sql = "select "+hour+" from angles where date = '"+date+"'"
    cursor.execute(sql)
    ang = cursor.fetchall()
    a = int(ang[0][0])
    ser.write(str(a))
    time.sleep(2)
    
    
