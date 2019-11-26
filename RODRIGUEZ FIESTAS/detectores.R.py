#Programa11- Calcular el promedio de total pasivo
#Declaración
t_pasivo2009=0.0
t_pasivo2010=0.0
t_pasivo2011=0.0
promedioT=0.0

#Input
t_pasivo2009=float(input("Ingrese total pasivo 2009:"))
t_pasivo2010=float(input("Ingrese total pasivo 2010:"))
t_pasivo2011=float(input("Ingrese total pasivo 2011:"))


#Processing
promedioT=(t_pasivo2009+t_pasivo2010+t_pasivo2011)/3

# DETECTOR
# Sera un total pasivo elevado cuando su promedio > 27
t_pasivo_elevado=(total > 27)

#Output
print("###############################################")
print("#            BALANCE DE PAGOS                 #")
print("###############################################")
print("# total pasivo 2009: ",t_pasivo2009,"         #")
print("# total pasivo 2010: ",t_pasivo2010,"         #")
print("# total pasivo 2011: ",t_pasivo2011,"         #")
print("###############################################")
print("    Promedio de total pasivo: ",promedioT       )
print("# total pasivo elevado: ",t_pasivo_elevado,"  #")
print("###############################################")


#Programa12- Calcular el promedio total de capital contable
#Declaración
t_cap_contable2009=0.0
t_cap_contable2010=0.0
t_cap_contable2011=0.0
promedioC=0.0

#Input
t_cap_contable2009=float(input("Ingrese total capital contable 2009:"))
t_cap_contable2010=float(input("Ingrese total capital contable 2010:"))
t_cap_contable2011=float(input("Ingrese total capital contable 2011:"))

#Processing
promedioC=(t_cap_contable2009+t_cap_contable2010+t_cap_contable2011)/3

# DETECTOR
# Sera un total capital contable superior cuando su promedio > 17
t_cap_contable_elevado=( total > 17)

#Output
print("#################################################################")
print("#                     BALANCE DE PAGOS                          #")
print("#################################################################")
print("# total capital contable 2009: ",t_cap_contable2009,"           #")
print("# total capital contable 2010: ",t_cap_contable2010,"           #")
print("# total capital contable 2011 : ",t_cap_contable2011,"          #")
print("#################################################################")
print(   "Promedio total de capital contable: ",promedioC                )
print(" #total capital contrable elevado: ",t_cap_contable_elevado,"  #" )
print("#################################################################")


#Programa13- Calcular el total activos
#Declaración
t_activos2006=0.0
t_activos2007=0.0
t_activos2005=0.0
total=0.0

#Input
t_activos2006=float(input("Ingrese total activos 2006:"))
t_activos2007=float(input("Ingrese total activos 2007:"))
t_activos2005=float(input("Ingrese total activos 2005:"))


#Processing
Total=(t_activos2006+t_activos2007+t_activos2005)

# DETECTOR
# Sera un total activos bajo cuando el total < 107
t_activos_bajo=( total < 107)


#Output
print("#####################################################")
print("#                    BALANCE DE PAGO                #")
print("#####################################################")
print("# total activos 2006 :  ",t_activos2006,"           #")
print("# total activos 2007 :   ",t_activos2007,"          #")
print("# total activos 2005 :   ",t_activos2005,"          #")
print("#####################################################")
print(                 "Total: ",Total                       )
print("   # total pasivo elevado: ",t_pasivo_elevado,"  #"   )
print("#####################################################")


#Programa14- Calcular el promedio de total de la participacion controladora
#Declaración
t_participacion_controladora2009=0.0
t_participacion_controladora2010=0.0
t_participacion_controladora2011=0.0
promedioK=0.0

#Input
t_participacion_controladora2009=float(input("Ingrese total participacion controladora 2009:"))
t_participacion_controladora2010=float(input("Ingrese total participacion controladora 2010:"))
t_participacion_controladora2011=float(input("Ingrese total participacion controladora 2011:"))


#Processing
promedioK=(t_participacion_controladora2009+t_participacion_controladora2010+t_participacion_controladora2011)/3

# DETECTOR
# Sera un total participacion controladora elevado cuando su promedio > 15
t_participacion_controladora_elevado=( total > 15)


#Output
print("#####################################################################################")
print("#                            BALANCE DE PAGO                                        #")
print("######################################################################################")
print("# total participacion controladora 2009: ",t_participacion_controladora2009,"        #")
print("# total participacion controladora 2010  : ",t_participacion_controladora2010,"      #")
print("# total participacion controladora 2011 : ",t_participacion_controladora2011,"       #")
print("######################################################################################")
print("# total participacion controladora elevado: ",t_participacion_controladora,"         #")
print("Promedio de total de la participacion controladora: ",        promedioK                )
print("######################################################################################")


#Programa15- Calcular el promedio de ventas netas
#Declaración
ventas_netas2005=0.0
ventas_netas2008=0.0
ventas_netas2014=0.0
promedioR=0.0

#Input
ventas_netas2005=float(input("Ingrese ventas netas 2005:"))
ventas_netas2008=float(input("Ingrese ventas netas 2008:"))
ventas_netas2014=float(input("Ingrese ventas netas 2014:"))

#Processing
promedioR=(ventas_netas2005+ventas_netas2008+ventas_netas2014)/3

# DETECTOR
# Sera un total ventas netas elevado cuando su promedio > 18
ventas_netas_elevado=( total > 18)

#Output
print("#####################################################")
print("#                 BALANCE DE PAGO                   #")
print("#####################################################")
print("# ventas netas 2005: ",ventas_netas2005,"           #")
print("# ventas netas 2008  : ",ventas_netas2008,"         #")
print("# ventas netas 2014 : ",ventas_netas2014,"          #")
print("#####################################################")
print("# total ventas netas : ",ventas_netas,"             #")
print("Promedio de ventas netas: ",promedioR                 )
print("#####################################################")


#Programa16- Calcular el promedio de utilidad bruta
#Declaración
utilidad_bruta2005=0.0
utilidad_bruta2006=0.0
utilidad_bruta2007=0.0
promedioG=0.0

#Input
utilidad_bruta2005=float(input("Ingrese utilidad bruta 2005:"))
utilidad_bruta2006=float(input("Ingrese utilidad bruta 2006:"))
utilidad_bruta2007=float(input("Ingrese utilidad bruta 2007:"))


#Processing
promedioG=(utilidad_bruta2005+utilidad_bruta2006+utilidad_bruta2007)/3

# DETECTOR
# Sera un total de utilidad bruta superior cuando su promedio > 8
utilidad_bruta_superior=( total > 😎

#Output
print("#######################################################")
print("#                    BALANCE DE PAGO                  #")
print("#######################################################")
print("# utilidad bruta 2005 : ",utilidad_bruta2005,"        #")
print("# utilidad bruta 2006 : ",utilidad_bruta2006,"        #")
print("# utilidad bruta 2007 : ",utilidad_bruta2007,"        #")
print("#######################################################")
print("# total utilidad bruta :     ",utlidad_bruta,"        #")
print("Promedio de utilidad bruta: ",        promedioG         )
print("#######################################################")


#Programa17- Calcular el promedio total de capital contable
#Declaración
t_cap_contable2014=0.0
t_cap_contable2013=0.0
t_cap_contable2012=0.0
promedioD=0.0

#Input
t_cap_contable2014=float(input("Ingrese total capital contable 2014:"))
t_cap_contable2013=float(input("Ingrese total capital contable 2013:"))
t_cap_contable2012=float(input("Ingrese total capital contable 2012:"))


#Processing
promedioD=(t_cap_contable2014+t_cap_contable2013+t_cap_contable2012)/3

# DETECTOR
# Sera un total de capital contable superior cuando su promedio > 12
t_cap_contable=( total > 12)

#Output
print("###############################################################")
print("#                        BALANCE DE PAGO                      #")
print("###############################################################")
print("# total capital contable 2014:  ",t_cap_contable2014,"        #")
print("# total capital contable 2013  : ",t_cap_contable2013,"       #")
print("# total capital contable 2012 : ",t_cap_contable2012,"        #")
print("###############################################################")
print("# total capital contable : ",t_cap_contable,"                 #")
print("Promedio total de capital contable: ",promedioD                 )
print("###############################################################")

#Programa18- Calcular el total activos
#Declaración
t_activos2014=0.0
t_activos2013=0.0
t_activos2012=0.0
total=0.0

#Input
t_activos2014=float(input("Ingrese total activos 2014:"))
t_activos2013=float(input("Ingrese total activos 2013:"))
t_activos2012=float(input("Ingrese total activos 2012:"))


#Processing
Total=(t_activos2014+t_activos2013+t_activos2012)

# DETECTOR
# Sera un total activos elevado cuando su promedio > 111
t_activos_elevado=( total > 111)

#Output
print("#####################################################")
print("#               BALANCE DE PAGO                     #")
print("#####################################################")
print("# total activos 2014: ",t_activos2014,"             #")
print("# total activos 2013  : ",t_activos2013,"           #")
print("# total activos 2012 : ",t_activos2012,"            #")
print("#####################################################")
print("# total activos : ",t_activos,"                     #")
print(              "Total: ",Total                          )
print("#####################################################")


#Programa19- Calcular el promedio de total pasivo
#Declaración
t_pasivo2005=0.0
t_pasivo2006=0.0
t_pasivo2007=0.0
promedioX=0.0

#Input
t_pasivo2005=float(input("Ingrese total pasivo 2005:"))
t_pasivo2006=float(input("Ingrese total pasivo 2006:"))
t_pasivo2007=float(input("Ingrese total pasivo 2007:"))


#Processing
promedioX=(t_pasivo2005+t_pasivo2006+t_pasivo2007)/3

# DETECTOR
# Sera un total pasivo alto cuando su promedio > 22
t_pasivo_alto=( total > 22)

#Output
#Output
print("####################################################")
print("#           BALANCE DE PAGO                        #")
print("####################################################")
print("# total pasivo 2005: ",t_pasivo2005,"              #")
print("# total pasivo 2006  : ",t_pasivo2006,"            #")
print("# total pasivo 2007 : ",t_pasivo2007,"             #")
print("####################################################")
print("# total pasivo : ",t_pasivo,"                      #")
print("Promedio de total pasivo: ",promedioX                )
print("####################################################")



#Programa20- Calcular el promedio de total de la participacion controladora
#Declaración
t_participacion_controladora2005=0.0
t_participacion_controladora2006=0.0
t_participacion_controladora2007=0.0
promedioK=0.0

#Input
t_participacion_controladora2005=float(input("Ingrese total participacion controladora 2005:"))
t_participacion_controladora2006=float(input("Ingrese total participacion controladora 2006:"))
t_participacion_controladora2007=float(input("Ingrese total participacion controladora 2007:"))


#Processing
promedioK=(t_participacion_controladora2005+t_participacion_controladora2006+t_participacion_controladora2007)/3

# DETECTOR
# Sera un total de participacion controladora superior cuando su promedio > 14
t_participacion_controladora_superior=( total > 14)

#Output
print("############################################################################################")
print("#                                     BALANCE DE PAGO                                      #")
print("############################################################################################")
print("# total participacion controladora 2005: ",t_participacion_controladora2005,"              #")
print("# total participacion controladora 2006  : ",t_participacion_controladora2006,"            #")
print("# total participacion controladora 2007 : ",t_participacion_controladora2007,"             #")
print("############################################################################################")
print("# total de la participacion controladora : ",t_participacion_controladora,"                                   #")
print("Promedio de total de la participacion controladora: ",promedioK                              )
print("############################################################################################")
