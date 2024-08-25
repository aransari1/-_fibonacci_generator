import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column, Container
from flet_core.control_event import ControlEvent
from Backend import Fibonacci_Generator
ThemeChanger = 'light'

def Main_Function(page: ft.Page) -> None:
    page.title = "Fibonacci Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 275
    page.window.height = 400
    #page.window.resizable = False
    page.theme_mode = ThemeChanger

    
    def Decrement_Function(e: ControlEvent) -> None:
        User_Range_Input.value = str(int(User_Range_Input.value) - 1)
        page.update()

    def Increment_Function(e: ControlEvent) -> None:
        User_Range_Input.value = str(int(User_Range_Input.value) + 1)
        page.update()

    def Validation(e: ControlEvent) -> None:
        if User_Range_Input.value.strip():
            Generate_Button.disabled = False
        else:
            Generate_Button.disabled = True
        page.update()

    def Generate_Click(e):
        Fibonacci_Series = Fibonacci_Generator(int(User_Range_Input.value))
        Fibonacci_Showing_Label.value = f"Fibonacci Series: {", ".join(map(str, Fibonacci_Series))}"
        page.update()

    Fibonacci_Showing_Label: Text = ft.Text(value='',
                                 text_align=ft.TextAlign.LEFT,
                                 size=10,
                                 color='indigo'
                                 )

    Main_Heading: Text = ft.Text(value='FIBONACCI GENERATOR',
                                 text_align=ft.TextAlign.CENTER,
                                 size=24,
                                 weight=ft.FontWeight.BOLD,
                                 color='indigo'
                                 )

    User_Range_Input: TextField = ft.TextField(label='Fibonacci Range',
                                      value='1',
                                      text_align=ft.TextAlign.CENTER,
                                      width=120,
                                      color='pink'
                                      )
    User_Range_Input.on_change = Validation

    Generate_Button: ElevatedButton = ElevatedButton(text='Generate',
                                                   width=135,
                                                   icon=ft.icons.QR_CODE,
                                                   color='indigo',
                                                   on_click=Generate_Click,
                                                   disabled=False
                                                   )

    Subtract_Button: ft.IconButton =  ft.IconButton(icon=ft.icons.REMOVE,
                                                    icon_color=ft.colors.PINK,
                                                    on_click=Decrement_Function
                                                    )
    
    Addtion_Button: ft.IconButton =  ft.IconButton(icon=ft.icons.ADD,
                                                   icon_color=ft.colors.PINK,
                                                   on_click=Increment_Function
                                                   )
    
    
    





    page.add(
        Container(
            content=ft.Column(
                [
                    Container(
                        content=Main_Heading,
                        padding=ft.padding.all(10)
                    ),
                    Container(
                        content=ft.Row(
                            [
                                Subtract_Button,
                                User_Range_Input,
                                Addtion_Button
                            ],
                                alignment=ft.MainAxisAlignment.CENTER
                        ),
                            padding=ft.padding.all(10)
                    ),
                        Container(
                            content=Generate_Button,
                            padding=ft.padding.all(10)
                                ),
                        Container(
                            content=Fibonacci_Showing_Label,
                            padding=ft.padding.all(10)
                                )
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
                padding=ft.padding.all(10)
        )
    )

if __name__ == '__main__':
    ft.app(target=Main_Function)
    # ft.app(target=Main_Function, view=ft.WEB_BROWSER)
