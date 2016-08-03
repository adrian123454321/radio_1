from radio import Radio

mi_radio=Radio("a")

desea_continuar=True
while desea_continuar:
	if mi_radio.encendido:
		opcion=input("1)apagar radio 2)elejir emisora3)subir volumen4)bajar volumen")
			if opcion==1:
				mi_radio.encendido=False
			else:
				mi_radio.encendido()

			if opcion==2
				canal=input("elija una emisora")
					if canal=fm:
						mi_radio.en_fm
					else:
						mi_radio.en_am=True




