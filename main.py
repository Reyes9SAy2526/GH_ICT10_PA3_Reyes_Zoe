# Comment here
from pyscript import display, document


def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
        'Madagascar': 'Antananarivo',
        'Mongolia': 'Ulaanbaatar',
        'Egypt': 'Cairo',
        'Philippines': 'Manila',
        'USA': 'Washington D.C.',
        'Denmark': 'Copenhagen',
        'Chile': 'Santiago'
    }

    countries_checker = user_input in countries

    display_message = (
        f'Sorry, no {user_input} in the list',
        f'{user_input} is in the list. Its capital is {countries.get(user_input)}'
    )

    display(display_message[countries_checker], target='results')