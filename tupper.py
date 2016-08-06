import tkinter as tk

cell_width = 10
cell_height = 10

hor_cells = 106
ver_cells = 17

canvas_height = cell_height * ver_cells
canvas_width = cell_width * hor_cells

#drawing_matrix = [[None for j in range(ver_cells)] for i in range(hor_cells)]
drawing_matrix = [[None for j in range(hor_cells)] for i in range(ver_cells)]

def toggle_cell(event):
    x = event.x
    y = event.y

    chosen_cell_x = int(x//cell_width)
    chosen_cell_y = int(y//cell_height)

    #print("Cell: " + str(chosen_cell_x) + ", " + str(chosen_cell_y))
    #print("Coords: " + str(event.x) + ", " + str(event.y))
    
    if(not drawing_matrix[chosen_cell_y][chosen_cell_x]):
        drawing_matrix[chosen_cell_y][chosen_cell_x] = canvas.create_rectangle(cell_width * chosen_cell_x,
                                                                               cell_height * chosen_cell_y,
                                                                               cell_width * (chosen_cell_x + 1),
                                                                               cell_height * (chosen_cell_y + 1),
                                                                               fill="black")
    else:
        canvas.delete(drawing_matrix[chosen_cell_y][chosen_cell_x])
        drawing_matrix[chosen_cell_y][chosen_cell_x] = None

    

def clear_drawing_matrix():
    for i in range(hor_cells):
        for j in range(ver_cells):
            canvas.delete(drawing_matrix[j][i])
            drawing_matrix[j][i] = None


def get_k():
    total_k_bin = ''
    for i in range(hor_cells):
        #print(len(drawing_matrix[0]))
        column = [1 if row[i] != None else 0 for row in drawing_matrix]
        #column.reverse()
        
        k_part_bin = ''.join([str(digit) for digit in column])
        #print(k_part_bin)
        total_k_bin = k_part_bin + total_k_bin

    k_value = int(total_k_bin, 2)*17
    k_textbox.delete(0, 'end')
    k_textbox.insert(0, k_value)

    print('K = ' + str(k_value), end='\n')

'''
def draw_k():
    k_value = int(k_textbox.get())
    total_k_bin = bin(k_value)[2:]
    for i in range(hor_cells):
        column = 
'''

top = tk.Tk()

text_label = tk.Label(top, text="Hello!")
text_label.grid(row = 1, column = 1)

# Canvas
canvas = tk.Canvas(top, bg="white", height=canvas_height, width=canvas_width)
canvas.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)

canvas.bind("<Button-1>", toggle_cell)


# K label and textbox
k_frame = tk.Frame(top)
k_frame.grid(row = 3, column = 1, padx = 5, pady = 5)

k_label = tk.Label(k_frame, text="K=")
k_label.pack(side = "left")

k_textbox = tk.Entry(k_frame)
k_textbox.pack(side = "left")

k_textbox.text = 'sadfdsf'

# Clear and Get K buttons
clear_get_frame = tk.Frame(top)
clear_get_frame.grid(row = 3, column = 2)

clear_button = tk.Button(clear_get_frame, text = "Clear", command = clear_drawing_matrix)
clear_button.pack(side="left", padx = 5, pady = 5)

get_k_button = tk.Button(clear_get_frame, text = "Get K", command = get_k)
get_k_button.pack(side="left", padx = 5, pady = 5)

draw_k_button = tk.Button(clear_get_frame, text = "Draw K")
get_k_button.pack(side="left", padx = 5, pady = 5)


top.mainloop()
