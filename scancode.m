function r = scancode(n)
    if n <=4
        r = reshape(1:2^(2*n),2^n,2^n)';
    else
        t = scancode(n-1);
        d = 2^(2*n-2);
        r = [t t+d; t+2*d t+3*d];
    end
end