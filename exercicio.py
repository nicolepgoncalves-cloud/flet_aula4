import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("O Banguela é tipo um gatinho preto, fofinho."))

    page.add(
        ft.Text("Olá, Meu nome é Soluço!"),
        ft.Image(
            src="imeges/banguela.jpg",
            height=200
        ),
        ft.Button(
            content="Clique aqui",
            on_click=mostrar_mensagem,
            bgcolor="#bf0606",
            color="white"
        )
       

    
    )

ft.app(main)    