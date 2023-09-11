import numpy as np

art = """

      888   d8b        888                   888                    
      888   Y8P        888                   888                    
      888              888                   888                    
      888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
      888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
      888   888888     888   .d888888888     888   888  88888888888 
      Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
       "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  

"""


grid = """
  ❕   ❕  
➖➕➖➕➖
  ❕   ❕  
➖➕➖➕➖
  ❕   ❕   
"""


# grid = f"""
#  {grid_data[0][0]}❕{grid_data[0][1]}❕{grid_data[0][2]}
#  ➖➕➖➕➖
#  {grid_data[1][0]}❕{grid_data[1][1]}❕{grid_data[1][2]}
#  ➖➕➖➕➖
#  {grid_data[2][0]}❕{grid_data[2][1]}❕{grid_data[2][2]}
# """

grid_original = """
 ⭕❕⭕❕⭕
 ➖➕➖➕➖
 ⭕❕❌❕⭕
 ➖➕➖➕➖
 ❌❕❌❕⭕ 
"""

move_x = "❌"
move_o = "⭕"

how_to_grid_data = np.array([["1️⃣", "2️⃣", "3️⃣"],
                             ["4️⃣", "5️⃣", "6️⃣"],
                             ["7️⃣", "8️⃣", "9️⃣"]])


def make_grid(grid_data):
    temp_grid = f"""
     {grid_data[0][0]}❕{grid_data[0][1]}❕{grid_data[0][2]}
     ➖➕➖➕➖
     {grid_data[1][0]}❕{grid_data[1][1]}❕{grid_data[1][2]}
     ➖➕➖➕➖
     {grid_data[2][0]}❕{grid_data[2][1]}❕{grid_data[2][2]}
    """
    return temp_grid