from os import remove
from pathlib import Path
from yaml import safe_load, dump
from decat.utils import pkg

home = script_dir = Path(__file__).parent.absolute()

def load_config() -> dict:
    with open(f"{home}/config/config.yaml", "r") as f:
        config_data: dict = safe_load(f)
        return config_data

def load_lock() -> dict:
    with open(f"{home}/config/config.lock", "r") as f:
        state_data: dict = safe_load(f)
        return state_data

def dump_config(pkgs: dict):
    with open(f"{home}/config/state.yaml", "w") as f:
        dump(pkgs, f, default_flow_style=False)

def query(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print(f"Entering dictionary: {key}")
            query(value)
        else:
            print(f"{key}: {value}")
            match key:
                case "pkgs":
                     print("yay")
                   

if __name__ == "__main__":
    data = load_config()
    #print(data)
    lock = load_lock()

    # Query the config file
    query(data)
    #print(data_bit)
    #for bit in data_bit:
     #   print(bit)
    ##       case "pkgs":
     #           print("yay")




    for top_key, top_value in data.items():
        #print(f"{top_key} : {top_value}")
        match top_key:
            case "pkgs":
                #install(top_value)
                #dump_config(load_config())
                pass
