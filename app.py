import streamlit as st
import requests

# Set the title of the web app
st.title("Interactive Pokedex 🔴⚪")

# Create a text input for the user to search a Pokemon
pokemon_name = st.text_input("Enter a Pokemon name:", "pikachu").strip().lower()

# The specific URL to fetch the live Pokemon data
api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

# Fetch the data when a user types a name
if pokemon_name:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract the official artwork URL and display the image
        image_url = data['sprites']['other']['official-artwork']['front_default']
        st.image(image_url, width=250)
        
        # Display Name
        st.subheader(f"Name: {data['name'].capitalize()}")
        
        # Extract and display Types
        pokemon_types = []
        for t in data['types']:
            pokemon_types.append(t['type']['name'].capitalize())
        st.write(f"**Type:** {', '.join(pokemon_types)}")
        
        # Extract and display Powers (Abilities)
        pokemon_abilities = []
        for a in data['abilities']:
            pokemon_abilities.append(a['ability']['name'].capitalize())
        st.write(f"**Powers (Abilities):** {', '.join(pokemon_abilities)}")
        
    else:
        st.error("Pokemon not found! Check the spelling and try again.")