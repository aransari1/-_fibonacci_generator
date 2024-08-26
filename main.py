import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column, Container
from flet_core.control_event import ControlEvent
from Backend import Fibonacci_Generator

def Main_Function(page: ft.Page) -> None:
    page.title = "Fibonacci Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 600
    page.scroll = ft.ScrollMode.ALWAYS


    def Theme_Changer(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        Theme_Switch.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    Theme_Switch = ft.Switch(label="Light theme", on_change=Theme_Changer)

    def Decrement_Function(e: ControlEvent) -> None:
        try:     
            if not User_Range_Input.value.strip():
                User_Range_Input.value=1
            elif int(User_Range_Input.value) >0:
                User_Range_Input.value = str(int(User_Range_Input.value) - 1)
            elif int(User_Range_Input.value) <0:
                User_Range_Input.value = str(0)
            else:
                pass
        except ValueError:
            pass
        page.update()


    def Increment_Function(e: ControlEvent) -> None:
        try:     
            if not User_Range_Input.value.strip():
                User_Range_Input.value=1
            else:
                User_Range_Input.value = str(int(User_Range_Input.value) + 1)
        except ValueError:
            pass
        page.update()

    def Validation(e: ControlEvent) -> None:
        if User_Range_Input.value.strip():
            try:
                # Attempt to convert the input value to an integer
                int_value = int(User_Range_Input.value)
                Generate_Button.disabled = False
                if int_value < 1:
                    Fibonacci_Showing_Label.value = "⚠️Warning!⚠️\nRange can't be in zero or negative number"
                    Fibonacci_Showing_Label.color = 'orange600'
                    Fibonacci_Showing_Label.size = '12'
                    Fibonacci_Showing_Label.text_align = 'CENTER'
                    Generate_Button.disabled = True 
                elif int_value > 1000:
                    Fibonacci_Showing_Label.value = "⚠️Warning!⚠️\nEntering higher range may decrease your PC performance for a while"
                    Fibonacci_Showing_Label.color = 'orange'
                    Fibonacci_Showing_Label.size = '12'
                    Fibonacci_Showing_Label.text_align = 'CENTER'
                    page.update()
                else:
                    Fibonacci_Showing_Label.value = ''
                page.update
            except ValueError:
                # If conversion fails, it's not an integer
                Fibonacci_Showing_Label.value = "⚠️Wrong input value!⚠️\nPlease enter an integer value"
                Fibonacci_Showing_Label.color = 'orange'
                Fibonacci_Showing_Label.size = '12'
                Fibonacci_Showing_Label.text_align = 'CENTER'
                Generate_Button.disabled = True
                page.update()
        else:
            Fibonacci_Showing_Label.value = "⚠️No input value!⚠️\nPlease give valid input"
            Fibonacci_Showing_Label.color = 'red'
            Fibonacci_Showing_Label.size = '13'
            Fibonacci_Showing_Label.text_align = 'CENTER'
            Generate_Button.disabled = True
            
            page.update()
        page.update()


    def Generate_Click(e):
        Fibonacci_Series = Fibonacci_Generator(int(User_Range_Input.value))
        Fibonacci_Showing_Label.value = ',\n'.join(map(str, Fibonacci_Series))
        Fibonacci_Showing_Label.color = 'indigo'
        Fibonacci_Showing_Label.size = '10'
        Fibonacci_Showing_Label.text_align = 'LEFT'
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
    
    # Adding the widgets to the page.
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
                            content=ft.Row(
                                [
                                    Generate_Button,
                                    Theme_Switch
                                ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                            ),

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


ft.app(Main_Function)
