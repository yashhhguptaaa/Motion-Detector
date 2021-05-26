from motion_detector import df
from bokeh.plotting import show,figure,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%D %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%D %H:%M:%S")


cds=ColumnDataSource(df)

f=figure(x_axis_type='datetime',title="Motion Graph",responsive=True,height=100,width=500)
f.yaxis.minor_tick_line_color=None
f.ygrid[0].ticker_desired_num_ticks=1
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)

f.quad(left="Start",right="End",top=1,bottom=0,color="red",source=cds)
output_file("Graph.html")
show(f)