import streamlit as st

def main():
    st.title("🏠 Home Energy Consumption Calculator")
    st.write("Calculate your daily energy consumption based on your home setup!")
    
    # User info
    st.header("👤 Personal Information")
    name = st.text_input("Enter your name:", value="Jenil")
    age = st.number_input("Enter your age:", min_value=1, max_value=120, value=19)
    
    # Living type
    st.header("🏢 Housing Type")
    living_options = {
        "Flat": "1",
        "Tenement": "2", 
        "Bungalow": "3"
    }
    living = st.selectbox("Where do you live?", list(living_options.keys()))
    
    # Display living type
    if living == "Flat":
        st.success("You live in a flat.")
    elif living == "Tenement":
        st.success("You live in a Tenement")
    elif living == "Bungalow":
        st.success("You live in a Bungalow")
    
    # BHK selection
    st.header("🏠 House Configuration")
    bhk_options = ["1 BHK", "2 BHK", "3 BHK"]
    bhk = st.selectbox("How many BHK is your house?", bhk_options)
    
    # Calculate base energy consumption
    energy = 0
    
    if bhk == "1 BHK":
        energy = 2.4  # Fixed value as in original code
        st.info(f"You have 2 lights and 2 fans in your house. Base energy consumption: {energy} kWh")
    elif bhk == "2 BHK":
        energy = (3 * 0.4) + (3 * 0.8)  # 3 lights + 3 fans
        st.info(f"You have 3 lights and 3 fans in your house. Base energy consumption: {energy} kWh")
    elif bhk == "3 BHK":
        energy = (4 * 0.4) + (4 * 0.8)  # 4 lights + 4 fans
        st.info(f"You have 4 lights and 4 fans in your house. Base energy consumption: {energy} kWh")
    
    # Additional appliances
    st.header("🔌 Additional Appliances")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ac = st.checkbox("❄️ Air Conditioner", help="Adds 3 kWh to consumption")
        if ac:
            energy += 3
    
    with col2:
        wm = st.checkbox("🧺 Washing Machine", help="Adds 3 kWh to consumption")
        if wm:
            energy += 3
    
    with col3:
        fridge = st.checkbox("🧊 Refrigerator", help="Adds 3 kWh to consumption")
        if fridge:
            energy += 3
    
    # Results
    st.header("📊 Energy Consumption Summary")
    
    # Create a summary card
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Total Daily Energy Consumption",
            value=f"{energy} kWh",
            delta=f"{energy - 2.4:.1f} kWh above base" if energy > 2.4 else None
        )
    
    with col2:
        monthly_consumption = energy * 30
        st.metric(
            label="Estimated Monthly Consumption",
            value=f"{monthly_consumption} kWh"
        )
    
    # Breakdown
    st.subheader("📋 Consumption Breakdown")
    
    breakdown_data = []
    base_consumption = 0
    
    if bhk == "1 BHK":
        base_consumption = 2.4
        breakdown_data.append(("Lights & Fans (2 each)", 2.4))
    elif bhk == "2 BHK":
        base_consumption = 3.6
        breakdown_data.append(("Lights & Fans (3 each)", 3.6))
    elif bhk == "3 BHK":
        base_consumption = 4.8
        breakdown_data.append(("Lights & Fans (4 each)", 4.8))
    
    if ac:
        breakdown_data.append(("Air Conditioner", 3.0))
    if wm:
        breakdown_data.append(("Washing Machine", 3.0))
    if fridge:
        breakdown_data.append(("Refrigerator", 3.0))
    
    for item, consumption in breakdown_data:
        st.write(f"• {item}: **{consumption} kWh**")
    
    # Tips section
    st.header("💡 Energy Saving Tips")
    tips = [
        "Use LED bulbs instead of incandescent bulbs to save up to 80% energy",
        "Set your AC temperature to 24°C or higher for optimal efficiency",
        "Unplug appliances when not in use to avoid phantom energy consumption",
        "Use natural light during the day to reduce lighting needs",
        "Regular maintenance of appliances ensures better efficiency"
    ]
    
    for tip in tips:
        st.write(f"• {tip}")
    
    # Footer
    st.markdown("---")
    st.markdown("*This calculator provides estimated energy consumption based on typical appliance usage patterns.*")

if __name__ == "__main__":
    main()