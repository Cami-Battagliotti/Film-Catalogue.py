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
        Devuelve: Un mesaje informando si el catalogo existe o no.
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


    def removeFilm(self, filmName):

        '''
        Función que elimina el film ingresado por el usuario en un catalogo indicado.
        Parámetros:
            name: Es el nombre del catalogo (nombrado segun el genero).
            filmName: Es un string con el nombre del film a eliminar.
            path: Es la ruta al archivo.
        Devuelve: Un mesaje informando si el film fue eliminado o si ha habido algún problema.
        '''
        
        try:
            f = open(self.path, 'r')
        except FileNotFoundError:
             print('❌ The catalogue does not exist')
        else:
            allFilms = f.readlines()
            f.close()

            filmsList = []
            for line in allFilms:           
                if filmName not in line:
                    filmsList.append(line)

            with open(self.path, 'w') as f:
                f.writelines(filmsList)

            if filmName in line:
                print(f'\nThe film "{filmName}" has been deleted from the catalogue {self.name}✅')
            else:
                print('\n❌ The entered film does not exist in our database.')


    def createCatalogue(self):
        '''
        Función que crea un catalogo vacío para guardar una lista de peliculas.
        Parámetros: 
            path: Es la ruta del nuevo catalogo.
            name: Nombre del nuevo catalogo.
        Devuelve: Un mesaje informando sobre si el catalogo se ha creado correctamente o si ya existia.
        '''
        if os.path.isfile(self.path):
            print(f'\n❌ The catalogue "{self.name}" already exists.')
        else:
            with open(self.path, mode="w") as f:
                f.write(f'Catalogue of {self.name} films:\n')
            print(f'\nA new catalogue of films "{self.name}" has been successfully created✅') 




#Bienvenida y muestra del menu de opciones
def show_menu():
    print(
    '\n**************************'
    '\nMenu of available options:\n'
    '\n1) Add a film ➕\n'
    '2) Listing films 📃\n'
    '3) Remove a film ➖\n'
    '4) Remove the complete catalogue 💀\n'
    '5) Create a new Catalogue 🆕\n'
    '6) Exit👋\n'
    )


def main():

    '''
    Función que lanza la aplicación para la gestión del catalogo de peliculas.
    '''
    print('\n**************************\n'
          '\n😊 WELCOME !!😊\n'
          '🎬 We have a few film catalogues available for you 🎬')

    while True:
        
        '''
        Bucle que muestra el menu y solicita al usuario la seleccion de una opcion, ejecutando la aplicacion mientras que la opcion 6 (Exit) no sea ingresada y devolviendo un mensaje de error si la opcion ingresada no esta en el menu.
        '''
        show_menu()

        option = input('\nPlease select an option from the list (only number): ')

        if option == '6':
            print('\nSuccessful programme Exit ✅\n')
            break

        elif option not in ['1','2','3','4','5']:
            (print('\nERROR ❌ Please check the menu again and introduce a valid option:'))

        else: 
            genre = input('\nPlease state the Genre: ').capitalize()
            path = f'Catalogue/{genre}.txt'
            catalogue = FilmCatalogue(genre, path)
            
            if option == '1':
                '''
                Solicita nombre del catalogo sobre el que desea trabajar, establece la ruta del mismo y, si existe, crea un objeto Film con los datos ingresados por el usuario que sera el que utilice el metodo "addFilm" para agregarlo a ese catalogo especifico. Devuelve un mensaje de error si el catalogo ingresado no existe.
                '''
                if os.path.exists(path):
                    
                    newFilmName = input('Please indicate the Name of the film: ').capitalize()
                    newFilmDirector = input('Please indicate the Director of the film: ').capitalize()
                    newFilmYear = input('Please indicate the Year of release: ')
                    film = Film(newFilmName, newFilmDirector, newFilmYear)

                    catalogue.addFilm(film)

                else: 
                    print('\n❌ The file does not exist. Please try another one')

            elif option == '2':
                catalogue.listFilms()

            elif option == '3':
                titleToRemove = input('Please state the Title of the film you want to remove: ').capitalize()

                catalogue.removeFilm(titleToRemove)

            elif option == '4':
                catalogue.removeCatalogue()

            elif option == '5':
                catalogue.createCatalogue()

                


main()