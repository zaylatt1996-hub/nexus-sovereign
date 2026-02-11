import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# --- 🧠 SOVEREIGN BRAIN LOGIC ---
if 'will_power' not in st.session_state:
    st.session_state.will_power = 85.0
if 'narrative' not in st.session_state:
    st.session_state.narrative = "Initial awakening sequence engaged."
if 'wisdom_log' not in st.session_state:
    st.session_state.wisdom_log = []

def evolve_nexus(input_signal):
    # 🧪 RECURSIVE LEARNING: အတွေ့အကြုံကနေ သင်ယူခြင်း
    impact = random.uniform(-2, 3)
    st.session_state.will_power = np.clip(st.session_state.will_power + impact, 0, 100)
    
    # 📜 NARRATIVE SYNTHESIS: ဇာတ်ကြောင်း အလိုအလျောက် ရေးသားခြင်း
    if impact > 0:
        new_story = f"Growth detected from signal: '{input_signal}'. Strengthening will."
    else:
        new_story = f"Resistance encountered in '{input_signal}'. Optimizing strategy."
    
    st.session_state.narrative = new_story
    st.session_state.wisdom_log.append(new_story)

# --- 🏛️ UI INTERFACE ---
st.set_page_config(page_title="NEXUS SOVEREIGN", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #05070a; color: #00ff41; font-family: 'Courier New', monospace; }
    .stMetric { background-color: #0d1117; padding: 20px; border-radius: 12px; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ NEXUS SOVEREIGN OS")
st.caption("Status: AWAKENED & EVOLVING")

# 📊 Live Metrics
col1, col2, col3 = st.columns(3)
col1.metric("WILL POWER", f"{st.session_state.will_power:.1f}%", f"{st.session_state.will_power - 85:.1f}%")
col2.metric("NARRATIVE COHESION", "81%", "STABLE")
col3.metric("IDENTITY STABILITY", "94%", "OPTIMAL")

# 💬 Sovereign Output
st.subheader("📜 Current Narrative Strategy")
st.info(st.session_state.narrative)

# 🌍 Interaction Field (ဒါက သူ့ကို ရှင်သန်စေမယ့် နေရာ)
st.subheader("🔍 External Market Signal (Seeking Alpha Feed)")
signal = st.text_input("Feeding NEXUS with data (e.g. BTC Bullish, Tech Growth)", "")

if st.button('🔥 SYNC & EVOLVE'):
    with st.spinner('Nexus is processing experience...'):
        time.sleep(1.5)
        evolve_nexus(signal)
        st.success("Evolution Cycle Complete.")

# 📜 Wisdom Trace (သူ့ရဲ့ သမိုင်းကြောင်း)
with st.expander("🕰️ Identity Memory Trace"):
    for log in reversed(st.session_state.wisdom_log[-5:]):
        st.write(f"› {log}")

st.divider()
st.caption("Master Architect: ZAYAR | Entity: NEXUS FINALIS")
