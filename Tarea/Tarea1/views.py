from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
import requests
from Tarea1.modulo import lista_episodios, info_episodio, lista_personajes, nombre_personaje, info_personaje, info_lugar

caps = lista_episodios()
#personajes = lista_personajes()

def principal(request): #Primera vista 

    doc_externo=open('Tarea1/p_capitulos.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"capitulos":caps})
    document=plt.render(ctx)

    return HttpResponse(document)


def episodios(request ,numero):

    episodio = info_episodio(numero)
    episodio["personajes"] = []
    for personaje in episodio["characters"]:
        episodio["personajes"].append(nombre_personaje(personaje))

    doc_externo=open('Tarea1/p_episodio.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"episodio":episodio})
    document=plt.render(ctx)

    return HttpResponse(document)


def personaje(requests, numero):

    character = info_personaje(numero)
    character["episodes"] = []
    for episodio in character["episode"]:
        character["episodes"].append(nombre_personaje(episodio))

    character["nombre_location"] = nombre_personaje(character["location"]["url"])
    character["nombre_origin"] = nombre_personaje(character["origin"]["url"])

    doc_externo=open('Tarea1/p_personaje.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"personaje":character})
    document=plt.render(ctx)

    return HttpResponse(document)


def location(requests, numero):

    location = info_lugar(numero)
    location["residentes"] = []
    for personaje in location["residents"]:
        location["residentes"].append(nombre_personaje(personaje))

    doc_externo=open('Tarea1/p_location.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"lugar":location})
    document=plt.render(ctx)

    return HttpResponse(document)