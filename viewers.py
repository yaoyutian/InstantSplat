import os

THE_PATH = os.path.dirname(__file__)
exe_path =f"{THE_PATH}\\viewers\\bin\\SIBR_gaussianViewer_app.exe"
model_dir  = f"{THE_PATH}\\output\\infer"
os.system(f"{exe_path} -m {model_dir}")
