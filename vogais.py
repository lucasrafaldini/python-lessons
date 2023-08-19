from collections import Counter
# Esse é a biblioteca auxiliar do python para lidar com jsons. Ela é built-in, não requerendo instalação
import json
# pandas e matplot lib são bibliotecas externas, então requerem instalação
import pandas as pd
import matplotlib.pyplot as plt


# Primeiro criamos uma classe que abarque todas as funções que desejamos
class DataVisualizer:

    def __init__(self, filename='texto.json', key='text'):
        # Aqui definimos os atributos da classe
        self.text: str
        self.filename = filename
        self.key = key

    # Dentro dessa classe, podemos iniciar com uma função que pegue e trate o nosso input (nesse caso, o texto)
    # Para tornar o exemplo um pouco mais real, vou colocar o texto dentro de um json

    # Repare que estou passando dois parâmetros, mas estou definindo valores default para eles
    # Assim a função pode ser chamada mesmo sem parâmetros e funcionará no caso exemplar
    def get_text_from_json(self):
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
                if self.key in data:
                    return data[self.key]
                else:
                    print(f"Key '{self.key}' not found in the JSON file.")
                    return None
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{self.filename}'.")
            return None
    
    def plot_individual_vowels(self, text):
        if text is not None:
            # Count the occurrences of each vowel
            vowel_counts = Counter(char for char in text.lower() if char in 'aeiou')
            # breakpoint()
            # Extract vowel labels and counts
            vowels = list(sorted(vowel_counts.keys()))
            counts = [vowel_counts[item] for item in vowels]

            # Define a custom color palette for the bars
            colors = ['red', 'blue', 'green', 'orange', 'purple']

            # Creating a DataFrame for visualization
            data = {'Vowel': vowels, 'Count': counts}
            df = pd.DataFrame(data)

            # Creating a bar chart using pandas and matplotlib
            df.plot(kind='bar', x='Vowel', y='Count', legend=None, color=colors)
            plt.title('Vowel Counts in Text')
            plt.ylabel('Count')
            plt.xlabel('Vowel')
            plt.xticks(rotation=0)
            plt.tight_layout()

            plt.show()

        else:
            raise Exception('No text to plot statistics')

    def main(self):
        text = self.get_text_from_json()
        # breakpoint()
        self.plot_individual_vowels(text)

if __name__ == '__main__':
    # Agora podemos chamar as funções da classe
    instance = DataVisualizer()
    instance.main()