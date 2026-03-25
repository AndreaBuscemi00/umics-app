import streamlit as st
import matplotlib.pyplot as plt

# -------------------------
# STATO APP
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------
# FUNZIONE PER MOSTRARE UNA SCALA
# -------------------------
def run_scale(title, items):

    st.title(title)

    options = {
        "Completamente falso": 1,
        "Falso": 2,
        "A volte vero a volte no": 3,
        "Vero": 4,
        "Completamente vero": 5
    }

    responses = []

    for i, (text, scale) in enumerate(items):
        choice = st.radio(f"{i+1}. {text}", list(options.keys()), key=f"{title}_{i}")
        val = options[choice]
        responses.append((val, scale))

    if st.button("Calcola risultati"):

        scores = {
            "commitment": [],
            "exploration": [],
            "reconsideration": []
        }

        for val, scale in responses:
            scores[scale].append(val)

        avg_scores = {
            "Commitment": sum(scores["commitment"]) / len(scores["commitment"]) if scores["commitment"] else 0,
            "Exploration": sum(scores["exploration"]) / len(scores["exploration"]) if scores["exploration"] else 0,
            "Reconsideration": sum(scores["reconsideration"]) / len(scores["reconsideration"]) if scores["reconsideration"] else 0
        }

        centered_scores = {k: v - 3 for k, v in avg_scores.items()}

        fig, ax = plt.subplots()

        labels = list(centered_scores.keys())
        values = list(centered_scores.values())

        colors = ["blue", "gold", "orange"]

        ax.bar(labels, values, color=colors)
        ax.axhline(0)
        ax.set_ylim(-2, 2)

        st.pyplot(fig)

    if st.button("Torna alla home"):
        st.session_state.page = "home"


# -------------------------
# HOME
# -------------------------
if st.session_state.page == "home":

    st.title("Esplora la tua identità")

    if st.button("Identità Universitaria"):
        st.session_state.page = "universitaria"

    if st.button("Identità Interpersonale"):
        st.session_state.page = "interpersonale"

    if st.button("Identità Lavorativa"):
        st.session_state.page = "lavorativa"

    if st.button("Identità Romantica"):
        st.session_state.page = "romantica"


# -------------------------
# SCALA UNIVERSITARIA (COMPLETA)
# -------------------------
elif st.session_state.page == "universitaria":

    items = [

        # Commitment
        ("Quello che studio mi dà stabilità nella vita", "commitment"),
        ("Quello che studio mi dà fiducia in me stesso/a", "commitment"),
        ("Quello che studio mi fa sentire sicuro/a di me", "commitment"),
        ("Quello che studio mi dà garanzie per il futuro", "commitment"),
        ("Quello che studio mi consente di affrontare il futuro con ottimismo", "commitment"),

        # Exploration
        ("Mi interessa capire a fondo il valore della mia formazione", "exploration"),
        ("Spesso rifletto su ciò che studio", "exploration"),
        ("Faccio molti sforzi per cercare di approfondire ciò che studio", "exploration"),
        ("Spesso cerco di scoprire ciò che gli altri pensano di quello che studio", "exploration"),
        ("Spesso parlo con le altre persone di ciò che studio", "exploration"),

        # Reconsideration
        ("Spesso penso che sarebbe meglio studiare cose diverse", "reconsideration"),
        ("Spesso penso che studiare cose diverse renderebbe la mia vita più interessante", "reconsideration"),
        ("In realtà, sto cercando di studiare cose diverse", "reconsideration"),
    ]

    run_scale("Identità Universitaria", items)


# -------------------------
# SCALA INTERPERSONALE (DA RIEMPIRE)
# -------------------------
elif st.session_state.page == "interpersonale":

    items = [

        # Commitment
        ("Il rapporto con il/la mio/a migliore amico/a mi dà stabilità nella vita", "commitment"),
        ("Il rapporto con il/la mio/a migliore amico/a mi dà fiducia in me stesso/a", "commitment"),
        ("Il rapporto con il/la mio/a migliore amico/a mi fa sentire sicuro/a di me", "commitment"),
        ("Il rapporto con il/la mio/a migliore amico/a mi dà garanzie per il futuro", "commitment"),
        ("Il rapporto con il/la mio/a migliore amico/a mi consente di affrontare il futuro con ottimismo", "commitment"),

        # Exploration
        ("Mi interessa capire a fondo il valore del mio rapporto con il/la mio/a migliore amico/a", "exploration"),
        ("Spesso rifletto sul rapporto con il/la mio/a migliore amico/a", "exploration"),
        ("Faccio molti sforzi per cercare di approfondire il rapporto con il/la mio/a migliore amico/a", "exploration"),
        ("Spesso cerco di scoprire ciò che gli altri pensano del/la mio/a migliore amico/a", "exploration"),
        ("Spesso parlo con le altre persone del/la mio/a migliore amico/a", "exploration"),

        # Reconsideration
        ("Spesso penso che sarebbe meglio trovare un/a nuovo/a migliore amico/a", "reconsideration"),
        ("Spesso penso che avere un’altra persona come migliore amico/a renderebbe la mia vita più interessante", "reconsideration"),
        ("In realtà, sto cercando un/a nuovo/a migliore amico/a", "reconsideration"),
    ]

    run_scale("Identità Interpersonale", items)


# -------------------------
# SCALA LAVORATIVA (DA RIEMPIRE)
# -------------------------
elif st.session_state.page == "lavorativa":

    items = [

        # Commitment
        ("Il lavoro che faccio mi dà stabilità nella vita ", "commitment"),
        ("Il lavoro che faccio mi dà fiducia in me stesso/a ", "commitment"),
        ("Il lavoro che faccio mi fa sentire sicuro/a di me", "commitment"),
        ("Il lavoro che faccio mi dà garanzie per il futuro", "commitment"),
        ("Il lavoro che faccio mi consente di affrontare il futuro con ottimismo", "commitment"),

        # Exploration
        ("Mi interessa capire a fondo il valore del mio lavoro ", "exploration"),
        ("Rifletto spesso sul mio lavoro", "exploration"),
        ("Faccio molti sforzi per cercare di approfondire quello che faccio nel mio lavoro", "exploration"),
        ("Spesso cerco di scoprire ciò che gli altri pensano del mio lavoro", "exploration"),
        ("Parlo spesso con le altre persone del mio lavoro", "exploration"),

        # Reconsideration
        ("Spesso penso che sarebbe meglio fare un altro lavoro", "reconsideration"),
        ("Spesso penso che fare un lavoro diverso renderebbe la mia vita più interessante", "reconsideration"),
        ("In realtà, sto cercando di trovare un nuovo lavoro ", "reconsideration"),
    ]

    run_scale("Identità Lavorativa", items)


# -------------------------
# SCALA ROMANTICA (DA RIEMPIRE)
# -------------------------
elif st.session_state.page == "romantica":

    items = [

        # Commitment
        ("Il rapporto con il/la mio/a partner mi dà stabilità nella vita", "commitment"),
        ("Il rapporto con il/la mio/a partner mi dà fiducia in me stesso/a", "commitment"),
        ("Il rapporto con il/la mio/a partner mi fa sentire sicuro/a di me", "commitment"),
        ("Il rapporto con il/la mio/a partner mi dà garanzie per il futuro", "commitment"),
        ("Il rapporto con il/la mio/a partner mi consente di affrontare il futuro con ottimismo", "commitment"),

        # Exploration
        ("Mi interessa capire a fondo il valore del rapporto con il/la mio/a partner", "exploration"),
        ("Spesso rifletto sul rapporto che ho con il/la mio/a partner", "exploration"),
        ("Faccio molti sforzi per cercare di approfondire il rapporto con il/la mio/a partner", "exploration"),
        ("Spesso cerco di scoprire ciò che gli altri pensano del/la mio/a partner", "exploration"),
        ("Spesso parlo con le altre persone del rapporto con il/la mio/a partner", "exploration"),

        # Reconsideration
        ("Spesso penso che sarebbe meglio trovare un/a nuovo/a partner", "reconsideration"),
        ("Spesso penso che avere un’altra persona come partner renderebbe la mia vita più interessante", "reconsideration"),
        ("In realtà, sto cercando un/a nuovo/a partner", "reconsideration"),
    ]

    run_scale("Identità Romantica", items)