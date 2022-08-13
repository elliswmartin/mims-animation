# mims-animation
 Jupyter notebook that animates a Python Turtle rainbow drawing. Created during MIMS bootcamp alongside 4 classmates. 
 
# How It Works
Relies on `draw_rainbow` to create single rainbow at a desired starting point. As `start_x` is increased at a regular internal, animation begins. 

```
def move_rainbow(start_x, start_y, num_frames, screen, sleeptime):
    for j in range(num_frames):
        if j < num_frames // 2:
            start_x = start_x + 20
        if j > num_frames // 2:
            start_x = start_x - 20
        draw_rainbow(start_x, start_y)
        screen.update()
        time.sleep(sleeptime)
        clear()
```

![unnamed](https://user-images.githubusercontent.com/54450015/184468146-e79cf230-f016-4e93-8981-c7058d520f5d.gif)
