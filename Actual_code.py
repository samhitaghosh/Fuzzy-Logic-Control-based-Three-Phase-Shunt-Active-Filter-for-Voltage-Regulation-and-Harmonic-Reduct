#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Sign = ctrl.Antecedent(np.arange(-1,1.1,0.10),'sign')
Strength = ctrl.Antecedent(np.arange(-1,1.1,0.10),'strength')
preg = ctrl.Consequent(np.arange(-1,1.1,0.10),'preg')

Sign['Negative'] = fuzz.trimf(Sign.universe,[-1,-1,0])
Sign['Zero'] = fuzz.trimf(Sign.universe,[-1,0,1])
Sign['Positive'] = fuzz.trimf(Sign.universe,[0,1,1])
Strength['Small'] = fuzz.trimf(Sign.universe,[-1,-1,0])
Strength['Medium'] = fuzz.trimf(Sign.universe,[-1,0,1])
Strength['Large'] = fuzz.trimf(Sign.universe,[0,1,1])

preg['NL'] = fuzz.trapmf(preg.universe, [-1, -1,-0.7,-0.3])
preg['NM'] = fuzz.trapmf(preg.universe, [-0.7, -0.3,-0.3,-0.1])
preg['NS'] = fuzz.trapmf(preg.universe, [-0.3, -0.1,-0.1,0])
preg['ZE'] = fuzz.trapmf(preg.universe, [-0.1,0, 0, 0.1])
preg['PS'] = fuzz.trapmf(preg.universe, [0, 0.1, 0.1,0.3])
preg['PM'] = fuzz.trapmf(preg.universe, [0.1, 0.3, 0.3,0.7])
preg['PL'] = fuzz.trapmf(preg.universe, [0.3,0.7,1,1])

Sign.view()
Strength.view()
preg.view()



rule1 = ctrl.Rule(Sign['Negative']&Strength['Small'],preg['NS'])
rule2 = ctrl.Rule(Sign['Negative']&Strength['Medium'],preg['NM'])
rule3 = ctrl.Rule(Sign['Negative']&Strength['Large'],preg['NL'])
rule4 = ctrl.Rule(Sign['Zero'],preg['ZE'])
rule5 = ctrl.Rule(Sign['Positive']&Strength['Small'],preg['PS'])
rule6 = ctrl.Rule(Sign['Positive']&Strength['Medium'],preg['PM'])
rule7 = ctrl.Rule(Sign['Positive']&Strength['Large'],preg['PL'])

tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['sign'] = -0.1
tipping.input['strength'] = -0.1
tipping.compute()
print(tipping.output['preg'])
preg.view(sim=tipping)

