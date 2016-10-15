import os
    
#cria matriz 3x3
vetor1=[' ',' ',' ']
vetor2=[' ',' ',' ']
vetor3=[' ',' ',' ']
matriz=[vetor1,vetor2,vetor3]

#imprime o ambiente na tela
def ambiente():
    
    print ("JOGO DA VELHA")
    print ("----------------")
    print ('','1',matriz[0][0],'2',matriz[0][1],'3',matriz[0][2],'',sep=" | ")
    print ('','4',matriz[1][0],'5',matriz[1][1],'6',matriz[1][2],'',sep=" | ")
    print ('','7',matriz[2][0],'8',matriz[2][1],'9',matriz[2][2],'',sep=" | ")
    print ("----------------")

#captura as jogas do player
def jogadas_humana():
    
    jogada_humana = int(input("Jogada Humana = "))
    if jogada_humana == 1 and matriz[0][0] == ' ':
        matriz[0][0]= 'X'
        
    elif jogada_humana == 2 and matriz[0][1] == ' ':
        matriz[0][1]= 'X'
        
    elif jogada_humana == 3 and matriz[0][2] == ' ':
        matriz[0][2]= 'X'
        
    elif jogada_humana == 4 and matriz[1][0] == ' ':
        matriz[1][0]= 'X'
    
    elif jogada_humana == 5 and matriz[1][1] == ' ':
        matriz[1][1]= 'X'
    
    elif jogada_humana == 6 and matriz[1][2] == ' ':
        matriz[1][2]= 'X'
   
    elif jogada_humana == 7 and matriz[2][0] == ' ':
        matriz[2][0]= 'X'
        
    elif jogada_humana == 8 and matriz[2][1] == ' ':
        matriz[2][1]= 'X'
   
    elif jogada_humana == 9 and matriz[2][2] == ' ':
        matriz[2][2]= 'X'
   
    
#define as jogadas da IA
def jogadas_ia():
    
    if contador == 1:
        
         if (matriz [0][0] == "X" or matriz [2][0] == "X" or matriz [0][2] == "X"  or matriz [2][2] == "X"):
             if matriz [1][1] == ' ':
                matriz[1][1] = "O"
             
         elif (matriz [1][1] == "X"):
             if matriz [2][0] == ' ':
                 matriz[2][0] = "O"
             
         elif (matriz [0][1] == "X" or matriz [2][1] == "X" or matriz [1][2] == "X"  or matriz [1][0] == "X"):
             if matriz [0][0] == ' ':
                 matriz[0][0] = "O"       
             
    elif contador == 2:
        print("11")
     
        
            
#verifica se alguem ganhou
def verificar_ganhador():
    
    if matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2]=='X':
        print("Temos um vencendor")
        ganhador=1
    elif matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2]=='O':
        print("Temos um vencendor")
        ganhador=2

    elif matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0]=='X':
        print("Temos um vencendor")
        ganhador=1
        
    elif matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0]=='O':
        print("Temos um vencendor")
        ganhador=2

    elif matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2]=='X':
        print("Temos um vencendor")
        ganhador=1
        
    elif matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2]=='O':
        print("Temos um vencendor")
        ganhador=2
    
    elif matriz[1][0]== 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X':
        print("temos um vencedor")
        ganhador = 1

    elif matriz[1][0]== 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O':
        print("temos um vencedor")
        ganhador = 2     

    elif matriz[2][0]== 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X':
        print("temos um vencedor")
        ganhador = 1

    elif matriz[2][0]== 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O':
        print("temos um vencedor")
        ganhador = 2

    elif matriz[2][0]== 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X':
        print("temos um vencedor")
        ganhador = 1
        
    elif matriz[2][0]== 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O':
        print("temos um vencedor")
        ganhador = 2

    elif matriz[0][1]== 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X':
        print("temos um vencedor")
        ganhador = 1
        
    elif matriz[0][1]== 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O':
        print("temos um vencedor")
        ganhador = 2
    
    

#primeiro imprime o ambiente
ganhador = 0
ambiente()
contador = 0
while ganhador == 0 :
    contador = 1
    verificar_ganhador()
    jogadas_humana()
    verificar_ganhador()
    jogadas_ia()
    verificar_ganhador()
    contador += 1
    if contador == 5 or ganhador != 0:
        print(ganhador)
        break
    else:
        os.system("cls")
        ambiente()
        
    










