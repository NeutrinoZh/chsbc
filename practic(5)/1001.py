import winsound

sounds = [
    (440,500), (440,500), (440,500), (349,350), (523,150),
    (440,500), (349,350), (523,150), (440,1000), (659,500),
    (659,500), (659,500), (698,350), (523,150), (415,500),
    (349,350), (523,150), (440,1000)
]

for a, b in sounds:
    winsound.Beep(a, b)