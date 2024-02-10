from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    #forwards state
    if state == 0:
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() == 1000 and mycontroller.right_odom.get_count() == 1000 and turns_made == 0 :
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count() 
        

    #turning state number one
    elif state == 1:
        mycontroller.raft.led_on()
        
        mycontroller.custom_left_turn(100)
        #increase turns made counter
        turns_made += 1

        state = 2

    elif state == 2:
        
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() > 1500 and mycontroller.right_odom.get_count() > 1500 and turns_made == 1 :

            mycontroller.custom_right_turn(100)

            turns_made += 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count() 

            state = 3
    elif state == 3:
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() > 1500 and mycontroller.right_odom.get_count() > 1500 and turns_made == 1 :

            mycontroller.custom_left_turn(100)

            turns_made += 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count() #At the third turn


            
        

    
    #stopping state
    elif state == 5 :
        mycontroller.stop()