
#IMPRESIÓN ASCII
#Programa 1
#Declaración
paciente=" "
edad=0
altura=0.0
peso=0.0
masa_corporal=0.0

#Input
paciente=str(input("Ingrese nombre del paciente:"))
edad=int(input("Ingrese su edad:"))
altura=float(input("Ingrese su altura:"))
peso=float(input("Ingrese su peso :"))

#Processing
masa_corporal=(peso/altura)

#Output
print("###########################################")
print("#              Exámen Médico              #")
print("###########################################")
print("# Paciente : ",paciente,"                 #")
print("# Edad: ",edad,"                          #")
print("# Altura: ",altura,"                      #")
print("# Peso: ",peso,"                          #")
print("###########################################")
print("# Masa corporal: ",masa_corporal,"        #")
print("###########################################")


#Programa 2
#Declaración
alumno=" "
nota1=0.0
nota2=0.0
nota3=0.0
promedio=0

#Input
alumno=str(input("Ingrese nombre de alumno:"))
nota1=int(input("Ingrese nota1:"))
nota2=int(input("Ingrese nota2:"))
nota3=int(input("Ingrese nota3:"))

#Processing
promedio=(nota1+nota2+nota3)/3

# OUTPUT
print("##########################################")
print("#             Boleta de notas            #")
print("##########################################")
print("# Alumno : ",alumno,"                    #")
print("# Nota1: ",nota1,"                       #")
print("# Nota2: ",nota2,"                       #")
print("# Nota3: ",nota3,"                       #")
print("##########################################")
print("# Promedio: ",promedio,"                 #")
print("##########################################")

#Programa 3
#Declaración
producto= " "
inventario_inicial=0.0
compras=0.0
inventario_final=0.0
costo_ventas=0.0

#Input
producto=str(input("Producto: "))
inventario_inicial=float(input("Inventario inicial: "))
compras=float(input("Compras: "))
inventario_final=float(input("Inventario final: "))

#Processing
costo_ventas=(inventario_inicial+compras-inventario_final)

#Output
print("################################################")
print("#             Costo de ventas                  #")
print("################################################")
print("# Inventario inicial : ",inventario_inicial,"  #")
print("# Compras: ",compras,"                         #")
print("# Inventario final: ",inventario_final,"       #")
print("################################################")
print("# Costo de ventas: ",costo_ventas,"            #")
print("################################################")

#Programa 4
#Declaración
promedio_biologia=0
promedio_quimica=0
promedio_raz_verbal=0
promedio_raz_matematico=0
promedio_general=0

#Input
promedio_biologia=int(input("Ingrese promedio de biologia:"))
promedio_quimica=int(input("Ingrese promedio de quimica:"))
promedio_raz_verbal=int(input("Ingrese promedio de raz. verbal:"))
promedio_raz_mate=int(input("Ingrese promedio raz. matematico:"))

#Processing
promedio_general=(promedio_biologia+promedio_quimica+promedio_raz_verbal+promedio_raz_mate)/4

#Output
print("######################################################")
print("#                  Certificado de estudio            #")
print("######################################################")
print("# Promedio de Biología : ",promedio_biologia,"       #")
print("# Promedio de Química: ",promedio_quimica,"          #")
print("# Promedio de Raz.Verbal: ",promedio_raz_verbal,"    #")
print("# Promedio de Raz.Matemático: ",promedio_raz_mate,"  #")
print("######################################################")
print("Promedio general= ",promedio_general,"               #")
print("######################################################")

#Programa 5
#Declaración
total_base_imp=0.0
IVA21=0.0
retencion15=0.0
importe_total=0.0

#Input
total_base_imp=float(input("Ingrese total de base imponible:"))
IVA21=float(input("Ingrese IVA21:"))
retencion15=float(input("Ingrese retencion15:"))

#Processing
importe_total=(total_base_imp+IVA21-retencion15)

#Output
print("######################################################")
print("#               Boleta eléctronica                   #")
print("######################################################")
print("# Total de base imponible: ",total_base_imp,"        #")
print("# IVA 21%: ",IVA21,"                                 #")
print("# Retencion 15%: ",retencion15,"                     #")
print("######################################################")
print("# Importe total: ",importe_total,"                   #")
print("######################################################")

#Programa 6
#Declaración
libro_auditoría_t=0.0
libro_manual_c=0.0
compendio_l=0.0
total_pago=0.0

#Input
libro_auditoría_t=float(input("Ingrese el precio del libro autoría:"))
libro_manual_c=float(input("Ingrese el prefio del libro manual:"))
compendio_l=float(input("Ingrese el precio del compendioL: "))

#Processing
total_pago=(libro_auditoría_t+libro_manual_c+compendio_l)

#Output
print("#########################################")
print("#     BOLETA DE PAGO                    #")
print("#########################################")
print("# Libro autoría : ",libro_auditoría_t," #")
print("# Libro manual: ",libro_manual_c,"      #")
print("# Compendio: ",compendio_l,"            #")
print("#########################################")
print("# Total pagó: ",total_pago,"            #")
print("#########################################")

#Programa 7
#Declaración
valor_total=0.0
tasa_IGV=0.0
valor_neto=0.0
IGV=0.0

#Input
valor_total=float(input("Ingrese el valor total:"))
tasa_IGV=float(input("Ingrese la tasa de IGV:"))
valor_neto=float(input("Ingrese el valor neto:"))

#Processing
IGV=(valor_neto*tasa_IGV)

#Output
print("##################################")
print("#        Boleta eléctronica      #")
print("##################################")
print("# Valor total : ",valor_total,"  #")
print("# Tasa de IGV: ",tasa_IGV,"      #")
print("# Valor neto: ",valor_neto,"     #")
print("##################################")
print("# IGV: ",IGV,"                   #")
print("##################################")

#Programa 8
#Declaración
costo_directo=0.0
gasto_general_fijo=0.0
gasto_general_variable=0.0
utilidad=0.0
subtotal=0.0

#Input
costo_directo=float(input("Ingrese costo directo:"))
gasto_general_fijo=float(input("Ingrese gasto general fijo:"))
gasto_general_variable=float(input("Ingrese gasto general variable:"))
utilidad=float(input("Ingrese la utilidad:"))

#Processing
subtotal=(costo_directo+gasto_general_fijo+gasto_general_variable+utilidad)

#Output
print("#######################################################")
print("#            Presupuesto adicional de obra            #")
print("#######################################################")
print("# Costo directo : ",costo_directo,"                   #")
print("# Gasto general fijo: ",gasto_general_fijo,"          #")
print("# Gasto general variable: ",gasto_general_variable,"  #")
print("# Utilidad: ",utilidad,"                              #")
print("#######################################################")
print("# SubTotal: ",subtotal,"                              #")
print("#######################################################")

#Programa 9
#Declaración
descuento=0.0
precio_original=0.0
precio_descuento=0.0
precio_final=0.0

#Input
descuento=float(input("Ingrese el descuento:"))
precio_original=float(input("Ingrese el precio original:"))
precio_descuento=float(input("Ingrese el precio con descuento:"))

#Processing
precio_final=(precio_original-precio_descuento)

#Output
print("####################################################")
print("#                   Boleta de Pagó                 #")
print("####################################################")
print("# Descuento : ",descuento,"                        #")
print("# Precio original: ",precio_original,"             #")
print("# Precio con descuento: ",precio_descuento,"       #")
print("####################################################")
print("# Precio final ",precio_final,"                    #")
print("####################################################")

#Programa 10
#Declaración
Matematica=0
credit_mat=0
geometria=0
credit_geo=0
quimica=0
credit_quim=0
lenguaje=0
credit_leng=0
promedio_ponderado=0

#Input
Matematica=int(input("Promedio de Matemática: "))
credit_mat=int(input("Creditos de Mátematicas: "))
geometria=int(input("Promedio de Geometría: "))
credit_geo=int(input("Creditos de Geometría: "))
quimica=int(input("Promedio de Química: "))
credit_quim=int(input("Creditos de Química: "))
lenguaje=int(input("Promedio de Lenguaje: "))
credit_leng=int(input("Creditos de Lenguaje: "))

#Processing
promedio_ponderado=((Matematica*credit_mat)+(geometria*credit_geo)+(quimica*credit_quim)+(lenguaje*credit_leng))/(credit_mat+credit_geo+credit_quim+credit_leng)

# Output
print("##############################################")
print("#             Constancia de notas            #")
print("##############################################")
print("# Promedio de mátematica : ",Matematica,"    #")
print("# Creditos de mátematicas: ",credit_mat,"    #")
print("# Promedio de geometría: ",geometria,"       #")
print("# Creditos de geomatría ",credit_geo,"       #")
print("# Promedio de química: ",quimica,"           #")
print("# Creditos de química: ",credit_quim,"       #")
print("# Promedio de lenguaje: ",lenguaje,"         #")
print("# Creditos de lenguaje: ",credit_leng,"      #")
print("##############################################")
print("# Promedio ponderado: ",promedio_ponderado," #")
print("##############################################")
