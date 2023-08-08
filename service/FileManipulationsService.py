import os
import cv2 as cv

class FileManipulationService():

    def __init__(self, path_workspaceFolder):
        self.path_img_src_folder = os.path.join(path_workspaceFolder, 'img_src')
        self.path_dist_folder = os.path.join(path_workspaceFolder, 'dist')
        if not os.path.exists(self.path_dist_folder):
            os.makedirs(self.path_dist_folder)
    
    def __get_original_img(self, img_name):
        return cv.imread(os.path.join(self.path_img_src_folder, img_name))
    
    def get_original_imgs(self):
        imgs_soldas = []
        imgs_soldas.append(self.__get_original_img('ausente.png'))
        imgs_soldas.append(self.__get_original_img('boa.png'))
        imgs_soldas.append(self.__get_original_img('excesso.png'))
        imgs_soldas.append(self.__get_original_img('ponte.png'))
        imgs_soldas.append(self.__get_original_img('pouca.png'))
        return imgs_soldas
    
    def create_transformed_img(self, t_img_name, t_img):
        cv.imwrite(os.path.join(self.path_dist_folder, t_img_name), t_img)