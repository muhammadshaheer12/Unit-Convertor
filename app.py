import streamlit as st
from forex_python.converter import CurrencyRates

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ('metre', 'centimetre'): 100,
        ('centimetre', 'metre'): 0.01,
        ('kilometre', 'metre'): 1000,
        ('metre', 'kilometre'): 0.001,
        ('gram', 'kilogram'): 0.001,
        ('kilogram', 'gram'): 1000,
        ('pound', 'kilogram'): 0.453592,
        ('kilogram', 'pound'): 2.20462,
        ('litre', 'millilitre'): 1000,
        ('millilitre', 'litre'): 0.001,
    }
    
    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]
    elif (to_unit, from_unit) in conversion_factors:
        return value / conversion_factors[(to_unit, from_unit)]
    else:
        return None

def convert_currency(value, from_currency, to_currency):
    c = CurrencyRates()
    try:
        return c.convert(from_currency, to_currency, value)
    except:
        return None

st.markdown("""
    <style>
        .main {background-color: #f4f4f4;}
        .stButton>button {border-radius: 10px; padding: 10px; font-size: 16px; background-color: #4CAF50; color: white;}
        .stSelectbox, .stNumberInput {border-radius: 5px;}
    </style>
""", unsafe_allow_html=True)

st.title(" 🔄 Unit Convertor 🌍")
st.write("⚡ Convert between different units easily! ⚖️📏💧💰")

categories = {
    "Length 📏": ["metre", "centimetre", "kilometre"],
    "Weight ⚖️": ["gram", "kilogram", "pound"],
    "Volume 💧": ["litre", "millilitre"],
    "Currency 💰": ["USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD"]
}

selected_category = st.selectbox("📌 Select Category", list(categories.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔄 From Unit", categories[selected_category])
    value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")
with col2:
    to_unit = st.selectbox("➡️ To Unit", categories[selected_category])

if st.button("🚀 Convert", help="Click to convert the units"):
    if selected_category == "Currency 💰":
        result = convert_currency(value, from_unit, to_unit)
    else:
        result = convert_units(value, from_unit, to_unit)
    
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit} 🎯")
    else:
        st.error("❌ Conversion not available for selected units.")
