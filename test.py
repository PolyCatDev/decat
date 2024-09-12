def recursive_parse(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print(f"Entering dictionary: {key}")
            recursive_parse(value)
        else:
            print(f"{key}: {value}")

# Example usage
data = {'pkgs': {'flatpak': ['org.mozilla.Thunderbird'], 'homebrew': ['lsd', 'dust', 'fastfetch', 'pipx']}, 'test': {'banana': [1], 'yay': [3, 4]}}
recursive_parse(data)

