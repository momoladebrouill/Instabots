from simple_image_download import simple_image_download as simp
def dwnld(indice,nb=1):
    response = simp.simple_image_download
    response().download(indice,nb)
    return response
if __name__=='__main__':
    response = simp.simple_image_download
    response().download("dieu",1)
