from bokeh.plotting import figure, save

p = figure(title="My first interactive plot!")

x_coords = [0,1,2,3,4]
y_coords = [5,4,1,2,0]
p.circle(x=x_coords, y=y_coords, size=10, color="red")
outfp = r"../docs/points.html"
save(obj=p, filename=outfp)