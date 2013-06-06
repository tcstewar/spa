import nengo.nef_theano as nef
import spa

class Rules:
    def rule1():
        condition(state='A')
        effect(state='B')
    def rule2():
        condition(state='B')
        effect(state='C')
    def rule3():
        condition(state='C')
        effect(state='A')
        


class Sequence(spa.SPA):
    vocab = spa.Vocabulary(8)
    
    state = spa.Buffer()
    
    bg = spa.BasalGanglia(Rules)
    thal = spa.Thalamus(bg)
    
    input = spa.Input(0.1, state='A')
    
    
net = nef.Network('Sequence')
model = Sequence(net)


pThal = net.make_probe('thal.rule', dt_sample=0.001, pstc=0.005)

net.run(1)

import matplotlib.pyplot as plt
plt.plot(pThal.get_data())
plt.show()
