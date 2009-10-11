import Image, ImageDraw

def create_blank(size):
    img = Image.new("RGBA", size, color=(255,255,255))
    img.save('sample.png')
    return img

import math

sqrt_const = math.sqrt(3)/2
color = (0,0,0)
blank = (255,255,255)

def triangle(draw, line, iter, iters):
    dx = line[1][0]-line[0][0] 
    dy = line[1][1]-line[0][1] 
    s_point = (line[0][0]+dx/3, line[0][1]+dy/3)
    e_point = (line[1][0]-dx/3, line[1][1]-dy/3)
    rotated = rotate_point(line[0], 120, s_point)
    if iter==iters:
       draw.line([s_point, rotated], fill=color)
       draw.line([rotated, e_point], fill=color)
    if iter<iters:
       triangle(draw, [s_point, rotated], iter+1, iters)
       triangle(draw, [rotated, e_point], iter+1, iters)
       triangle(draw, [e_point, line[1]], iter+1, iters)
       triangle(draw, [line[0], s_point], iter+1, iters)

def create_koch(img, iters):
    draw = ImageDraw.Draw(img)
    w,h = img.size
    ta = w/4*3
    th = sqrt_const*ta
    top = (w/2, h/12)
    triangle(draw, [(top[0]+ta/2, top[1]+th), (top[0]-ta/2, top[1]+th)],1,iters)
    triangle(draw, [top, (top[0]+ta/2, top[1]+th)],1, iters)
    triangle(draw, [(top[0]-ta/2, top[1]+th), top],1, iters)
    del draw

angle = lambda a: (a/float(180))*math.pi

from math import cos, sin

def rotate_point( point, a, offset):
    n_x = (point[0]-offset[0])*cos(angle(a)) - (point[1]-offset[1])*sin(angle(a))
    n_y = (point[0]-offset[0])*sin(angle(a)) + (point[1]-offset[1])*cos(angle(a))
    return (n_x+offset[0], n_y+offset[1])

if __name__=="__main__":
    img = create_blank((1000,1000))
    create_koch(img, 8)
    img.save('sample.png')
