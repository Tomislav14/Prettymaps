import prettymaps

plot = prettymaps.plot(
    'Donji Grad, Zagreb',
    circle=True,
    radius=False,
    layers={
        "green": {
            "tags": {
                "landuse": "grass",
                "natural": ["island", "wood"],
                "leisure": "park"
            }
        },
        "forest": {
            "tags": {
                "landuse": "forest"
            }
        },
        "water": {
            "tags": {
                "natural": ["water", "bay"]
            }
        },
        "parking": {
            "tags": {
                "amenity": "parking",
                "highway": "pedestrian",
                "man_made": "pier"
            }
        },
        "streets": {
            "width": {
                "motorway": 5,
                "trunk": 5,
                "primary": 4.5,
                "secondary": 4,
                "tertiary": 3.5,
                "residential": 3,
            }
        },
        "building": {
            "tags": {"building": True},
        },
    },
    style={
        "background": {
            "fc": "#FFFFFF",  # Bijela boja pozadine
            "ec": "#FFFFFF",  # Boja ruba pozadine (u ovom slučaju, bijela)
            "hatch": "ooo...",  # Opcionalno: šara
        },
        "perimeter": {
            "fc": "#FFFFFF",  # Bijela boja perimetra (rub kartice)
            "ec": "#FFFFFF",  # Boja ruba perimetra (u ovom slučaju, bijela)
            "lw": 0,  # Debljina linije perimetra (postavljeno na 0 da se ne prikaže)
            "hatch": "ooo...",  # Opcionalno: šara
        },
        "green": {
            "fc": "#D0F1BF",
            "ec": "#2F3737",
            "lw": 1,
        },
        "forest": {
            "fc": "#64B96A",
            "ec": "#2F3737",
            "lw": 1,
        },
        "water": {
            "fc": "#a1e3ff",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#85c9e6",
            "lw": 1,
        },
        "parking": {
            "fc": "#F2F4CB",
            "ec": "#2F3737",
            "lw": 1,
        },
        "streets": {
            "fc": "#2F3737",
            "ec": "#475657",
            "alpha": 1,
            "lw": 0,
        },
        "building": {
            "fc":"#000000",
            "ec": "#2F3737",
            "lw": 0.5,
        }
    }
)

    