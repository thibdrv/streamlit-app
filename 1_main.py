import streamlit as st

# ---------------------
# Configuration générale
# ---------------------
st.set_page_config(
	page_title="Étude de marché – Cinéma en Creuse",
	layout="wide"
)

# ---------------------
# TITRE
# ---------------------
st.title("🎬 Étude de marché – Consommation de cinéma")
st.subheader("Département de la Creuse (23)")

st.markdown("---")

# ---------------------
# KPIs (comme sur ton lien)
# ---------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
	st.metric(
    	label="Population (2022)",
    	value="115 529"
	)

with col2:
	st.metric(
    	label="Densité (hab/km²)",
    	value="20,8"
	)

with col3:
	st.metric(
    	label="Part des +60 ans",
    	value="39 %"
	)

with col4:
	st.metric(
    	label="Cinémas",
    	value="Peu équipés",
    	delta="Sous la moyenne nationale"
	)

st.markdown("---")

# ---------------------
# SECTION 1 – Démographie
# ---------------------
st.header("👥 Contexte démographique (INSEE)")

st.markdown(
	"""
La Creuse est un département rural à **faible densité de population**.
La population diminue régulièrement depuis plusieurs décennies et se caractérise
par un **vieillissement marqué**.

- Population totale : **115 529 habitants**
- Densité : **20,8 habitants/km²**
- **39 % des habitants ont 60 ans ou plus**
- Seulement **25 % ont moins de 30 ans**
"""
)

# ---------------------
# SECTION 2 – Équipement cinéma
# ---------------------
st.header("🎞️ Équipement cinématographique (CNC)")

st.markdown(
	"""
Selon le CNC, la Creuse fait partie des départements **les moins bien équipés en salles de cinéma**.

Caractéristiques principales :
- Peu d'établissements
- Salles de **petite capacité**
- Cinémas majoritairement **Art et Essai**
- Implantation concentrée dans quelques villes (Guéret, La Souterraine, Aubusson)
- **Absence de multiplexe**
"""
)

# ---------------------
# SECTION 3 – Fréquentation
# ---------------------
st.header("📉 Fréquentation des salles (CNC)")

st.markdown(
	"""
La fréquentation des salles est **inférieure à la moyenne nationale**, ce qui est
caractéristique des territoires ruraux peu denses.

La consommation de cinéma dépend fortement :
- de la **distance aux salles**
- de la **taille des établissements**
- de la diversité de la programmation

La pratique est donc **occasionnelle**, et fortement conditionnée par l’offre locale.
"""
)

# ---------------------
# SECTION 4 – Pratiques culturelles
# ---------------------
st.header("🎭 Pratiques culturelles (INSEE)")

st.markdown(
	"""
À l’échelle nationale :
- **40 % des Français** vont au cinéma au moins une fois par an
- Cette proportion est **plus faible chez les populations âgées et rurales**

Les principales raisons de non‑fréquentation :
- Manque d’intérêt
- Éloignement géographique
- Contraintes financières secondaires
"""
)

# ---------------------
# SECTION SYNTHESE
# ---------------------
st.header("✅ Synthèse marché")

st.success(
	"""
Le marché du cinéma dans la Creuse est :
- de **petite taille**
- contraint par la **démographie**
- limité par l’**offre d’équipements**

Les salles jouent un rôle **culturel et social essentiel**, davantage qu’un rôle de
loisir de masse.
"""
)

# ---------------------
# SOURCES
# ---------------------
st.markdown("---")
st.caption(
	"Sources : INSEE (dossier département Creuse), CNC (Géographie du cinéma, équipements et fréquentation)"
)
