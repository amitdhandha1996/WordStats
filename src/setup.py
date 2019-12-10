import cx_Freeze

executables = [cx_Freeze.Executable("WordStats.py")]

cx_Freeze.setup(
    name="WordStats",
    options={"build_exe": {"packages": ['pymsgbox', 'matplotlib', 'numpy']}},
    version='1.1',
    description='A simple text analyzer.',
    author='Sean Xie',
    executables=executables
)
