
# GUI Project

This project is part of my research contribution at Koç University. It is an application developed using Python and PyQt5, designed to model and analyze laser-material interactions.

## Project Overview

The Laser Simulation Project is a desktop application that allows users to:

1. Select and manage materials for simulation
2. Set laser parameters
3. Import and visualize G-code files
4. Run simulations based on the selected parameters

## Technologies Used

- **Python**: Primary programming language
- **PyQt5**: For creating the graphical user interface
- **PyQtGraph**: For data visualization
- **fbs (fman build system)**: For building and packaging the application

## Key Components

### 1. Material Selection

Users can select materials from a predefined list or add new ones. Each material has properties such as density, conductivity, specific heat, and diffusion.

### 2. Laser Parameters

This component allows users to input and save various laser parameters, including laser power, velocity, diameter, layer thickness, and absorbability.

### 3. File and Simulation Parameters

Users can select G-code files, visualize layers, and set simulation parameters for the run.

### 4. Simulation

This tab will handle the core simulation logic based on selected materials, laser parameters, and G-code files.

## Main Application

The main application window brings together all the components into a tabbed interface.

## Future Work

This project is part of ongoing research, and future updates may include:

- Implementation of the core simulation algorithms
- Enhanced visualization of simulation results
- Integration with external libraries for more accurate physical modeling
- Performance optimization for large-scale simulations

## Contribution

This project is developed as part of research at Koç University. Contributions, suggestions, and feedback are highly encouraged to improve the simulation's functionality and accuracy.

## Running the Project

To run the project, ensure that you have `fbs` installed, then use the following command:

```bash
fbs run
```

This will build and launch the application.

---

Feel free to contribute by submitting issues or pull requests to the project repository.
