import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Fluid Mechanics Calculator", layout="centered")

# --- Mathematical Functions ---
def pressure(rho, g, h):
    return rho * g * h

def velocity(Q, A):
    return Q / A if A != 0 else 0

def discharge(A, V):
    return A * V

def reynolds_number(rho, V, D, mu):
    return (rho * V * D) / mu if mu != 0 else 0

def dynamic_pressure(rho, V):
    return 0.5 * rho * V ** 2

# --- UI Setup ---
st.title("🌊 Fluid Mechanics Calculator")
st.write("Select a calculation from the sidebar menu to get started.")

# Sidebar Navigation Menu
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Calculation:",
    [
        "Hydrostatic Pressure",
        "Fluid Velocity",
        "Discharge (Flow Rate)",
        "Reynolds Number",
        "Dynamic Pressure"
    ]
)

# --- Calculation Forms ---

if choice == "Hydrostatic Pressure":
    st.header("🪠 Hydrostatic Pressure Calculation")
    st.write("Formula: $P = \\rho \\cdot g \\cdot h$")
    
    # Input fields
    rho = st.number_input("Fluid Density ($\\rho$, kg/m³):", min_value=0.0, value=1000.0, step=10.0)
    g = st.number_input("Gravitational Acceleration ($g$, m/s²):", min_value=0.0, value=9.81, step=0.01)
    h = st.number_input("Height/Depth ($h$, m):", min_value=0.0, value=1.0, step=0.5)
    
    if st.button("Calculate Pressure"):
        P = pressure(rho, g, h)
        st.success(f"**Pressure (P)** = **{P:,.2f} Pa** (or {P/1000:.3f} kPa)")

elif choice == "Fluid Velocity":
    st.header("⚡ Fluid Velocity Calculation")
    st.write("Formula: $V = \\frac{Q}{A}$")
    
    Q = st.number_input("Discharge ($Q$, m³/s):", min_value=0.0, value=1.0, step=0.1)
    A = st.number_input("Cross-sectional Area ($A$, m²):", min_value=0.0001, value=0.5, step=0.05)
    
    if st.button("Calculate Velocity"):
        V = velocity(Q, A)
        st.success(f"**Fluid Velocity (V)** = **{V:,.2f} m/s**")

elif choice == "Discharge (Flow Rate)":
    st.header("💧 Discharge Calculation")
    st.write("Formula: $Q = A \\cdot V$")
    
    A = st.number_input("Cross-sectional Area ($A$, m²):", min_value=0.0, value=0.5, step=0.05)
    V = st.number_input("Fluid Velocity ($V$, m/s):", min_value=0.0, value=2.0, step=0.1)
    
    if st.button("Calculate Discharge"):
        Q = discharge(A, V)
        st.success(f"**Discharge (Q)** = **{Q:,.4f} m³/s**")

elif choice == "Reynolds Number":
    st.header("🌀 Reynolds Number Calculation")
    st.write("Formula: $Re = \\frac{\\rho \\cdot V \\cdot D}{\\mu}$")
    
    rho = st.number_input("Fluid Density ($\\rho$, kg/m³):", min_value=0.0, value=1000.0, step=10.0)
    V = st.number_input("Fluid Velocity ($V$, m/s):", min_value=0.0, value=1.5, step=0.1)
    D = st.number_input("Pipe Diameter ($D$, m):", min_value=0.0001, value=0.05, step=0.01)
    mu = st.number_input("Dynamic Viscosity ($\\mu$, Pa·s):", min_value=0.000001, value=0.001002, format="%.6f")
    
    if st.button("Calculate Reynolds Number"):
        Re = reynolds_number(rho, V, D, mu)
        st.success(f"**Reynolds Number (Re)** = **{Re:,.1f}**")
        
        # flow regime explanation
        if Re < 2300:
            st.info("Flow Regime: **Laminar Flow**")
        elif 2300 <= Re <= 4000:
            st.warning("Flow Regime: **Transient/Transition Flow**")
        else:
            st.error("Flow Regime: **Turbulent Flow**")

elif choice == "Dynamic Pressure":
    st.header("🏎️ Dynamic Pressure Calculation")
    st.write("Formula: $P_d = \\frac{1}{2} \\rho V^2$")
    
    rho = st.number_input("Fluid Density ($\\rho$, kg/m³):", min_value=0.0, value=1.225, step=0.1, help="Air density at sea level is roughly 1.225 kg/m³")
    V = st.number_input("Fluid Velocity ($V$, m/s):", min_value=0.0, value=10.0, step=1.0)
    
    if st.button("Calculate Dynamic Pressure"):
        Pd = dynamic_pressure(rho, V)
        st.success(f"**Dynamic Pressure ($P_d$)** = **{Pd:,.2f} Pa**")
