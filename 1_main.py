import streamlit as st

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
	page_title="Projet 2 – Cinéma Creuse",
	layout="wide"
)

# -----------------------------
# TITRE
# -----------------------------
st.markdown("### 📍 Le département de la Creuse 🐄")
st.markdown("**115 995 habitants en 2020**  \n📉 Population en diminution")
st.markdown("---")

# =============================
# DATA
# =============================

# Répartition par âge (INSEE – valeurs arrondies)
age_data = pd.DataFrame({
	"Tranche d'âge": [
    	"0-14 ans",
    	"15-29 ans",
    	"30-44 ans",
    	"45-59 ans",
    	"60-74 ans",
    	"75 ans ou plus"
	],
	"Pourcentage": [13, 12, 14, 21, 25, 15]
})

# Evolution population Creuse (INSEE)
pop_data = pd.DataFrame({
	"Année": [
    	2006, 2007, 2008, 2009, 2010,
    	2011, 2012, 2013, 2014, 2015,
    	2016, 2017, 2018, 2019, 2020
	],
	"Population": [
    	123500, 123900, 124100, 123700, 123000,
    	122400, 121300, 120700, 120400, 120100,
    	119100, 118300, 117100, 116300, 115995
	]
})

# =============================
# LAYOUT
# =============================

col_left, col_right = st.columns([2, 1])

# -----------------------------
# TEXTE + CAMEMBERT
# -----------------------------
with col_right:
	st.markdown("**58 ans en 2020**  \nÂge médian")
	
	fig_pie, ax_pie = plt.subplots()
	ax_pie.pie(
    	age_data["Pourcentage"],
    	labels=age_data["Tranche d'âge"],
    	autopct="%1.0f%%",
    	startangle=90
	)
	ax_pie.axis("equal")
	st.pyplot(fig_pie)

# -----------------------------
# COURBE POPULATION
# -----------------------------
with col_left:
	st.markdown("### Évolution du nombre d’habitants")

	fig_line, ax_line = plt.subplots()
	ax_line.plot(
    	pop_data["Année"],
    	pop_data["Population"],
    	marker="o"
	)

	ax_line.set_xlabel("Année")
	ax_line.set_ylabel("Population")
	ax_line.grid(True)

	st.pyplot(fig_line)

# -----------------------------
# SOURCES
# -----------------------------
st.markdown(
	"""
*Sources :* 
INSEE – Recensement de la population 
CNC – Géographie du cinéma
"""
)

