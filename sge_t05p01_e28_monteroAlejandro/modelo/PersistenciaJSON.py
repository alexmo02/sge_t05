import json
from modelo.ClubModulo import Club

class Persistencia:
    def __init__(self) -> None:
        pass

    def prepararDictSocio(c):
        dictPrep=c.__dict__.copy()
        dictPrep["_usuarioAsociado"]=c._usuarioAsociado._dni
        listaUsuariosAux=list()
        
        try:
            for i in dictPrep["_bicicletas"]:
                lista=[]
                try:
                    for e in i._listaReparaciones:
                        lista.append(e.__dict__)
                        i.__dict__["_listaReparaciones"]=lista
                except:
                    continue
                listaUsuariosAux.append(i.__dict__)
                
                dictPrep["_bicicletas"]=listaUsuariosAux
        except:
            dictPrep["_bicicletas"]=listaUsuariosAux
            
        return dictPrep

    def prepararDictClub(c):
        dictPrep=c.copy()
        dictPrep["_diccSocios"]={}
        dictPrep["_listaEventos"]=[]
        dictPrep["_diccUsuarios"]={}
        
        return dictPrep

    def guardarDatos(club):
        #USUARIOS
        listaUsuariosAux=list()
        for i in club._diccUsuarios.values():
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONUsuarios("usuario.json", listaUsuariosAux)
        del listaUsuariosAux

        #SOCIOS
        listaUsuariosAux=list()
        for e in club._diccSocios.values():
            socio=e
            listaUsuariosAux.append(socio)       

        colAux=list()
        for c in listaUsuariosAux:
            colAux.append(Persistencia.prepararDictSocio(c)) #Looping Using List 
        Club.guardarJSONSocios("socio.json", colAux)

        #CLUB
        colAux=list()
        colAux.append(Persistencia.prepararDictClub(club.__dict__))

        Club.guardarJSONClub("club.json", colAux )
        
        #EVENTOS
        listaUsuariosAux=list()
        for i in club._listaEventos:
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONEventos("evento.json", listaUsuariosAux)
        del listaUsuariosAux