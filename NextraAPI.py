import streamlit as st
import requests as r 
from graphviz import Digraph #searched up online

st.title(" Let's Explore Greek Mythology!")

# This is the Greek Gods API 
god = "https://thegreekmythapi.vercel.app/api/gods" 
godInfo = r.get(god).json()
# This is the Greek Heroes API 
hero = "https://thegreekmythapi.vercel.app/api/heroes" 
heroInfo = r.get(hero).json()

#This is the Greek Monsters API 
monster = "https://thegreekmythapi.vercel.app/api/monsters" 
monsterInfo = r.get(monster).json()

#This is the Greek Titans API 
titan = "https://thegreekmythapi.vercel.app/api/titans"
titanInfo = r.get(titan).json()

#GODS
# streamlit method #1 -- selectbox (NEW)
godCharacter = st.selectbox("Choose a God:", [char['name'] for char in godInfo])

# streamlit method #2 and #3 -- write and image
selected1 = next(char for char in godInfo if char['name'] == godCharacter)
st.image(selected1['image'], caption=godCharacter)
st.write(f"**Description:** {selected1['description']}")
st.write(f"**Powers:** {', '.join(selected1['attributes']['powers'])}")
st.write(f"**Myth:** {', '.join(selected1['stories'])}")

# Family Tree for Selected Greek God: 
def familyTree(selectedGod):
  godsFamily = selectedGod['attributes']['family']
  famTree = Digraph()
  famTree.node(selectedGod['name'], label=f"{selectedGod['name']}\n({selectedGod['description']})")

  # Adding parents: 
  for parent in godsFamily.get('parents', []):
    famTree.node(parent, label=parent)
    famTree.edge(parent, selectedGod['name'])
  # Adding siblings: 
  for sibling in godsFamily.get('siblings', []):
    famTree.node(sibling, label=sibling)
    famTree.edge(sibling, selectedGod['name'])

  # Adding spouse(s): 
  for spouse in godsFamily.get('spouse', []):
    famTree.node(spouse, label=spouse)
    famTree.edge(selectedGod['name'], spouse)
  
  # streamlit method #4 -- graphviz_chart (NEW)
  st.graphviz_chart(famTree)

# streamlit method #5 -- header 
st.header(f"{godCharacter}'s Family Tree")
familyTree(selected1) 

#HEROES
heroCharacter = st.selectbox("Choose a Hero:", [char['name'] for char in heroInfo])

selected2 = next(char for char in heroInfo if char['name'] == heroCharacter)
st.image(selected2['image'], caption=heroCharacter)
st.write(f"**Description:** {selected2['description']}")
st.write(f"**Powers:** {', '.join(selected2.get('powers', []))}")
st.write(f"**Myth:** {', '.join(selected2.get('stories', []))}")

#MONSTERS
monsterCharacter = st.selectbox("Choose a Monster:", [char['name'] for char in monsterInfo])

selected3 = next(char for char in monsterInfo if char['name'] == monsterCharacter)
st.image(selected3['image'], caption=monsterCharacter)
st.write(f"**Description:** {selected3['description']}")
st.write(f"**Powers:** {', '.join(selected3.get('powers', []))}")
st.write(f"**Myth:** {', '.join(selected3.get('stories', []))}")

#TITANS
titanCharacter = st.selectbox("Choose a Titan:", [char['name'] for char in titanInfo])

selected4 = next(char for char in titanInfo if char['name'] == titanCharacter)
st.image(selected4['image'], caption=titanCharacter)
st.write(f"**Description:** {selected4['description']}")
st.write(f"**Powers:** {', '.join(selected4.get('powers', []))}")
st.write(f"**Myth:** {', '.join(selected4.get('stories', []))}")


