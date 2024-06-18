import os

class Film:

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.__year = year

    @property
    def year(self):
        '''
        Metodo que permite visualizar el atributo privado "year", y el decorador @property permite acceder a este como un atributo normal. Devuelve el atributo privado "year".
        '''
        return self.__year
    
    def __str__(self):
        '''
        Metodo que representa el objeto de la clase como una cadena(string) posible de ser leida por el humano. 
        Parametros: atributos de la clase almacenados en una lista.
        Devuelve: una cadena con los atributos.
        '''
        listData = [self.title, self.director, self.year]
        return f'Film: {listData}'
    

    class FilmCatalogue:

        def __init__(self, catalogueName, filePath):
            self.name = catalogueName
            self.path = filePath
    

    #Bienvenida y muestra del menu de opciones
def show_menu():
    print(
    '\n**************************'
    '\nMenu of available options:\n'
    '\n1) Add a film ➕\n'
    '2) Listing films 📃\n'
    '3) Remove a film ➖\n'
    '4) Remove the complete catalogue 💀\n'
    '5) Exit👋\n'
    )