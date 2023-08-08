import cv2 as cv

def rotation(img, angle):

    # Se o angulo for 90,180 a rotacao padrao do opencv e feita
    match angle:
        case 90:
            return __default_rotation(img, cv.ROTATE_90_CLOCKWISE)
        case -90:
            return __default_rotation(img, cv.ROTATE_90_COUNTERCLOCKWISE)
        case 180:
            return __default_rotation(img, cv.ROTATE_180)
    
    # pega as dimensoes e calcula o centro da imagem
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # rotaciona no angulo dado a partir do centro da imagem
    M = cv.getRotationMatrix2D((cX, cY), angle, 1.0)

    # Pega o valor RGB de um pixel da imagem pra usar de background
    #branco = (255,255,255)
    b,g,r = (img[w-4, h-4])
    board_color=(int(b), int(g), int(r))

    rotated = cv.warpAffine(img, M, (w, h), borderValue=board_color)

    return rotated

def __default_rotation(img, angle):
    return cv.rotate(img, angle)

def flip(img, orientation = 'H'):
    return cv.flip(img, 0 if orientation == 'H' else 1)