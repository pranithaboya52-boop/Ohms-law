# Ohm's Law Calculator
# Formula: V = I × R

print("================================")
print("       OHM'S LAW CALCULATOR")
print("================================")
print("1. Calculate Voltage")
print("2. Calculate Current")
print("3. Calculate Resistance")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    # V = I × R
    current = float(input("Enter Current (A): "))
    resistance = float(input("Enter Resistance (Ω): "))

    voltage = current * resistance

    print("\nResult:")
    print(f"Voltage = {voltage:.2f} V")

elif choice == "2":
    # I = V / R
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (Ω): "))

    if resistance == 0:
        print("Error: Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print("\nResult:")
        print(f"Current = {current:.2f} A")

elif choice == "3":
    # R = V / I
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))

    if current == 0:
        print("Error: Current cannot be zero.")
    else:
        resistance = voltage / current
        print("\nResult:")
        print(f"Resistance = {resistance:.2f} Ω")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
