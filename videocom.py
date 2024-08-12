import moviepy.editor as mp
import cv2 as cv
import os
import glob2
import random2

clip_fps = 30
target_size = (1080, 1920)
folder_path = "D:/projects/about-inspiration/Videos/all"
keywords = ['success', 'victory', 'celebrate', 'sunset', 'love']
max_clips_per_keyword = 2

def combine_clips(clips):
    final_clip = clips[0].subclip(0,2)
    for i in range(1, len(clips)):
        final_clip = mp.concatenate_videoclips([final_clip, clips[i].subclip(0,2).set_fps(clip_fps)], method='compose')
    
    return final_clip

def resize_video(clip, target_size):
    width, height = target_size
    
    def resize_frame(frame):
        return cv.resize(frame, (width, height))
    
    return clip.fl_image(resize_frame)

def get_clips(keywords, max_clips_per_keyword):
    clips = []
    used_clips = set()
    for keyword in keywords:
        search_pattern = f"D:/projects/about-inspiration/Videos/all/*{keyword}*.mp4"
        clip_paths = glob2.glob(search_pattern, recursive=True)
        available_clips = [clip for clip in clip_paths if clip not in used_clips]
        selected_clips = random2.sample(available_clips, min(max_clips_per_keyword, len(available_clips)))
        used_clips.update(selected_clips)
        clips.extend([resize_video(mp.VideoFileClip(clip), target_size) for clip in selected_clips])
    return clips

clips = get_clips(keywords, max_clips_per_keyword)

combined_clip = combine_clips(clips)

combined_clip.write_videofile("output.mp4", fps=clip_fps)