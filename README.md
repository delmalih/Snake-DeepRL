# Snake-DeepRL

![game]("./images/game.png")

### Requirements

* Python 3
* `pip3 install -r requirements.txt`

### How to use it ?

Before running the `run_agent.py` script, feel free to edit the `constants.py` file.

##### Run a random player :

```
python3 run_agent.py -a Random
```

##### Train a CNN agent :

```
python3 run_agent.py -a CNN --train
```

![game]("./images/training.png")

##### Run a CNN agent (with the pretrained model in `<OUTPUT_PATH>/model.pth`) :

```
python3 run_agent.py -a CNN
```