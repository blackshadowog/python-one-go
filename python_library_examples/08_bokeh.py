from bokeh.plotting import figure, show

p = figure(title="Simple Bokeh Chart")
p.line([1, 2, 3, 4], [2, 5, 3, 7], line_width=2)
show(p)
