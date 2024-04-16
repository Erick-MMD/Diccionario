meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'XD':'Es una carita riéndose',
            'CHEUGY':'Algo que está pasado de moda o una persona que se esfuerza demasiado',
            'DEAD':'Algo es tan gracioso que el hablante se ha «muerto» de risa',
            'OUTFIT':'La ropa que estas llevando',
            'NPC':'Persona que no hace nada',
}

print('Hola, dime cual palabra deseas saber')
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print('El significado de',word, 'es:',meme_dict[word])
else:
    print('No tenemos esa definición')
            
