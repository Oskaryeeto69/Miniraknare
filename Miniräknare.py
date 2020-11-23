def add(x, y): # hittade detta på google för att göra det lättare att skriva
    return x + y # hittade detta på google för att göra det lättare att skriva
def subtract(x, y): # hittade detta på google för att göra det lättare att skriva
    return x - y
def multiply(x, y): # hittade detta på google för att göra det lättare att skriva
    return x * y

räknetyp = str(input('Tjabba å välkommen till den goa miniräknarn (klicka enter för att gå vidare)')) # välkomnar dig till miniräknaren
print('Välj ett räknesätt.') # frågar vilket räknesätt du vill använda eller om du vill avsluta
print('1. Räkna med addition') # säger att 1 är addition
print('2. Räkna med subtraktion') # säger att 2 är subtraktion
print('3. Räkna med multiplikation') # säger att 3 är multiplikation
print('4. För att avsluta') # säger att 4 avslutar programmet

while True: 

    val = input('Välj vilket räknesätt du vill använda eller om du vill avsluta (1 , 2, 3, 4) ') # ber dig välja räknesätt
    if val in('1', '2', '3', '4'): # säger att om valet är 
       
        if val == '1':
            num1 = float(input("Vad är första nummret: ")) # frågar vad första nummret är
            num2 = float(input("Vad är  andra nummret: ")) # frågar vad andra nummret är
            print ('Summan av', num1, '+', num2, '=', add (num1, num2)) # printar svaret av de två talen du skrev
        elif val == '2':
            num1 = float(input("Vad är första nummret: ")) # frågar vad första nummret är
            num2 = float(input("Vad är  andra nummeret: ")) # frågar vad andra nummret är
            print ('Differensen av', num1, '-', num2, '=', subtract (num1, num2)) # printar differensen av de två talen du skrev
        elif val == '3':
            num1 = float(input("Vad är första nummret: ")) # frågar vad första nummret är
            num2 = float(input("Vad är  andra nummeret: ")) # frågar vad andra nummret är
            print ('Produkten av', num1, '*', num2, '=', multiply (num1, num2)) # printar produkten av de två talen u skrev
        elif val == '4':
            print('Vad tråkigt att du inte ville räkna nå mer :(') # Detta printas när du klickar 4, när du avslutar alltså
            break
else:
    print("helt fel tänkt där")