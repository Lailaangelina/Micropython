from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    #forwards state 0
    if state == 0:
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000 :
            state = 2
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()  
            
    #forwards state 1
    elif state == 1:
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() >= 2300 and mycontroller.right_odom.get_count() >= 2300 :
            state = 3
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count() 


        

    #turning state
    elif state == 2:
        mycontroller.raft.led_on()
        
        mycontroller.left_turn()
        #increase turns made counter
        turns_made += 1

        #two transition conditions
        if turns_made < 2 :
            state = 0
        else :
            state = 1
    
    #stopping state
    elif state == 3 :
        mycontroller.stop()