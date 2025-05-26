"""
Input: HE slide, Polygons(STRtree) from HE slide,
       IHC slide

1. Extract bbox for each polygon from HE and IHC
2. Tile registration
3. Feature extraction

"""
import cv2
import pickle
from tqdm import tqdm
import numpy as np
import openslide
import skimage as ski
from pathlib import Path
from multiprocessing import Pool
from shapely import affinity
from shapely.geometry import Polygon


class Nuclei_features():
    def __init__(self, HE_filepath, IHC_filepath, strtree_filepath):
        self.he_slide = openslide.OpenSlide(HE_filepath)
        self.ihc_slide = openslide.OpenSlide(IHC_filepath)
         
        with open(strtree, 'rb') as f:
            self.strtree = pickle.load(f)
        
        self.nuclei_number = len(strtree.geometries)
    
    def get_nuclei_bbox(self, )
