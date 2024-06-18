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

        def addFilm(self, filmToAdd):
            self.film = filmToAdd

            '''
            Función que agrega el film ingresado por el usuario en un catalogo indicado.
            Parámetros:
                name: Es el nombre del catalogo (nombrado segun el genero).
                film: Es un string con los datos del film a agregar.
                path: Es la ruta al archivo.
            Devuelve: Un mesaje informando si el film fue agregado o ha habido algún problema.
            '''

            try:
                f = open(self.path,'a')             
            except FileNotFoundError:
                print(f'\n❌ The catalogue "{self.name}" does not exist\n')
            else:
                f.write(f"\n{self.film}")
                f.close()
                print(f'\nThe {self.film} has been added✅')


    def listFilms(self):

        '''
        Función que muestra los films presentes en un catalogo indicado.
        Parámetros:
            name: Es el nombre del catalogo (nombrado segun el genero).
            path: Es la ruta al archivo.
        Devuelve:
            Un mesaje informando si el catalogo existe o no.
        '''

        try:
            f = open(self.path,'r')
        except FileNotFoundError:
            print(f'\n❌ The catalogue "{self.name}" does not exist\n')
        else:
            print('\n')
            print(f.read())
            f.close()


    def removeCatalogue(self):

        '''
        Función que elimina un catalogo indicado.
        Parámetros:
            name: Es el nombre del catalogo (nombrado segun el genero).
            path: Es la ruta al archivo.
        Devuelve: Un mesaje informando si el catalogo fue removido exitosamente o si hubo algun problema.
        '''
        
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f'\nThe catalogue "{self.name}" has been removed✅')
        else: 
            print('\n❌ The file does not exist.')

    

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


def main():

    '''
    Función que lanza la aplicación para la gestión del catalogo de peliculas.
    '''
    print('\n**************************\n'
          '\nWELCOME !!😊\n'
          '🎬 We have a few film catalogues available for you 🎬')

    while True:
        
        '''
        Bucle que muestra el menu y solicita al usuario la seleccion de una opcion, ejecutando la aplicacion mientras que la opcion 5 (Exit) no sea ingresada.
        '''
        show_menu()

        option = input('\nPlease select an option from the list (only number): ')

        if option == '5':
            print('\nSuccessful programme Exit ✅\n')
            break


main()