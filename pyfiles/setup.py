from cx_freeze import setup, Executable
base=None
executables=[Executable("main.py", base=base)]
packages=["random","pygame","math","cx_freeze"]
options={
    'build_exe':{
        'packages':packages,
    },
}
setup(
    name="Adventure Smash",
    options=options,
    version="2.0",
    description='undefined',
    executables=executables
)
