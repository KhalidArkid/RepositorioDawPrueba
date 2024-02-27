'''
Heu estat desafiat a implementar un programa que simula un joc d'endevinar una combinació de 5 lletres secretes. Cada vegada que feu un intent, el programa us donarà una 
pista per ajudar-vos a arribar a la combinació correcta.

La combinació consisteix en 5 lletres seleccionades aleatòriament. En cada intent, rebeu una pista per a cada lletra de la combinació. Les pistes es donen de la següent
 manera:

- Una lletra seguida d'un punt (.) indica que la lletra no és correcta.
- Una lletra seguida d'una O indica que heu encertat amb aquesta lletra.
- Una lletra seguida d'una X indica que la lletra és correcta, però no està en la posició correcta.

El programa continua fins que encerteu la combinació secreta. En aquest moment, rebreu un missatge de felicitació.

Requeriments del Programa:
1. Implementeu una funció per generar la combinació secreta de 5 lletres aleatòries.
2. Implementeu una funció principal que gestioni els intents de l'usuari i proporcioni les pistes corresponents.
3. Utilitzeu mètodes basats en paràmetres d'entrada i sortida.
4. Propagueu els valors entre invocacions dels mètodes per mantenir l'estat del joc.

Nota: Aquest exemple destaca la importància de l'ús de mètodes en la descomposició d'un problema complex i com gestionar les dades d'entrada i sortida de manera efectiva.


Exemple
```
> Escriu 5 lletres minúscules: atzbqLa resposta es [-OX--]. Continua intentant-ho!
> Escriu 5 lletres minúscules: btymz
La resposta es [-O-XX]. Continua intentant-ho!
> Escriu 5 lletres minúscules: mtzoc
La resposta es [OOX--]. Continua intentant-ho!
> Escriu 5 lletres minúscules: mtdzp
La resposta es [OO-OX]. Continua intentant-ho!
> Escriu 5 lletres minúscules: mtpze
La resposta es [OOOO-]. Continua intentant-ho!
> Escriu 5 lletres minúscules: mtpzx
La resposta es [OOOOO]. Has encertat!
'''

'''
TOP DOWN
1. Generar combinacion (random)
2. Mostrar pistas
3. Mostrar resposta
'''

lletres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
combinacio_secreta = []

def generar_combinacio() -> None:
    seed = 2
    for i in range(5):
        seed = (seed * 997) % 1000
        random = (seed * 503) % 1000 / 1000
        numero = int(random * len(lletres))
        combinacio_secreta.append(lletres[numero])

def mostrar_pistes(usuari_combinacio: list) -> str:

    pistes = []
    for i in range(5):
        if usuari_combinacio[i] == combinacio_secreta[i]:
            pistes.append("O")
        elif usuari_combinacio[i] in combinacio_secreta:
            pistes.append("X")
        else:
            pistes.append(".")
    return "".join(pistes)

def mostrar_resposta() -> None:
    generar_combinacio()
    while True:
        usuari_combinacio = list(input("Escriu 5 lletres minúscules: "))
        
        if len(usuari_combinacio) != 5:
            print("5 lletres PELELE no 80 ni 2, exactament 5 lletres.")
            continue
        
        pistes = mostrar_pistes(usuari_combinacio)
        print(f"La resposta és {pistes}. Continua intentant-ho com l'Atletic de Madrid!")
        
        if pistes == "OOOOO":
            print("Visca Barça, enhorabona, CHAMPIONSS!")
            break

mostrar_resposta()