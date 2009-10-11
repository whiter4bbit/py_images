import Image, ImageDraw
import math

color = (0,200,255,20)

sq_const = math.sqrt(3)/2

def put_triangle(draw, pos, a, iter, max_iter):
     na = a / math.pow(2, iter)
     nth = sq_const*na
     tops = (pos[0]-(na/2),pos[1]+nth)
     tope = (pos[0]+(na/2),pos[1]+nth)
     draw.line([tops,tope], fill=color)
     draw.line([(tops[0]+na/2,tops[1]+nth),tops], fill=color)
     draw.line([(tops[0]+na/2,tops[1]+nth), tope], fill=color)
     if iter<max_iter:
     	put_triangle(draw, pos, a, iter+1, max_iter)
	put_triangle(draw, tops, a, iter+1, max_iter)
	put_triangle(draw, tope, a, iter+1, max_iter)

def sierpinski_triangle(size, iters):
    img = Image.new("RGBA", size, color = (255,255,255))
    img.save('tmp.png')
    draw = ImageDraw.Draw(img)
    w,h = img.size
    a = w
    th = sq_const*a
    draw.line([(w/2,h-th), (0,h)], fill=color)
    draw.line([(w/2,h-th), (w,h)], fill=color)
    draw.line([(0,h),(w,h)], fill=color)
    put_triangle(draw, (w/2, h-th), a, 1, iters)    
    return img

if __name__=="__main__":
    img = sierpinski_triangle((400,400), 10)
    img.save('sample.png')

