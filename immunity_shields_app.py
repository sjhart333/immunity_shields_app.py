# 🛡️ Cognitive Immunity Shields - Streamlit App

import streamlit as st

st.set_page_config(page_title="Cognitive Immunity Shields", layout="wide")

st.title("🛡️ Cognitive Immunity Shields")
st.markdown("""
Understand how psychological defenses, media conditioning, and identity-driven cognition
create immunity to contradictory information.
""")

# Tabs
tabs = st.tabs(["Shield Types", "Psychology", "Systemic Factors", "Penetration Strategies"])

# --- Shield Types Tab ---
with tabs[0]:
    shield_data = [
        {
            "name": "Epistemic Shield",
            "desc": "Only accepts info from 'trusted' sources",
            "penetrable": "Very Difficult",
            "mechanics": "Source credibility hierarchy overrides content evaluation",
            "examples": [
                "Fox News viewers dismissing CNN reports as 'fake news'",
                "QAnon followers only trusting 'Q drops'",
                "Academic echo chambers rejecting outside research"
            ],
            "counters": ["Peer-approved messengers", "Source diversification", "Insider defections"]
        },
        {
            "name": "Moral Inversion Shield",
            "desc": "Crimes reframed as virtue or necessity",
            "penetrable": "Moderate",
            "mechanics": "Ends justify means; persecution proves righteousness",
            "examples": [
                "January 6th as 'legitimate political discourse'",
                "Authoritarianism as 'defending democracy'"
            ],
            "counters": ["Appeal to values", "Highlight hypocrisy", "Show victims"]
        },
        {
            "name": "Tribal Identity Shield",
            "desc": "Loyalty trumps truth; leaving = betrayal",
            "penetrable": "Very Difficult",
            "mechanics": "Criticism of leader = attack on self",
            "examples": ["MAGA identity > policy views", "Party over personal values"],
            "counters": ["Create new identity", "Show in-group betrayal", "Offer belonging"]
        },
        {
            "name": "Victimhood Shield",
            "desc": "Any criticism = persecution",
            "penetrable": "Moderate",
            "mechanics": "Opposition proves righteousness",
            "examples": ["Indictments = 'witch hunt'", "Fact-checking = 'censorship'"],
            "counters": ["Show privilege", "Reframe as accountability"]
        },
        {
            "name": "Spiritual Shield",
            "desc": "Divine mandate immunizes criticism",
            "penetrable": "Extremely Difficult",
            "mechanics": "Questioning leader = questioning God",
            "examples": ["Trump as 'God's vessel'", "Prosperity gospel justification"],
            "counters": ["Religious counter-narratives", "Theological contradiction"]
        },
        {
            "name": "Distraction Shield",
            "desc": "Flood the zone so nothing sticks",
            "penetrable": "Moderate",
            "mechanics": "Overload prevents deep processing",
            "examples": ["Controversy cycles", "Firehose propaganda"],
            "counters": ["Clear timelines", "Pattern recognition"]
        },
        {
            "name": "Mockery Shield",
            "desc": "Deflect with humor/dismissal",
            "penetrable": "Moderate",
            "mechanics": "Serious becomes silly",
            "examples": ["'Liberal tears' memes", "'TDS' mockery"],
            "counters": ["Expose pain", "Use humor strategically"]
        }
    ]

    for shield in shield_data:
        with st.expander(f"{shield['name']} ({shield['penetrable']})"):
            st.write(shield["desc"])
            st.markdown(f"**Psychological Mechanics:** {shield['mechanics']}")
            st.markdown("**Examples:**")
            for ex in shield["examples"]:
                st.markdown(f"- {ex}")
            st.markdown("**Counters:**")
            for co in shield["counters"]:
                st.markdown(f"✅ {co}")

# --- Psychology Tab ---
with tabs[1]:
    st.header("🧠 Underlying Psychological Mechanisms")
    psych = [
        ("Cognitive Dissonance", "Minimize belief vs. reality conflict", "'Strategic ambiguity' rationalizations"),
        ("Confirmation Bias", "Seek confirming evidence", "Algorithm-driven reinforcement"),
        ("Motivated Reasoning", "Emotion-driven logic", "Elaborate excuses for failures"),
        ("Identity-Protective Cognition", "Reject facts threatening group membership", "Conservative scientists downplaying findings"),
        ("Social Proof Cascade", "Others' beliefs = evidence", "Rally crowd as 'proof' of election win")
    ]
    for name, desc, ex in psych:
        with st.container():
            st.subheader(name)
            st.write(desc)
            st.caption(f"Example: {ex}")

# --- Systemic Factors Tab ---
with tabs[2]:
    st.header("🌐 Systemic Factors Enabling Immunity")
    systems = {
        "Media Ecosystem": [
            "Partisan silos", "Social media algorithms", "Influencer pseudo-credibility", "Think tank laundering"
        ],
        "Economic Incentives": [
            "Outrage = profit", "Grift rewards loyalty", "Alt-facts as product"],
        "Social Structure": [
            "Low trust in institutions", "Polarization", "Class + education gaps"],
        "Political Design": [
            "Base mobilization over persuasion", "Gerrymandering", "Winner-take-all system"]
    }
    for category, items in systems.items():
        with st.expander(category):
            for item in items:
                st.markdown(f"- {item}")

# --- Strategies Tab ---
with tabs[3]:
    st.header("🔓 Penetration Strategies")
    strategies = {
        "Narrative Aikido": [
            "Redirect force", "Find contradictions", "Co-opt language"
        ],
        "Trusted Messenger": [
            "Use in-group validators", "Religious voices", "Law enforcement allies"
        ],
        "Emotional Resonance": [
            "Speak to dignity", "Address fear/anxiety", "Provide belonging"
        ],
        "Inoculation Theory": [
            "Expose manipulation tactics", "Build critical thinking", "Prebunk disinfo"]
    }
    for strat, items in strategies.items():
        with st.expander(strat):
            for technique in items:
                st.markdown(f"✅ {technique}")

    st.markdown("---")
    st.info("Facts alone don’t work — shields evolved to resist them. Emotional resonance and identity-safe approaches are key.")
