for i in range(0,10):  #range tag tegund af collection
    if i == 5: #nested inn í for lykkjunni
        break # fæ þá út 0-4 og hættir við 5 en ef eg væri með continoue þá myndi ég fá 0,1,2,3,4,6,7,8,9
    print(i, end=' ')
else:
    print('Done')

print() #prentar út restina í nýrri línu

i=0
while i < 10: #geri það sama og í for, nema for er miklu styttri
    print(i, end=' ')
    i += 1
print()
for ch in 'forritun': #hér höfum við string og er tegund af collection
    print(ch, end=' ')

print()

for i in range(0,5): #nested forlykkja ein forlykkja inn í annarri
    print(i)
    for j in range(0,3):
        print(j, end=' ')
    print()


