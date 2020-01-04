# Marcu-Andria Battesti
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
land_yPrec = 0
deb_land_x = 0
fin_land_x = 0
land_xPrec = 0
ComputerCountCond = 0
ComputerCountOp = 0

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    
    #Récupération de l'altitude de la zone d'aterrissage et le debut et la fin de la zone
    if land_yPrec==land_y:
        ComputerCountCond+=1
        altiAtteri = land_y
        deb_land_x = land_xPrec
        fin_land_x = land_x
    else:
        ComputerCountCond+=1
        land_xPrec = land_x
        land_yPrec = land_y
    
    
    
#VVVVVVVVVVVVVVVVVVVV My Functions VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#Recupération de l'altitude restante avant l'aterrissage
def getAltitudeRestante(altiAtteri,y):
    altiRestante = y-altiAtteri
    return altiRestante
    
#Va servir à calculer la vitesse qu'il faut utiliser pour éviter le crash
def GetPrevisionP(iterRestante, v_speed):
    v_speed = 3.711*iterRestante-4*iterRestante- v_speed
    print("Prediction de vitesse à l'aterrissage : ",v_speed, file=sys.stderr)
    #Les degrés de puissance ont été choisit après divers tests. 
    #On aurait pu utiliser un algo génétique pour calculer les meilleurs palier
    if v_speed>39:
        pRecommend = 4
    elif v_speed>38:
        pRecommend = 2
    elif v_speed>31:
        pRecommend = 1                        
    else:
        pRecommend = 0
    return pRecommend
      
      
      
#C'est notre fonction principale
def CalculOptimisation(y, v_speed, land_y,altiAtteri, power):
    altRestante = getAltitudeRestante(altiAtteri,y)
    puissanceRecommend = 0
    #Cette condition évite la division par 0
    if v_speed != 0:
        nbIterRestMax = altRestante/(-v_speed)
        puissanceRecommend = GetPrevisionP(nbIterRestMax,v_speed)
    print("Puissance Recommend : ",puissanceRecommend, file=sys.stderr)
    return puissanceRecommend
        
            

    


    
#^^^^^^^^^^^^^^^^^^^^ My Functions ^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# game loop
while True:
    ComputerCountOp+=1
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    
    puissance = CalculOptimisation(y, v_speed, land_y, altiAtteri, power)
    ComputerCountCond+=2


    print("0",str(puissance))
    
    
    ComputeCount = ComputerCountCond+ComputerCountOp
    print("Total opération : ",ComputerCountOp, file=sys.stderr)
    print("Total condition : ",ComputerCountCond, file=sys.stderr)
    print("ComputeCount : ",ComputeCount, file=sys.stderr)
    
