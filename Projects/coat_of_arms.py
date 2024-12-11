import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("cloud")

q1 = codesters.Circle(100,100,200, 'LemonChiffon')
q2 = codesters.Square (-100,100,200, 'MistyRose')
q3 = codesters.Circle(-100,-100,200, 'AliceBlue')
q4 = codesters.Square(100,-100,200, 'Honeydew')

s1 = codesters.Sprite("Brownwies",100,100)
s1.set_size(0.2)
s2 = codesters.Sprite("AltoClef",-100,-100)
s2.set_size(0.5)
s3 = codesters.Sprite("pencil",100,-100)
s3.set_size(0.15)
s4 = codesters.Sprite("cats",-100,100)
s4.set_size(0.16)

message1 = codesters.Text("Agnes",0,220,"black")
message2 = codesters.Text("Ninja never quit",0,-220,"black")