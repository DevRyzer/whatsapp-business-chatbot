TOOLS = [
    {
        "type": "function",
            "function": {
                "name": "search_properties",
                "description": "Search for properties in the database using the user`s"
                                "specified criteria. Use this function whenever the user"
                                "asks to find, search, recommend or filter properties",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "zone": {
                            "type": "string", 
                            "description":  "Neighborhood or area requested by the user"
                                            "Use null if the user did not specify an area"
                            },
                        "max_price": {
                            "type": ["number", "null"], 
                            "description":  "Maximum property price in euros"
                                            "Use null if the user did not specify a maximum price"
                            },
                        "habitaciones_min": {
                            "type": ["integer", "null"], 
                            "description":  "Minimum number of bedrooms."
                                            "Use null if the user did not specify a it."
                            }
                    },
                "required": [
                    "zone",
                    "max_price",
                    "habitaciones_min"
                ]
                },
            }
    }
]