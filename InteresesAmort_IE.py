from tkinter import *
from tabulate import tabulate

####MODULOS####

#PARA INTERESES

def InteresSimple():
    IS = float(P.get())*float(r.get())*float(n.get())/float(t.get())
    VF = IS + float(P.get())
    F.set(VF)
    return Interes.set(IS)
def InteresCompuesto():
    IC = float(P.get())*((1+(float(r.get())/float(t.get())))**float(n.get())-1)
    VF = IC + float(P.get())
    F.set(VF)
    return Interes.set(IC)

#PARA AMORTIZACIONES

def TablaAmortizacionFrances():
    print("SISTEMA FRANCES:")
    P=float(Prest.get())
    i=((1+(float(TEA.get())/100))**(1/12))-1
    n=int(n_per.get())
    I=P*(i/(1-(1+i)**(-n)))
    datos=[["N°","CUOTA","INTERES","AMORTIZACION","CAPITAL VIVO","CAPITAL AMORTIZADO"]]
    Cuota=0
    TotCuota=0
    Interes=0
    TotInteres=0
    Amortiz=0
    TotAmortiz=0
    CapVivo=P-Amortiz
    CapAmort=0
    datos+=[[0,Cuota,Interes,Amortiz,CapVivo,CapAmort]]
    for k in range(1,n+1):
        Cuota=round(I,2)
        TotCuota+=Cuota
        Interes=round(CapVivo*i,2)
        TotInteres+=Interes
        Amortiz=round(Cuota-Interes,2)
        TotAmortiz+=Amortiz
        CapVivo=round(CapVivo-Amortiz,2)
        CapAmort=round(CapAmort+Amortiz,2)
        datos+=[[k,Cuota,Interes,Amortiz,CapVivo,CapAmort]]
    datos+=[["Total:",TotCuota,TotInteres,TotAmortiz,"...","..."]]
    print(tabulate(datos,headers="firstrow",tablefmt="fancy_grid"))

def TablaAmortizacionAleman():
    print("SISTEMA ALEMAN:")
    P=float(Prest.get())
    i=((1+(float(TEA.get())/100))**(1/12))-1
    n=int(n_per.get())
    datos=[["N°","DEUDA INIC.","INTERES","AMORT. REAL","AMORT.ACUM.","DEUDA PEND.","CUOTA"]]
    DeudaInicial=P
    Interes=round(P*i,2)
    TotInteres=0
    AmortReal=round(P/n,2)
    AmortAcum=AmortReal
    DeudaPend=DeudaInicial-AmortReal
    Cuota=Interes+AmortReal
    TotCuota=0
    datos+=[[1,DeudaInicial,Interes,AmortReal,AmortAcum,DeudaPend,Cuota]]
    for k in range(1,n+1):
        DeudaInicial=round(DeudaPend,2)
        Interes=round(DeudaInicial*i,2)
        TotInteres+=Interes
        AmortAcum+=AmortReal
        DeudaPend=DeudaInicial-AmortReal
        Cuota=Interes+AmortReal
        TotCuota+=Cuota
        datos+=[[k,DeudaInicial,Interes,AmortReal,AmortAcum,DeudaPend,Cuota]]
    datos+=[["Tot:","...",TotInteres,AmortAcum,"...","...",TotCuota]]
    print(tabulate(datos,headers="firstrow",tablefmt="fancy_grid"))

def TablaAmortizacionAmericano():
    print("SISTEMA AMERICANO:")
    P=float(Prest.get())
    i=((1+(float(TEA.get())/100))**(1/12))-1
    n=int(n_per.get())
    datos=[["N°","SALDO INIC.","INTERES","CAPITAL","CUOTA","SALDO FINAL"]]
    InteresTot=0
    CuotaTot=0
    for k in range(1,n):
        SaldoInicial=round(P,2)
        Interes=round(P*i,2)
        InteresTot+=Interes
        Capital=0
        Cuota=Interes
        CuotaTot+=Cuota
        SaldoFinal=SaldoInicial-Capital
        datos+=[[k,SaldoInicial,Interes,Capital,Cuota,SaldoFinal]]
    datos+=[[n,P,P*i,P,P*(1+i),0]]
    CuotaTot+=P
    datos+=[["Tot:","...",InteresTot,P,CuotaTot,"..."]]
    print(tabulate(datos,headers="firstrow",tablefmt="fancy_grid"))

####MAIN####
#general
raiz=Tk()
raiz.title("Ing Econ.")
raiz.geometry("450x480")
raiz.resizable(0,0)
Interes=DoubleVar()
F=DoubleVar()
t=DoubleVar()

#INTERESES#

#TITULO1
TIT=Label(raiz, text="INTERES SIMPLE Y COMPUESTO",bg="#FFFFFF")
TIT.place(x=110,y=20,width=200,height=20)
#capital
TxtCapital=Label(raiz, text="Capital:",anchor=W)
TxtCapital.place(x=40,y=50,width=120,height=20)
P=Entry(raiz)
P.place(x=250,y=50,width=150,height=20)
#Taza de Interes
TxtTazaInteres=Label(raiz, text="Taza de interes",anchor=W)
TxtTazaInteres.place(x=40,y=80,width=120,height=20)
r=Entry(raiz)
r.place(x=250,y=80,width=150,height=20)
#Tiempo
TxtTiempo=Label(raiz, text="Tiempo",anchor=W)
TxtTiempo.place(x=40,y=110,width=120,height=20)
n=Entry(raiz)
n.place(x=250,y=110,width=150,height=20)
#Unidad Tiempo
Opc1=Radiobutton(raiz,text="Dia",value=36000,variable=t)
Opc1.place(x=40,y=140)
Opc2=Radiobutton(raiz,text="Mes",value=1200,variable=t)
Opc2.place(x=120,y=140)
Opc3=Radiobutton(raiz,text="Año",value=100,variable=t)
Opc3.place(x=200,y=140)
#Interes Simple
BotonIS=Button(raiz,text="Calcular Interes Simple",command=InteresSimple)
BotonIS.place(x=40,y=170,width=170,height=20)
TxtInteres=Label(raiz, text="Interes:",anchor=W)
TxtInteres.place(x=40,y=200,width=120,height=20)
RptaIS=Label(raiz, textvariable=Interes)
RptaIS.place(x=250,y=200,width=150,height=20)
#Interes Compuesto
BotonIC=Button(raiz,text="Calcular Interes Compuesto",command=InteresCompuesto)
BotonIC.place(x=220,y=170,width=170,height=20)
RptaIC=Label(raiz, textvariable=Interes)
RptaIC.place(x=250,y=200,width=150,height=20)
#Valor Futuro
TxtVF=Label(raiz, text="Valor Futuro:",anchor=W)
TxtVF.place(x=40,y=230,width=120,height=20)
RptaVF=Label(raiz, textvariable=F)
RptaVF.place(x=250,y=230,width=150,height=20)

#TABLA DE AMORTIZACION#

#TITULO2
TIT2=Label(raiz, text="TABLAS DE AMORTIZACION",bg="#FFFFFF")
TIT2.place(x=110,y=280,width=200,height=20)
#Prestamo
TxtPrestamo=Label(raiz, text="Préstamo:",anchor=W)
TxtPrestamo.place(x=40,y=310,width=120,height=20)
Prest=Entry(raiz)
Prest.place(x=250,y=310,width=150,height=20)
#TEA
TxtTEA=Label(raiz, text="Taza efectiva Anual(TEA):",anchor=W)
TxtTEA.place(x=40,y=340,width=150,height=20)
TEA=Entry(raiz)
TEA.place(x=250,y=340,width=150,height=20)
#Periodo/s
TxtTiempo=Label(raiz, text="Periodos",anchor=W)
TxtTiempo.place(x=40,y=370,width=120,height=20)
n_per=Entry(raiz)
n_per.place(x=250,y=370,width=150,height=20)
#SISTEMA FRANCES
BotonTAF=Button(raiz,text="Sistema Francés",command=TablaAmortizacionFrances)
BotonTAF.place(x=40,y=400,width=120,height=20)
#SISTEMA ALEMAN
BotonTAF=Button(raiz,text="Sistema Alemán",command=TablaAmortizacionAleman)
BotonTAF.place(x=170,y=400,width=120,height=20)
#SISTEMA AMERICANO
BotonTAF=Button(raiz,text="Sistema Americano",command=TablaAmortizacionAmericano)
BotonTAF.place(x=300,y=400,width=120,height=20)
#FIN
raiz.mainloop()
