import requests

def obtener_pokemon():
    nombre = input("Ingresa el nombre del pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        nombre_pokemon = datos["name"].capitalize()
        altura = datos["height"] / 10
        peso = datos["weight"] / 10
        numero_pokedex = datos["id"]
        
        tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
        habilidades = [hab["ability"]["name"].capitalize() for hab in datos["habilidades"]]
        
        print("\n📖 POKEDEX")
        print(f"🔡 Numero: {numero_pokedex}")
        print(f"🐉 Nombre: {nombre_pokemon}")
        print(f"📏 Altura: {altura} metros")
        print(f"⚖ Peso: {peso} kg")
        print(f"🔥 Tipo(s): {','.join(tipos)}")
        print(f"💡 Habilidades: {','.join(habilidades)}")
        
    except requests.exceptions.HTTPError:
        print("❌ Pokemon no encontrado. Intenta de nuevo")
    except requests.exceptions.RequestException:
        print("❌ Error de conexion con la api.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

obtener_pokemon()