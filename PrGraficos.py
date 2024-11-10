import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, filedialog

# Función para cargar el archivo y mostrar gráficos de precipitaciones de pueblos específicos
def mostrar_grafico():
    # Abrir diálogo para seleccionar archivo CSV
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if archivo:
        # Cargar datos
        data = pd.read_csv(archivo)
        
        # Imprimir nombres de columnas para verificar
        print("Columnas del archivo CSV:", data.columns)
        
        # Convertir FechaObservacion a datetime para manejar fecha y hora
        data['FechaHora'] = pd.to_datetime(data['FechaObservacion'], errors='coerce')
        
        # Filtrar solo los pueblos de interés
        pueblos_interes = ["LAGUNA DE LA PLAZA", "MALPELO - DIMAR", "BORAUDO"]
        data_filtrada = data[data['NombreEstacion'].isin(pueblos_interes)]
        
        # Convertir 'ValorObservado' a numérico, forzando los errores a NaN
        data_filtrada['ValorObservado'] = pd.to_numeric(data_filtrada['ValorObservado'], errors='coerce')
        
        # Agrupar por pueblo y fecha para graficar
        plt.figure(figsize=(10, 6))
        
        for pueblo in pueblos_interes:
            pueblo_data = data_filtrada[data_filtrada['NombreEstacion'] == pueblo]
            plt.plot(pueblo_data['FechaHora'], pueblo_data['ValorObservado'], label=pueblo, marker='o')
        
        # Personalizar el gráfico
        plt.title('Precipitación Observada en Pueblos Seleccionados', fontsize=16)
        plt.xlabel('Fecha y Hora de Observación', fontsize=12)
        plt.ylabel('Precipitación (mm)', fontsize=12)
        
        # Ajustar las etiquetas de los ejes
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        
        # Mostrar la leyenda con un tamaño de fuente más grande
        plt.legend(fontsize=10)
        
        plt.tight_layout()
        plt.show()

# Configurar ventana de la interfaz gráfica
ventana = Tk()
ventana.title("Programa de Precipitaciones en Pueblos")
ventana.geometry("400x150")  # Establece el tamaño de la ventana
ventana.resizable(False, False)  # Deshabilita el redimensionado

# Crear y centrar el botón
Button(ventana, text="Seleccionar archivo y mostrar gráfico", command=mostrar_grafico, width=30, height=2).pack(pady=40)

ventana.mainloop()
