import pygame
global animation_frames
animation_frames = {}




class Animation:
    def __init__(self):
        pass


    def load_animation(self, path, frame_time):
        animation_name = path.split('/')[-1]
        animation_framse_data = []
        n = 0
        for frame in frame_time:
            animation_frames_id = animation_name + str(n)
            img_location = path + '/' + animation_frames_id + '.png'
            animation_image = pygame.image.load(img_location).convert()
            animation_image.set_colorkey((255,255,255))
            animation_frames[animation_framse_id] = animation_image.copy()
            for i in range(frame):
                animation_framse_data.append(animation_frames_id)
            n+=1
            return animation_framse_data

            
animation_database['run'] = load_animation('./resources/PNG/Knight/Run',[7,7,7,7,7,7,7,7]) # ile klatek na każdy obrazek
animation_database['idle'] = load_animation('./resources/PNG/Knight/Idle',[10,10,10,10,10,10,10,10,10,10,10,10]) # ile klatek na każdy obrazek
