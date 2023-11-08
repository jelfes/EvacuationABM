This repository implements an Agent Based Model (ABM) to similuate the impact of having friends around oneself on the panic level during an evacuation.

# Run
In order to run the experiment in a nice web interface run

```
python run_webapp.py
```

# File Overview 
`agent.py` defines the agent class for the simulation;   
`model.py` define the model class for the simulation;  
`canvas.py` define a class to represent the continous space module on the web application;  
`helpers.py` set of helper funcitons;  
`server.py` sets up the web application, defining parameter controls and visualizations;  
`run_webapp.py` launches the webapp;