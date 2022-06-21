from urllib import response
import pypokedex # Biblioteca onde contém informação dos pokemons.
import PIL.Image, PIL.ImageTk # Biblioteca Pillow, usada para manipulação de imagens.
import tkinter as tk # Biblioteca de interface gráfica.
import urllib3 # Biblioteca para manipulação de URL.
from io import BytesIO # Biblioteca onde lida com entradas e saidas.

# Montando a janela
window = tk.Tk()
window.geometry('1080x800')
window.title('Pokedex')
window.config(padx=10, pady=10)

title_label = tk.Label(window, text = 'Pokedex')
title_label.config(font=('Arial', 32))
title_label.pack(padx=10, pady=10)

# Inserindo as informações que aparecerá
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=('Arial', 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_name = tk.Label(window)
pokemon_name.config(font=('Arial', 20))
pokemon_name.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=('Arial', 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_hp = tk.Label(window)
pokemon_hp.config(font=('Arial', 20))
pokemon_hp.pack(padx=10, pady=10)

pokemon_atk = tk.Label(window)
pokemon_atk.config(font=('Arial', 20))
pokemon_atk.pack(padx=10, pady=10)

pokemon_def = tk.Label(window)
pokemon_def.config(font=('Arial', 20))
pokemon_def.pack(padx=10, pady=10)



# Funções que aparecerão na tela
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, 'end-1c'))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f'Nº {pokemon.dex}')
    pokemon_name.config(text=f'Name: {pokemon.name}'.title())
    pokemon_types.config(text=f" - ".join([t for t in pokemon.types]).title())
    pokemon_hp.config(text=f'HP: {pokemon.base_stats.hp}')
    pokemon_atk.config(text=f'ATK: {pokemon.base_stats.attack}')
    pokemon_def.config(text=f'DEF: {pokemon.base_stats.defense}')



label_id_name = tk.Label(window, text='Id ou nome')
label_id_name.config(font=('Arial', 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=('Arial', 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text='Carregar Pokemon', command=load_pokemon)
btn_load.config(font=('Arial', 20))
btn_load.pack(padx=10, pady=10)


window.mainloop()
