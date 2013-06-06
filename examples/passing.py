import nengo.nef_theano as nef
import spa

class Rules:
    def rule1():
        condition(state1='A')
        effect(state1='Z', state2='A')
    def rule2():
        condition(state2='A', state1='-A')        
        effect(state2='A', state3='A')
    def rule3():
        match(state2==state3)
        #condition(state2=state3)
        effect(state1='B')
    def rule4():
        condition(state1='B')
        effect(state1='B')
            
        


class Sequence(spa.SPA):
    vocab = spa.Vocabulary(8)
    verbose = True
    
    state1 = spa.Buffer(feedback=0)
    state2 = spa.Buffer(feedback=0)
    state3 = spa.Buffer(feedback=0)
    
    bg = spa.BasalGanglia(Rules)
    thal = spa.Thalamus(bg)
    
    input = spa.Input(0.1, state1='A')
    
    
net = nef.Network('Sequence', fixed_seed=1)
model = Sequence(net)


pThal = net.make_probe('thal.rule', dt_sample=0.001, pstc=0.005)
pStr = net.make_probe('bg.StrD2', dt_sample=0.001, pstc=0.01)
print 'running..'
net.run(1)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(pStr.get_data())
plt.figure()
plt.plot(pThal.get_data())
plt.show()
