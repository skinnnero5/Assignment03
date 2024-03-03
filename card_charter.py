import matplotlib.pyplot as plt
import json

class CardCharter:
    """Class for displaying matplotlib charts based on the data provided."""

    DEBUG = False

    @staticmethod
    def display_color_pie_chart(data, set):
        """
        Generate and display a pie chart based on the colors of the cards.

        Parameters:
        - data (list): List of JSON objects with Magic the Gathering card data.
        - set (str): The Magic the Gathering set abbreviation (ex: 'RVR' for Ravnica Remastered).
        """

        color_count = {'None'         : 0,
                       'Multicolored' : 0,
                       'White'        : 0,
                       'Blue'         : 0,
                       'Black'        : 0,
                       'Red'          : 0,
                       'Green'        : 0}

        for card_data in data:
            card = json.loads(card_data)
            if CardCharter.DEBUG:
                print(f"DEBUG| CardCharter card {card}")
            if (len(card['colors']) == 0):
                color_count['None'] += 1
            elif (len(card['colors']) > 1):
                color_count['Multicolored'] += 1
            else:
                match card['colors'][0]:
                    case 'W':
                        color_count['White'] += 1
                    case 'U':
                        color_count['Blue'] += 1
                    case 'B':
                        color_count['Black'] += 1
                    case 'R':
                        color_count['Red'] += 1
                    case 'G':
                        color_count['Green'] += 1

        labels = list(color_count.keys())
        values = list(color_count.values())

        colors_list = ['#CCCCCC', '#FFD700', '#EEEEEE', '#0000FF', '#444444', '#FF0000', '#00FF00']
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors = colors_list)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f"Color distribution for {set}")
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Color Distribution Pie Chart')
        plt.show()