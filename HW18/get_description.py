import xml.etree.ElementTree as ET


def get_description(title):
    '''
    Function return description of movie by title
    :param title: title (name) of movie
    :return: description
    '''
    tree = ET.parse('movies.xml')
    root = tree.getroot()
    film = root.find(f"./genre/decade/movie[@title=\"{title}\"]/description")
    return film.text


name_of_film = "Ferris Bueller's Day Off"
movie_description = get_description(name_of_film)
print(movie_description)
