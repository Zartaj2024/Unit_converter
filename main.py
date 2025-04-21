import streamlit as st

def convert_length(value, from_unit, to_unit):
    """Convert between length units"""
    # Convert to meters first
    if from_unit == "meters":
        meters = value
    elif from_unit == "feet":
        meters = value * 0.3048
    elif from_unit == "miles":
        meters = value * 1609.34
    elif from_unit == "kilometers":
        meters = value * 1000
    else:
        return None
    
    # Convert to target unit
    if to_unit == "meters":
        return meters
    elif to_unit == "feet":
        return meters / 0.3048
    elif to_unit == "miles":
        return meters / 1609.34
    elif to_unit == "kilometers":
        return meters / 1000
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    """Convert between weight units"""
    # Similar structure as convert_length
    if from_unit == "kilograms":
        kg = value
    elif from_unit == "pounds":
        kg = value * 0.453592
    elif from_unit == "ounces":
        kg = value * 0.0283495
    else:
        return None
    
    if to_unit == "kilograms":
        return kg
    elif to_unit == "pounds":
        return kg / 0.453592
    elif to_unit == "ounces":
        return kg / 0.0283495
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    """Convert between temperature units"""
    # Convert to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        return None
    
    # Convert to target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    """Convert between volume units"""
    # Convert to liters first
    if from_unit == "liters":
        liters = value
    elif from_unit == "gallons":
        liters = value * 3.78541
    elif from_unit == "milliliters":
        liters = value / 1000
    else:
        return None
    
    # Convert to target unit
    if to_unit == "liters":
        return liters
    elif to_unit == "gallons":
        return liters / 3.78541
    elif to_unit == "milliliters":
        return liters * 1000
    else:
        return None

def main():
    st.title("📐 Unit Converter")
    
    # Create sidebar for conversion type selection
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature", "Volume"]
    )
    
    # Define available units for each type
    units = {
        "Length": ["meters", "feet", "miles", "kilometers"],
        "Weight": ["kilograms", "pounds", "ounces"],
        "Temperature": ["celsius", "fahrenheit", "kelvin"],
        "Volume": ["liters", "gallons", "milliliters"]
    }
    
    # Create main content area
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("Enter value", min_value=0.0, value=1.0, step=0.1)
        from_unit = st.selectbox("From unit", units[conversion_type])
    
    with col2:
        to_unit = st.selectbox("To unit", units[conversion_type])
        if st.button("Convert"):
            # Perform conversion based on type
            if conversion_type == "Length":
                result = convert_length(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = convert_weight(value, from_unit, to_unit)
            elif conversion_type == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)
            elif conversion_type == "Volume":
                result = convert_volume(value, from_unit, to_unit)
            
            # Display result
            if result is not None:
                st.success(f"**Result:** {value:.2f} {from_unit} = {result:.4f} {to_unit}")
            else:
                st.error("Invalid conversion - please check your units")

if __name__ == "__main__":
    main()