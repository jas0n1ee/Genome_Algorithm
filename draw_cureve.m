function draw_cureve(m)
    w = size(m,1);
    x=[];
    y=[];
    for i = 1:w^2
        [r c] = find(m==i);
        x = [x r];
        y = [y c];
    end
    plot(x,y)