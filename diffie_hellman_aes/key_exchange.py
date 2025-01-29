from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
import json

def generate_dh_keys():
    parameters = dh.generate_parameters(generator=2, key_size=1024, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    
    param_numbers = parameters.parameter_numbers()
    p = param_numbers.p
    g = param_numbers.g
    y = public_key.public_numbers().y

    keys = {
        "p": str(p),
        "g": str(g),
        "private_key": str(private_key.private_numbers().x),
        "public_key": str(y)
    }

    with open("keys.json", "w") as f:
        json.dump(keys, f)

    return private_key, public_key, p, g

def load_dh_keys():
    with open("keys.json", "r") as f:
        keys = json.load(f)

    return (
        int(keys["p"]),
        int(keys["g"]),
        int(keys["private_key"]),
        int(keys["public_key"])
    )