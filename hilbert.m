function r = hilbert(n)
    if n == 1
        r = [1 4;2 3];
    elseif mod(n,2) == 0
        t = hilbert(n-1);
        l = 2*(n-1);
        r = [t                    t'+2^l;
            rot90(rot90(t))+2^l*3 t'+2^l*2];
    else 
        t = hilbert(n-1);
        l = 2*(n-1);
        r = [t        rot90(rot90(t))+2^l*3;
             t'+2^l   t'+2^l*2];
    end
