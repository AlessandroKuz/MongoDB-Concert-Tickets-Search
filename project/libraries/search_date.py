from project.libraries.mongo_connection import collection_connection
from project.libraries.join_concert_tickets import join_concert_tickets
from project.libraries.display_concerts import display_concerts
from project.libraries.buy_tickets import buy_tickets
import datetime


def search_by_date(start_date: datetime.datetime, end_date: datetime.datetime):
    ticket_collection = collection_connection('Compravendita-Concerti', 'Biglietto')
    tickets = join_concert_tickets(ticket_collection)

    selected_tickets = [ticket for ticket in tickets if start_date <= ticket['id_concerto'][0]['data_ora'] <= end_date]

    display_concerts(selected_tickets)
    buy_tickets(ticket_collection, selected_tickets)
