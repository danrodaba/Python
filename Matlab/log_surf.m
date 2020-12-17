p=0.1:0.1:4;
r=8:0.1:12;
[P,R]=meshgrid(p,r);
d=log(R./P);
surf(P,R,d)
xlabel('p')
ylabel('r')
zlabel('d')