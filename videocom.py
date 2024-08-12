import moviepy.editor as mp
import os
import glob2
import random2

clip_fps = 24
folder_path = "D:/projects/about-inspiration/Videos/all"
keywords = [ "man", "friends", 'luck']
max_clips_per_keyword = 1

def combine_clips(clips):
    final_clip = clips[0].subclip(0,2)
    for i in range(1, len(clips)):
        final_clip = mp.concatenate_videoclips([final_clip, clips[i].subclip(0,2).set_fps(clip_fps)], method='compose')
    
    return final_clip

def get_clips(folder_path, keywords, max_clips_per_keyword):
    clips = []
    for keyword in keywords:
        search_pattern = f"D:/projects/about-inspiration/Videos/all/*{keyword}*.mp4"
        clip_paths = glob2.glob(search_pattern, recursive=True)
        # num_clips = random2.randint(1, max_clips_per_keyword)
        selected_clips = random2.sample(clip_paths, min(max_clips_per_keyword, len(clip_paths)))
        clips.extend(selected_clips)

    return [mp.VideoFileClip(clip) for clip in clips]

clips = get_clips(folder_path, keywords, max_clips_per_keyword)

combined_clip = combine_clips(clips)

combined_clip.write_videofile("output3.mp4", fps=clip_fps)