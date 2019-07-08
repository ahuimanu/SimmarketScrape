from Simmarket import SimmarketP3DV4SceneryParser


def main():
    app = SimmarketP3DV4SceneryParser()

    app.parse_sceneries()
    app.print_sceneries()


if __name__ == "__main__":
    # execute only if run as a script
    main()






