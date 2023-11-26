from mainFunc import Stack

class PDA:
    def __init__(self, states, inputs, stacks, initial_state, initial_stack, accept_state, accept_condition, transitions):
        self.states = states
        self.inputs = inputs
        self.stacks = stacks
        self.state = initial_state
        self.stack = Stack([], -1)
        self.stack.push(initial_stack)
        self.accept_state = accept_state
        self.accept_condition = accept_condition
        self.transitions = transitions
    
    def run(self,input):
        if (input not in self.inputs and input!='e'):
            return False
        else:
            ret = False
            for j in self.transitions:
                if ((j[0] == self.state or j[0] == '_') and j[2] == self.stack.Top()):
                    if (j[1] == input) :
                        ret=True
                        if j[0] == '_':
                            self.state = self.state
                        else:
                            self.state = j[3]
                        self.stack.pop()
                        if (k!='e'):
                            for k in reversed(j[4]):
                                self.stack.push(k)
                    if (j[1] == 'e'):
                        self.state = j[3]
                        self.stack.pop()
                        if (k!='e'):
                            for k in reversed(j[4]):
                                self.stack.push(k)                        
                        break              
            return ret
    
    def isAccept(self):
        if ((self.state == self.accept_state and self.accept_condition == 'F') or (self.stack.isEmpty() and self.accept_condition == 'E')):
            return True
        else:
            return False
    