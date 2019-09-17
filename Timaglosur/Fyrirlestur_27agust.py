num = int(input('Input a number:'))

counter = 0
while counter < num:
    print(counter, end=' ') #segi printfallinu að prenta út eina línu með gildum
    counter += 1
    if counter == 5:
        break # hoppa alveg út úr while lykkjunni else hlutinn veður heldur ekki keyrður
else:
    print('Done') #ef boolean segðin er false
