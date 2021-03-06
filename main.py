import sys
import mulesoft
import sap
import networking
import utils


def sap_messageid():
    sap.messageid()


def sap_password():
    sap.password()


def mulesoft_api_catalog():
    mulesoft.catalog()


def mulesoft_secure_properties():
    mulesoft.secure()


def ping():
    networking.ping()


def traceroute():
    networking.traceroute()


def dns_lookup():
    networking.dns_lookup()


def character_duplicate_remover():
    utils.character_duplicate_remover()


def main():
    menu_items = ["SAP Password", "SAP MessageID", "MuleSoft API Catalog", "MuleSoft Secure Properties", "Ping",
                  "Traceroute", "DNS lookup", "Character duplicate remover"]
    while True:
        application_name = "PItoolkit"
        application_name_placeholder = len(application_name) * "-"
        menu_title_placeholder = int(max([len(item) for item in menu_items]) / 2) * "-"
        menu_header = f"{menu_title_placeholder}{application_name}{menu_title_placeholder}"
        menu_footer = f"{menu_title_placeholder}{application_name_placeholder}{menu_title_placeholder}"
        for menu_item_index, menu_item in enumerate(menu_items):
            if menu_item_index == 0:
                print(menu_header)
            print(f"{menu_item_index + 1}. {menu_item}")
            if menu_item_index == len(menu_items) - 1:
                print(menu_footer)
        selection = input("Enter selection: ")
        try:
            if 0 < int(selection) < len(menu_items) + 1:
                try:
                    getattr(sys.modules[__name__], "%s" % menu_items[int(selection) - 1].lower().replace(" ", "_"))()
                except AttributeError:
                    quit("Function is not implemented")
        except ValueError:
            quit()
        else:
            quit()


if __name__ == "__main__":
    main()
