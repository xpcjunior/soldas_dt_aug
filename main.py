import cv2 as cv
import numpy as np
import os
import service.TraditionalTransformationsService as tt_service
from service.FileManipulationsService import FileManipulationService


if __name__ == "__main__":

    fms = FileManipulationService(os.getcwd())

    imgs_solda = np.array(fms.get_original_imgs())

    angulos_de_rotacao = [90, 30, 45, -30, 12]
    
    for i, img in enumerate(imgs_solda):
        for angulo in angulos_de_rotacao:
            img_rotated = tt_service.rotation(img, angulo)
            fms.create_transformed_img(f'{i+1}-rot-{angulo}.png', img_rotated)