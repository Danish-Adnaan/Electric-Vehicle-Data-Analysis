# Electric Vehicle Data Analysis Project

## Project Overview
This project involves analyzing a dataset related to electric vehicles (EVs). The dataset contains various features such as electric range, energy consumption, price, and other relevant attributes. The goal is to uncover meaningful insights, tell a compelling story, perform hypothesis testing, and provide actionable recommendations based on the data.

## Dataset
- Filename: FEV-data-Excel.xlsx

## Dataset Overview
- **Car full name:** Full designation of the vehicle (make, model, variant)  
- **Make:** Brand or manufacturer of the car  
- **Model:** Specific model/version  
- **Minimal price (gross) [PLN]:** Minimum retail price in Polish złoty (PLN)  
- **Engine power [KM]:** Engine power in horsepower (KM)  
- **Maximum torque [Nm]:** Peak torque in Newton-meters (Nm)  
- **Type of brakes:** Braking system (e.g., disc, drum)  
- **Drive type:** Drivetrain configuration (FWD, RWD, AWD)  
- **Battery capacity [kWh]:** Battery energy capacity in kilowatt-hours (kWh)  
- **Range (WLTP) [km]:** Estimated driving range on full charge under WLTP standards  
- **Wheelbase [cm]:** Distance between front and rear axles  
- **Length [cm]:** Overall length of the car  
- **Width [cm]:** Width of the car  
- **Height [cm]:** Height of the car  
- **Minimal empty weight [kg]:** Minimum empty weight of the car  
- **Permissible gross weight [kg]:** Maximum allowed weight including passengers and cargo  
- **Maximum load capacity [kg]:** Max weight car can carry  
- **Number of seats:** Passenger seats count  
- **Number of doors:** Number of doors on the car  
- **Tire size [in]:** Tire size in inches  
- **Maximum speed [kph]:** Top speed in km/h  
- **Boot capacity (VDA) [l]:** Trunk/cargo space capacity in liters  
- **Acceleration 0-100 kph [s]:** Time in seconds from 0 to 100 km/h  
- **Maximum DC charging power [kW]:** Max charging power with fast charger  
- **Mean Energy consumption [kWh/100 km]:** Average energy use per 100 km  

## Tools Used
- Python libraries: Pandas, NumPy, SciPy, Matplotlib, and others as needed

## Instructions
- Write clean, structured code with explanations to guide readers through your analysis.
- Each task requires a coding solution and a written section explaining findings.

## Tasks

### Task 1
- Filter electric vehicles within budget (350,000 PLN) and minimum range (400 km).
- Group the filtered EVs by manufacturer (Make).
- Calculate the average battery capacity for each manufacturer.

### Task 2
- Detect outliers in the "Mean Energy consumption [kWh/100 km]" column to identify EVs with unusually high or low consumption.

### Task 3
- Visualize the relationship between battery capacity and range using an appropriate plot.
- Provide insights based on the visualization.

### Task 4
- Build an EV recommendation class that accepts user input for budget, desired range, and battery capacity.
- The class should return the top three EVs matching the criteria.

### Task 5
- Perform hypothesis testing (two-sample t-test) to check if there is a significant difference in average engine power ([KM]) between Tesla and Audi vehicles.
- Draw insights from the test results.

## Recommendations and Conclusion
- Summarize actionable insights derived from the data analysis and hypothesis testing to guide decision-making.
