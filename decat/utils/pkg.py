from subprocess import run

def install(pkgs: dict):
    for key, app_list in pkgs.items():
        #print(f"{key} : {app_list}")
        cmd = []
        trail = ""
        # Setting up the first arguments of install command
        match key:
            case "flatpak":
                cmd = ["flatpak", "install"]
                trail = "-y"
            case "homebrew":
                cmd = ["brew", "install"]

        # Adding packages to install command
        cmd.extend(app_list)

        if len(trail) > 0:
            cmd.append(trail)

        if app_list != [None]:
            print(cmd)
            run(cmd)
