import os
import subprocess
import glob


THE_PATH = os.path.dirname(__file__)

def get_jpg_files(jpg_path):
    #jpg_files = glob.glob(os.path.join(jpg_path,'*.jpg'))    # JPG
    #return jpg_files
    target_extensions={"jpg", "jpeg", "png","JPG", "JPEG", "PNG"}
    jpg_files = []
    for ext in target_extensions:
        jpg_files += glob.glob(os.path.join(jpg_path, f"*.{ext}"))
    print(len(jpg_files));  
    return jpg_files

gs_train_iter = 3000
pose_lr = "1x"



SCENE_NAME="bb0208_h"
SOURCE_PATH = f"{THE_PATH}/data/{SCENE_NAME}"
IMAGE_PATH = f"{SOURCE_PATH}/images"
IMAGE_FILES = get_jpg_files(IMAGE_PATH)
N_VIEW = len(IMAGE_FILES)

MODEL_PATH = f"{THE_PATH}/output/{SCENE_NAME}"
# Dust3r_coarse_geometric_initialization
CMD_D1 = [
    "python", "-W", "ignore", f"{THE_PATH}/init_geo.py",
    "-s", SOURCE_PATH,
    "-m", MODEL_PATH,
    "--n_views", str(N_VIEW),
    "--focal_avg",
    "--co_vis_dsp",
    "--conf_aware_ranking",
    "--infer_video"
]

# Train: jointly optimize pose
CMD_T = [
    "python", "-W", "ignore", f"{THE_PATH}/train.py",
    "-s", SOURCE_PATH,
    "-m", MODEL_PATH,
    "--n_views", str(N_VIEW),
    "--iterations", str(gs_train_iter),
    "--pp_optimizer",
    "--optim_pose"
]

# Render interpolated pose & output video
CMD_RI = [
    "python", "-W", "ignore", f"{THE_PATH}/render.py",
    "-s", SOURCE_PATH,
    "-m", MODEL_PATH,
    "--n_views", str(N_VIEW),
    "--iterations", str(gs_train_iter),
    "--infer_video"
]

print(f"========= : Dust3r_coarse_geometric_initialization =========")
subprocess.run(CMD_D1)

print(f"========= : Train: jointly optimize pose =========")
subprocess.run(CMD_T)

print(f"========= : Render interpolated pose & output video =========")
subprocess.run(CMD_RI)