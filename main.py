import flet as ft

def main(page: ft.Page):

    page.title = "Calculador de BTUs por área (m2)"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.window.width = 412        
    page.window.height = 915
    page.window.resizable = False
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Icon(name=ft.icons.AC_UNIT, size=60), 
                alignment=ft.alignment.center,                
            ),
            expand=False
        )
    )
    page.add(ft.Text("Descubra a quantidade ideal de BTUs\nna hora de escolher seu aparelho de\nAr-condicionado!", size="16"))
    page.add(ft.Divider(height=2))
    
    def calcular(e):
        
        if tb1.value and tb2.value and tb3.value:            
            
            # Algorítmo 
            area = float(tb1.value) * float(tb2.value)
            btu_por_pessoa = float(tb3.value) * 600
            btu_total = (area * 600) + btu_por_pessoa 
            btu_total          

            dlg1 = ft.AlertDialog(
                title=ft.Text(f"É necessário um aparelho de\n              {int(btu_total)} BTUs", size=18), surface_tint_color='blue'
            )
            page.open(dlg1)
            page.update()

        else:
            
            dlg2 = ft.AlertDialog(
                title=ft.Text("Favor preencher todos os campos!", size=16)
            )
            page.open(dlg2)
            page.update()

    def limpar_tela(e):
        tb1.value = ''
        tb2.value = ''
        tb3.value = ''
        page.update()

    # def dica(e):
    #     dlg3 = ft.AlertDialog(
    #             title=ft.Text("Informar as dimensões em metros", size=16)
    #     )
    #     page.open(dlg3)
    #     page.update()

    def sair_app(e):
        page.window.close()
        
    tb1 = ft.TextField(label="Largura em metros", icon=ft.icons.COTTAGE, keyboard_type='DATETIME', width=300)
    tb2 = ft.TextField(label="Comprimento em metros", icon=ft.icons.GITE, keyboard_type='DATETIME', width=300)
    tb3 = ft.TextField(label="Nº de pessoas", icon=ft.icons.FAMILY_RESTROOM, keyboard_type='DATETIME', width=300)

    page.spacing=20   

    t = ft.Text()
    page.add(tb1, tb2, tb3, t)

    page.add(
        ft.Column(
            [
                ft.Container(
                    ft.ElevatedButton(text="Calcular", width=120, on_click=calcular),
                    alignment=ft.alignment.center,
                    expand=True
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )
    page.add(ft.Divider(height=2))

    page.add(
        ft.Row(
            [          
                ft.Container(
                    ft.FloatingActionButton(icon=ft.icons.REFRESH, tooltip='Limpar tela', on_click=limpar_tela),
                    alignment=ft.alignment.bottom_left,
                    padding=5                   
                ),
                ft.Container(
                    ft.FloatingActionButton(icon=ft.icons.LOGOUT, tooltip='Sair', on_click=sair_app),
                    alignment=ft.alignment.bottom_right,
                    padding=5                    
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

ft.app(main)