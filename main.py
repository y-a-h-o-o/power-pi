from INA226 import ina

def setup():
    pass

def loop(): 
    # here will be an infinite loop until something happens, but during it we will
    # read and output the current voltage and current and time 
    # write the data onto a file
    # sleep for an unspecified amount of time
    # check for button inputs for actions
    pass

if __name__ == "__main__":
    try:
        setup() 
        while(True):
            loop()
    except KeyboardInterrupt:
        destroy()

