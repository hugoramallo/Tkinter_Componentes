import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class Componentes (tk.Tk):

    def __init__(self):
        # Inicializar componente de la clase padre con super y __init__
        super().__init__()
        # resolución 650x400, la ventaja se mostrará en la posición eje x: +450 eje y: +200
        self.geometry('650x400+450+200')
        self.title('Componentes')
        # ventana.iconbitmap('icono.ico')
        self._crear_tabs()

    def _crear_componentes_tabulador1(self, tabulador):
    # Agregar una etiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador, text='Nombre: ')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # Agregamos un botón
        def enviar():
            messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')
        boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def _crear_componentes_tabulador2(self, tabulador):
        contenido = 'Este es mi texto con el contenido'
        # Creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        # Mostramos el componente
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(self, tabulador):
        # Creamos una lista usando data list comprehensions (0-9)
        datos = [x+1 for x in range(100,110)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        # Seleccionamos un elemento por default a mostrar
        combobox.current(5-1)
        # Agregar botón para saber qué opción seleccionó el usuario
        def mostrar_valor():
            messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')
        boton1 = ttk.Button(tabulador, text='Mostrar valor Seccionado', command=mostrar_valor)
        boton1.grid(row=0, column=1)

    def _crear_componentes_tabulador4(self, tabulador):
        imagen = tk.PhotoImage(file='Python.png')
        def mostrar_titulo():
            messagebox.showinfo('Más info imagen', f'Nombre imagen: {imagen.cget("file")}')
        boton_imagen = ttk.Button(tabulador, image= imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(self, tabulador):
        # Creamos el componente de barra de progreso
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        # Métodos para controlar los eventos de la barra de progreso
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
                sleep(0.05)
                # Incrementamos nuestra barra de progreso
                barra_progreso['value'] = valor
                # Actualizamos la barra de progreso
                barra_progreso.update()
            barra_progreso['value'] = 0

        def ejecutar_ciclo():
            barra_progreso.start()

        def detener():
            barra_progreso.stop()

        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop())

        # Botones para controlar eventos
        boton_inicio = ttk.Button(tabulador, text='Ejecutar barra de progreso', command=ejecutar_barra)

        boton_inicio.grid(row=1, column=0)
        boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        boton_detener = ttk.Button(tabulador, text='Detener ejecución', command=detener)
        boton_detener.grid(row=1, column=2)
        boton_despues = ttk.Button(tabulador, text='Detener ejecución después', command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def _crear_tabs(self):
        # Creamos un tab contro, para ello usamos la clase de notebook
        control_tabulador = ttk.Notebook(self)
        # Agregamos un marco o frame para agregar dentro del tab y organizar los elemtnos
        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='Tabulador 1')
        #Mostramos el tabulador
        control_tabulador.pack(fill='both')
        # Creamos los componentes del tabulador 1
        self._crear_componentes_tabulador1(tabulador1)
        # Creamos un segundo tabulador
        tabulador2 = ttk.Labelframe(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador2, text='Tabulador 2')
        # Creamos los componentes del segundo tabulador
        self._crear_componentes_tabulador2(tabulador2)
        # Crear un tercer tabulador
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text='Tabulador 3')
        # Creamos los componentes del tercer tabulador
        self._crear_componentes_tabulador3(tabulador3)
        # Creamos un cuarto tabulador
        tabulador4 = ttk.Labelframe(control_tabulador, text='Imagen')
        control_tabulador.add(tabulador4, text='Tabulador 4')
        # Creamos lo componentes del cuarto tabulador
        self._crear_componentes_tabulador4(tabulador4)
        # Creamos un quinto tabulador
        tabulador5= ttk.Labelframe(control_tabulador, text='Barra de progreso')
        control_tabulador.add(tabulador5, text='Tabulador 5')
        # Creamos los componentes
        self._crear_componentes_tabulador5(tabulador5)

# Se comprueba si se ejecuta desde este mismo archivo
if __name__ == '__main__':
    # Creamos objeto de nuestra clase
    componentes_ventana = Componentes()
    componentes_ventana.mainloop()


