# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y9DViJ0ZUt09-ZhEhB9c0tvIohz-PwS5
"""

import csv

def process_csv(input_filename, output_filename):
    # Abrir el archivo CSV para leer
    with open(input_filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        # Saltar la primera línea que contiene los encabezados
        next(csvreader)

        # Abrir el archivo de salida para escribir las reseñas
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            count = 0  # Contador para las reseñas procesadas
            for row in csvreader:
                if count >= 10000:
                    break  # Detenerse después de 1000 reseñas

                # La reseña está en la columna 'Text' (índice 9)
                review_text = row[9]

                # Escribir la reseña en el archivo de salida, seguido de una nueva línea
                outfile.write(review_text + '\n')
                count += 1

    print(f"El archivo de texto con las primeras 1000 reseñas se ha generado exitosamente: {output_filename}")

# Usar la función
input_filename = 'Reviews.csv'  # Ruta del archivo CSV de entrada
output_filename = 'reviews_output.txt'  # Ruta del archivo de salida

process_csv(input_filename, output_filename)