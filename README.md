This repository implements an Agent Based Model (ABM) to simulate the impact of having friends around oneself on the panic level during an evacuation.

# Run
In order to run the experiment in a nice web interface run

```
python run_webapp.py
```

to run it locally or click on [this link](https://evacuation-abm.onrender.com/) to use a version hosted on Render.

# File Overview 
`agent.py` defines the agent class for the simulation;   
`model.py` defines the model class for the simulation;  
`canvas.py` defines a class to represent the continuous space module on the web application;  
`helpers.py` set of helper functions;  
`server.py` sets up the web application, defining parameter controls and visualizations;  
`run_webapp.py` launches the webapp;  
`batch_experiment.ipynb` summary of the different experiments;
