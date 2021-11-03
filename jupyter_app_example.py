import ipywidgets as widgets
from IPython.display import display, clear_output

qty = widgets.Dropdown(options=list(range(0, 100, 1)), value=0, description='Quantity')
qty1 = widgets.Dropdown(options=list(range(0, 100, 1)), value=0, description='Quantity')
qty2 = widgets.Dropdown(options=list(range(0, 100, 1)), value=0, description='Quantity')

containers = ['option1', 'option2', 'etc']

cnt = widgets.Dropdown(options=containers, value='None', description='x')
cnt1 = widgets.Dropdown(options=containers, value='None', description='y')
cnt2 = widgets.Dropdown(options=containers, value='None', description='z')

service_cycle = widgets.Dropdown(
    options=list(range(1, 8,1)),
    value=2,
    description='description',
    disabled=False,
)

cycle_unit = widgets.Dropdown(
    options=['DAY', 'WEEK', 'MONTH'],
    value='WEEK',
    description='description',
    disabled=False,
)

run = widgets.Button(
    description='Calculate',
    disabled=False,
    button_style='success',
    tooltip='Calculate',
    icon='check'
)

service = widgets.RadioButtons( options=['One', 'Two'], value='value')
site = widgets.RadioButtons( options=['One', 'Two'], value='value')
freq = widgets.Checkbox(value=False, description='check this')

output = widgets.Output()

def on_button_clicked(run):
    order_dict = {cnt.value: qty.value, cnt1.value: qty1.value, cnt2.value: qty2.value}
    if freq.value == False:
        x = 2
    else:
        x = 8
    with output:
        clear_output()
        # replace with new function
        a = ratecard.RateCard(site=site.value, service=service.value, 
                     container_qty_dict={k:v for k,v in order_dict.items() if k != 'None'}, 
                     servicecycleunit='WEEK',
                    servicecycle=x)
        print(a.__str__)

# display(run, output)
run.on_click(on_button_clicked)

# create a 10x2 grid layout
grid = widgets.GridspecLayout(10, 16)
# fill it in with widgets
grid[0:2, 1:10] = widgets.HTML("<h1>Example app</h1><p>fill with new values</p> ")
grid[2, 1:5] = service
grid[2, 5:10] = site
grid[4, 0:6] = cnt
grid[5, 0:6] = cnt1
grid[6, 0:6] = cnt2
grid[4, 6:16] = qty
grid[5, 6:16] = qty1
grid[6, 6:16] = qty2
grid[7, 0:5] = freq
grid[7, 5:] = run
grid[8,0] =widgets.HTML("<b>Output: </b>")
grid[8, 2:] = output
# run
grid
