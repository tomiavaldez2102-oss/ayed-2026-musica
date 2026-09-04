class Cancion:
    def __init__(self, id_cancion, titulo, artista):
        self.id = id_cancion
        self.titulo = titulo
        self.artista =artista
CATALOGO =[
    Cancion(1, 'De musica ligera','Soda Stereo'),
    Cancion(2, 'Persiana Americana', 'Soda Stereo'),
    Cancion(3, 'Flaca','Andres Calamaro')
]

def listar_catalogo():
    print('\n-CATALOGO MUSICAL---')
    for c in CATALOGO:
        print(f'{c.id}. {c. titulo} - {c.artista}')






