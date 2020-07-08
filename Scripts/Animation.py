import pygame
from Scripts.Player import Player
from Scripts.Vector import Vector
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


    def change_action(action_var,frame,new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame
                
    animation_database['Run'] = load_animation('./resources/PNG/Knight/Run',[7,7,7,7,7,7,7,7]) # ile klatek na każdy obrazek
    animation_database['Idle'] = load_animation('./resources/PNG/Knight/Idle',[10,10,10,10,10,10,10,10,10,10,10,10]) # ile klatek na każdy obrazek


    player_action = 'Idle'
    player_frame = 0
    player_flip = False


    # Wywołanie animacji 
    if moveDir[0] == 0:
        player_action,player_frame = change_action(player_action,player_frame,'Idle')
    if moveDir[0] > 0:
        player_flip = False
        player_action,player_frame = change_action(player_action,player_frame,'Run')

    # Miało być flipowanie postaci gdy idzie w innym kierunku xd
    if moveDir[0] < 0:
        player_flip = True
        player_action,player_frame = change_action(player_action,player_frame,'Run')


