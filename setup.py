from cx_Freeze import setup, Executable
base = None
executables = [Executable("back/server.py", base=base)]
packages = ["idna", "speech_recognition", "asyncio", "datetime", "random", "websockets", "datetime", "json"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "PegasusSpeech",
    options = options,
    version = "1.0",
    description = 'Convertion audio text sur un site web',
    executables = executables
)