import flet as ft 
from flet import *
from controls import add_to_control_reference

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    
    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)


    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    #the column args will set the number of columns to be displayed
                    columns=[
                        DataColumn(
                            Text("Cod Auxiliar", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("ISIN", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Descripcion", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("ID Valor", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Symbol", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Pais", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Desc 2", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Tipo Movimiento", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Valor Cierre", size=12, color="black", weight="bold")
                        ),
                    ],
                    #here is the configuration of the form to append the data into the rows
                    rows=[],
                )
            ],
        )