from flet import *

phone = TextField(prefix_icon=icons.PHONE, height=60,hint_text="Phone number", bgcolor="#D9D9D9", border_radius=12, border=0, border_color="#3871A5")
password = TextField(hint_text="Password",prefix_icon=icons.LOCK,password=True,height=60, bgcolor="#D9D9D9", border_radius=12, border=0, border_color="#3871A5")


login_container = Container(
        margin=margin.only(top=40),
    
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                    Container(alignment=alignment.center,content=Text(value="INELVABOT", color="#FFFFFF", size=48)),
                    Container(height=80),
                    phone,
                    password,
                    Container(
                        alignment=alignment.center,content=Container(
                            content=TextButton(
                                text="Login",
                                icon=icons.LOGIN,
                                width=200,
                                height=50,
                                style=ButtonStyle(
                                    elevation=2,
                                    color="#FFFFFF")
                                    ),
                                border_radius=border_radius.all(20),
                                border=border.all(
                                    color="#FFFFFF",width=2))),
                    Container(alignment=alignment.center,content=Text(value="Or", style=TextStyle(size=32, color="#FFFFFF"))),
                    Container(alignment=alignment.center,content=Container(
                            content=TextButton(
                                text="Register",
                                icon=icons.APP_REGISTRATION_ROUNDED,
                                width=200,
                                height=50,
                                style=ButtonStyle(
                                    elevation=2,
                                    color="#3871A5")
                                    ),
                                border_radius=border_radius.all(20),
                                bgcolor="#FFFFFF"
                                )),
                      

                      ],))
