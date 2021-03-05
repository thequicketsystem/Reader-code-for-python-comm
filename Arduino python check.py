##Testing for Serial Comm with Arduino

import serial
import time



def Call_reader():

    
   # print("calling reader")

    tag_IDs = [""]
    first = arduino.write(b'1')
    print(first)
    write2 = 0

    end =0

    time_start = time.time()

   # print("entering while loop")


    while end == 0:

   #     print("while loop")
   
        time_now = time.time()

        time_diff = time_now - time_start

##        if time_diff > 6 and write2 ==0:
##            
##            print("writing to arduino again")
##            test = arduino.write(b'1')
##            print(test)
##            write2 =1

        if time_diff > 9:
            break
              
        data = arduino.readline()


        if data:
           # print(data)

            proper = data.decode()

            #print(proper)

        
            if proper == "1234":                # check for message signaling end of read
                print("Reading over")
                break
        

            if proper[:3] == "e20":                 ## check to see if our tag

                tag_IDs.append((proper[:-2]))

                
##            print("Current list: ")
##            print (tag_IDs)
##            index += 1           


  #  print ("exciting read cycle")


    for spec in tag_IDs:
        print(spec)
        


    return tag_IDs[1:]






## main code for testing 
# /dev/ttyUSB0 corresponds to the top USB3 port on the rPi 4
arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout =.1)



print("hello world")


time.sleep(2)



print("first call")
##init = arduino.write(b'1')
##print(init)
x = 0

x = Call_reader()

print("\n")
print(x)


time.sleep(3)

print("second call")

y = Call_reader()


print(y)

##while True:
##    arduino.write(b'1')
##    data = arduino.readline()[:-2]
##    if data:
##        print(data)



