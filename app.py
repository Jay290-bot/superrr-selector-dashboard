
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SupeRR Selector",
    page_icon="🏏",
    layout="wide"
)

BATTERS = [
    [1,"Hardik Pandya",0.830,18.464,6.030,0.070,264,27,264,0.725],
    [2,"Rahul Tewatia",0.799,19.400,6.246,-0.205,286,32,238,0.704],
    [3,"Dasun Shanaka",0.706,14.151,2.582,1.619,324,33,227,0.694],
    [4,"Mohammad Nabi",0.690,14.733,4.167,0.687,264,22,233,0.700],
    [5,"Nicholas Pooran",0.602,16.743,3.689,0.048,230,18,230,0.697],
    [6,"Jimmy Neesham",0.487,27.512,4.387,-2.396,202,21,202,0.669],
    [7,"Azmatullah Omarzai",0.377,7.557,1.732,0.703,301,24,232,0.699],
    [8,"Shivam Dube",0.178,5.553,2.547,-0.860,424,38,419,0.807],
    [9,"Ayush Badoni",0.115,7.824,-0.641,-0.013,274,22,223,0.690],
    [10,"Shimron Hetmyer",0.095,7.198,0.759,-0.751,350,33,350,0.778]
]

BOWLERS = [
    [1,"Ravi Bishnoi",1.364,0.159,1.169,-4.125,3.482,1842,109,420,0.808],
    [2,"Prasidh Krishna",0.952,0.053,1.377,-6.273,3.684,882,50,200,0.667],
    [3,"Rashid Khan",0.651,-0.072,-0.097,-6.172,-0.609,2091,116,544,0.845],
    [4,"Maheesh Theekshana",0.608,-0.068,-0.247,-5.224,-1.277,1855,98,380,0.792],
    [5,"Adil Rashid",0.584,0.057,-1.568,-10.223,4.159,1032,60,242,0.708],
    [6,"Romario Shepherd",0.485,-0.111,0.050,-7.413,-1.654,1190,83,344,0.775],
    [7,"Mitchell Santner",0.454,-0.192,1.332,-7.993,-3.008,1376,80,330,0.767],
    [8,"Wanindu Hasaranga",0.433,-0.112,-0.300,-9.189,-0.184,1623,87,353,0.779],
    [9,"Hardik Pandya",0.417,-0.208,0.818,-2.680,-5.013,1547,110,221,0.688],
    [10,"Matheesha Pathirana",0.341,-0.194,0.455,-6.954,-3.705,673,47,290,0.744]
]

bat = pd.DataFrame(BATTERS, columns=[
    "Rank","Player","Score","SR Advantage",
    "Boundary Advantage","Dismissal Advantage",
    "Pressure Balls","Pressure Matches",
    "Common Phase Balls","Reliability"
])

bowl = pd.DataFrame(BOWLERS, columns=[
    "Rank","Player","Score","Economy Advantage",
    "Wicket Advantage","Dot Advantage",
    "Boundary Concession Advantage",
    "Challenge Balls","Challenge Matches",
    "Common Phase Balls","Reliability"
])

st.title("🏏 SupeRR Selector")
st.subheader("Pressure Performance Analytics")
st.caption("Rajasthan Royals | IPL 2027 Player Shortlisting")

a,b,c = st.columns(3)
a.metric("Top batters","10")
b.metric("Top bowlers","10")
c.metric("Eligibility","Strict-50")

st.divider()

tab1,tab2,tab3 = st.tabs([
    "🏏 Batters",
    "🎯 Bowlers",
    "📊 Methodology"
])

with tab1:
    st.header("Top 10 Batters Under Pressure")
    st.write(
        "Pressure means the batting team had five or fewer "
        "wickets in hand before the delivery."
    )
    st.dataframe(bat, use_container_width=True, hide_index=True)

    player = st.selectbox("Explore batter",bat["Player"])
    p = bat[bat["Player"] == player].iloc[0]

    st.subheader(player)
    x,y,z = st.columns(3)
    x.metric("Composite Score",f'{p["Score"]:.3f}')
    y.metric("Pressure Balls",int(p["Pressure Balls"]))
    z.metric("Reliability",f'{p["Reliability"]:.3f}')

    st.bar_chart(
        pd.DataFrame({
            "Advantage":[
                p["SR Advantage"],
                p["Boundary Advantage"],
                p["Dismissal Advantage"]
            ]
        },index=["Strike rate","Boundary rate","Dismissal rate"])
    )

with tab2:
    st.header("Top 10 Bowlers in Challenge Context")
    st.write(
        "Challenge context means the batting team had six or "
        "more wickets in hand before the delivery."
    )
    st.dataframe(bowl,use_container_width=True,hide_index=True)

    player = st.selectbox("Explore bowler",bowl["Player"])
    p = bowl[bowl["Player"] == player].iloc[0]

    st.subheader(player)
    x,y,z = st.columns(3)
    x.metric("Composite Score",f'{p["Score"]:.3f}')
    y.metric("Challenge Balls",int(p["Challenge Balls"]))
    z.metric("Reliability",f'{p["Reliability"]:.3f}')

    st.bar_chart(
        pd.DataFrame({
            "Advantage":[
                p["Economy Advantage"],
                p["Wicket Advantage"],
                p["Dot Advantage"],
                p["Boundary Concession Advantage"]
            ]
        },index=["Economy","Wickets","Dot balls","Boundary control"])
    )

with tab3:
    st.header("Research Methodology")

    st.subheader("Dataset")
    st.write("""
    - 837 matches: 367 IPL and 470 T20I.
    - 193,988 ball-by-ball delivery rows.
    - Dataset period: January 2022 to November 2026.
    """)

    st.subheader("Eligibility: Strict-50")
    st.write("""
    - Minimum 150 balls in each comparison state.
    - Minimum 10 distinct matches in each state.
    - Minimum 50 balls per state in each counted phase.
    - Minimum 200 common phase balls overall.
    - At least two comparable phases.
    """)

    st.subheader("Scoring weights")

    st.write("**Batters**")
    st.write("""
    - Strike-rate advantage: 40%
    - Boundary-ball percentage advantage: 30%
    - Dismissal-rate advantage: 30%
    """)

    st.write("**Bowlers**")
    st.write("""
    - Economy advantage: 40%
    - Wicket advantage: 30%
    - Dot-ball advantage: 15%
    - Boundary-concession advantage: 15%
    """)

    st.subheader("Reliability adjustment")
    st.latex(r"R = \\frac{Common\\ Phase\\ Balls}{Common\\ Phase\\ Balls+100}")

    st.latex(r"Final\\ Score = Weighted\\ Z\\ Score \\times R")

    st.warning("""
    Important limitations:
    - Scores are relative to the eligible player pool.
    - A positive composite does not mean every raw metric improved.
    - Bowling runs use a provisional delivery-level attribution proxy.
    - DLS and required run rate were not included.
    - Holdout checks were inconclusive; predictive accuracy is not claimed.
    - Historical performance does not guarantee IPL 2027 performance.
    """)

st.divider()
st.caption(
    "SupeRR Selector | Research-driven cricket analytics | "
    "Prepared for Rajasthan Royals hackathon"
)
