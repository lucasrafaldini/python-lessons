# Esse é a biblioteca auxiliar do python para lidar com jsons. Ela é built-in, não requerendo instalação
import json
# pandas e matplot lib são bibliotecas externas, então requerem instalação
import pandas as pd
import matplotlib.pyplot as plt


# Primeiro criamos uma classe que abarque todas as funções que desejamos
class DataVisualizer:

    # Dentro dessa classe, podemos iniciar com uma função que pegue e trate o nosso input (nesse caso, o texto)
    # Para tornar o exemplo um pouco mais real, vou colocar o texto dentro de um json

    # Repare que estou passando dois parâmetros, mas estou definindo valores default para eles
    # Assim a função pode ser chamada mesmo sem parâmetros e funcionará no caso exemplar
    def get_text_from_json(json_file_path='texto.json', key='texto'):
        try:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                
                if key in data:
                    return data[key]
                else:
                    print(f"Key '{key}' not found in the JSON file.")
                    return None
        except FileNotFoundError:
            print(f"File '{json_file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{json_file_path}'.")
            return None
    
    def count_vowels(text):
        vowels = "AEIOUaeiou"
        vowel_count = sum(1 for char in text if char in vowels)
        return vowel_count
    
    def plot_statistics(text):
        if text is not None:
            vowel_count = count_vowels(text)
            print("Number of vowels:", vowel_count)
            
            # Criando um Dataframe para visualização
            data = {'Text': [text], 'Vowel Count': [vowel_count]}
            df = pd.DataFrame(data)

            # Criando um gráfico de barra com o pandas e o matplotlib
            df.plot(kind='bar', x='Text', y='Vowel Count', legend=None)
            plt.title('Vowel Count in Text')
            plt.ylabel('Number of Vowels')
            plt.xlabel('Text')
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.show()
        else:
            raise Exception('No text to plot statistics')


