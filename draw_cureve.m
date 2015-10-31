function draw_cureve(m)
    w = size(m,1);
    h = size(m,2);
    x=[];
    y=[];
    for i = 1:w*h
        [r c] = find(m==i);
        x = [x r];
        y = [y c];
    end
    plot(y,x)