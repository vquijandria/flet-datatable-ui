import flet as ft
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable

txt_codigo_auxiliar = TextField(
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Código Auxiliar",
                           focused_border_color= "gray")


def main(page: Page):
    page.bgcolor = "#FDFDFD"
    page.padding = 20

    def __abrir_Registro(event):

        def __registrar(e):
            print(txt_codigo_auxiliar.value)

        def __regresar(e):
            page.views.pop()
            page.update()

        page.views.append(View(padding=40,


            controls=[
                Row(
                    
                    controls = [
                        
                        Column(spacing=2,
                       controls=[Text("Código Auxiliar"),
                                 txt_codigo_auxiliar
                       ,

                       ]),
                        
                        Column(spacing=2,
                        controls=[Text("ISIN"),
                                 TextField(
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Código ISIN",
                           focused_border_color= "gray"
                           
                           
                        ),
                        
                        ]),
                        Column(spacing=2,
                        controls=[Text("Symbol"),
                                 TextField(
                                    
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Symbol",
                           focused_border_color= "gray"
                        ),
                        
                        ]),
                        
                        
                    ]),
                Row(
                    controls = [
                    Column(spacing=2,
                        controls=[Text("ID del Valor"),
                                 TextField(
                                    
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "ID del Valor",
                           focused_border_color= "gray"
                        ),
                        
                        ]),
                    
                    
                    
                    Column(spacing=2,
                        controls=[Text("País"),
                                 TextField(
                                    
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "País",
                           focused_border_color= "gray"
                        ),
                        
                        ]),
                    
                    Column(spacing=2,
                        controls=[Text("Valor de Cierre"),
                                 TextField(
                                    
                           text_size=13,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Valor de Cierre",
                           focused_border_color= "gray"
                        ),
                        
                        ]),
                    
                    ]
                    ),
                
                Row(controls=[
                    Column(spacing=2,
                        controls=[Text("Descripción"),
                                 TextField(
                                    
                           text_size=13,
                           multiline = True,
                           height= 60,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Descripción",
                           focused_border_color= "gray"
                        ),
                        
                        ]),
                        Column(spacing=2,
                        controls=[Text("Segunda Descripción"),
                                 TextField(
                                    
                           text_size=13,
                           height= 60,
                           multiline = True,
                           content_padding=5,
                           cursor_color="black",
                           cursor_width=1,
                           cursor_height=18,
                           color="black",
                           hint_text= "Segunda Descripción",
                           focused_border_color= "gray"
                        ),
                        
                        ]),

                    
                ]),
                Row(
                    
                    controls = [
                        FilledButton("Registrar", on_click=__registrar),
                        FilledButton("Regresar", on_click=__regresar)
                    ]
                    
                    ),

            ]



        ))
        page.update()

    page.add(
        # Columna principal donde ira y mostrara cada componente
        Column(
            expand=True,
            controls=[
                # Las instancias de la clase van aqui...
                AppHeader(),
                Divider(height=2, color="transperent"),
                # AppForm(),
                Column(
                    scroll="hidden",
                    expand=True,

                    controls=[FilledButton(
                        "Nuevo", on_click=__abrir_Registro), AppDataTable()]
                ),
            ],
        )
    )
    page.update()
    pass


if __name__ == '__main__':
    ft.app(target=main)
