import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers


def main():
    session = script_helpers.get_api_session()
    sandbox_id = script_helpers.get_reservation_context_details().id

    session.ConfigureApps(reservationId=sandbox_id, printOutput=True)


if __name__ == "__main__":
    main()
