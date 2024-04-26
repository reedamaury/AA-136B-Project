import time
from statemachine import StateMachine, State
 
class SpacecraftState(StateMachine):
 
    # creating states
    S1 = State("State1", initial = True)
    S2 = State("State2")
      
    # transitions of the state
    from_S1_to_S2 = S1.to(S2)
    from_S2_to_S1 = S2.to(S1)

CONDITION_S2 = True
     
### TWIDDLE_THUMBS: code simply addes space between code executions to allow for easier visability.
def twiddle_thumbs():
    print("*\n*\n*")
        
### CHECK_CAM: sends a request to the camera function and gets sensor information
def CHECK_cam():
    pass

### CHECK_ATT: sends a request to the attitude determination function and gets sensor information
def CHECK_att():
    pass

### TRIGGER_MAG: sends a request to trigger magnetorquers, and sends confirmation back to the running while loop
def TRIGGER_mag():
    pass

### TRIGGER_MOM: sends a request to trigger momentum wheels, and sends confirmation back to the running while loop
def TRIGGER_mom():
    pass

### MAIN: the main sequence of code that will run.
def main():

    ## Initial Setup Phase...
    twiddle_thumbs()
    print("Starting ADCS Sequence...")

    Spacecraft = SpacecraftState()
    current_state = Spacecraft.current_state
    print(current_state)

    if current_state == Spacecraft.S1:
        print ("Correct Start Sequence")
    else:
        raise("Incorrect Start Sequence, Spacecraft should start in S1")
    
    twiddle_thumbs()

    ## Move to State 2 Phase...
    print("running loop to meet State 2 target conditions...")
    while (CONDITION_S2) == False:
        print("within while loop...")

    print("target conditions met, transitioning to State 2...")


if __name__ == "__main__":
    main()